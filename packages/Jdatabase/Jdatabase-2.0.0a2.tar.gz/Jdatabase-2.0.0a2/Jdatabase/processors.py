import datetime


def import_table(jdb, old_table, new_table):
    """
    imports all the data in a table into a new table with similar structure

    compare columns, adding all corresponding indexes to the col_to_col_indexes
    form a structure for imports taking the values from each row in the old table and adding any default values
    get all the data from the old table, and for each row in the data, add the row to the new table

    param structure for both old_table and new_table:
        {
            "table_name": "table_name",
            "columns": {
                "column_name": default_value,
                "column_name": default_value,
            }
        }

    :param: jdb: Jdatabase object connecting to the database with the two tables
    :param: old_table: dict with key values `table_name`: `the table name` (string) and `columns`: `the columns and
    their default values` (a dict containing the column names as keys with their default value as the value) for the
    table the data is being imported from
    :param: new_table: dict with key values `table_name`: `the table name` (string) and `columns`: `the columns and
    their default values` (a dict containing the column names as keys with their default value as the value) for the
    table the data is being inserted into
    :return: runtime when successful, error on error
    """

    try:

        start_time = datetime.datetime.utcnow()
        print(f"IMPORTING TABLE {old_table['table_name']} into {new_table['table_name']}...")

        # form column lists
        old_table_column_list = [column for column in old_table["columns"]]
        new_table_column_list = [column for column in new_table["columns"]]

        # compare columns
        col_to_col_indexes = {}
        known_new_indexes = []
        for column in new_table_column_list:
            if column in old_table_column_list:
                # add comparable columns to col_to_col_indexes
                col_to_col_indexes[new_table_column_list.index(column)] = old_table_column_list.index(column)
                # add new column index to known new indexes
                known_new_indexes.append(new_table_column_list.index(column))

        # form new table structure
        new_table_structure = {}
        # add either the index in the old table, or the default value to new_table_structure, key is column index
        count = 0
        for column in new_table["columns"]:
            if count in known_new_indexes:
                new_table_structure[count] = ["index", col_to_col_indexes[count]]
            else:
                new_table_structure[count] = ["default", new_table["columns"][column]]
            count += 1

        # get data from old table
        old_data = jdb.get_all(old_table["table_name"])
        # batch store for batch import
        batch_insert = []
        # add each row to the new table using the structure
        for row in old_data:
            # form insert
            insert = {}
            count = 0
            for column in new_table["columns"]:
                if new_table_structure[count][0] == "index":
                    # index val, pull from old data row's index
                    insert[column] = row[new_table_structure[count][1]]
                else:
                    insert[column] = new_table_structure[count][1]
                count += 1
            # insert row
            batch_insert.append(insert)

        # execute batch import
        jdb.insert_batch(new_table["table_name"], batch_insert)

        print(f"FINISHED IMPORTING TABLE {old_table['table_name']} into {new_table['table_name']}.")

        end_time = datetime.datetime.utcnow()

        return end_time - start_time

    except Exception as error:
        return error


def import_table_same_name(jdb, table_name, old_table_columns, new_table_columns):
    """
    recreates a table and imports data given a table name, and the columns for the current (old) table and the new table

    columns structure:
        {
            "column_name": default_value,
            "column_name": default_value,
        }

    :param jdb:
    :param table_name:
    :param old_table_columns:
    :param new_table_columns:
    :return:
    """

    try:

        start_time = datetime.datetime.utcnow()
        print(f"REMAKING AND IMPORTING TABLE {table_name}...")

        # form column lists
        old_table_column_list = [column for column in old_table_columns]
        new_table_column_list = [column for column in new_table_columns]

        # compare columns
        col_to_col_indexes = {}
        known_new_indexes = []
        for column in new_table_column_list:
            if column in old_table_column_list:
                # add comparable columns to col_to_col_indexes
                col_to_col_indexes[new_table_column_list.index(column)] = old_table_column_list.index(column)
                # add new column index to known new indexes
                known_new_indexes.append(new_table_column_list.index(column))

        # form new table structure
        new_table_structure = {}
        # add either the index in the old table, or the default value to new_table_structure, key is column index
        count = 0
        for column in new_table_columns:
            if count in known_new_indexes:
                new_table_structure[count] = ["index", col_to_col_indexes[count]]
            else:
                new_table_structure[count] = ["default", new_table_columns[column]]
            count += 1

        # get data from old table
        old_data = jdb.get_all(table_name)
        # batch store for batch import
        batch_insert = []
        # add each row to the new table using the structure
        for row in old_data:
            # form insert
            insert = {}
            count = 0
            for column in new_table_columns:
                if new_table_structure[count][0] == "index":
                    # index val, pull from old data row's index
                    insert[column] = row[new_table_structure[count][1]]
                else:
                    insert[column] = new_table_structure[count][1]
                count += 1
            # insert row
            batch_insert.append(insert)

        # delete and recreate the table
        jdb.drop_table(table_name)
        # calculate new_table_structure
        new_table_structure = gen_structure_from_columns_default(new_table_columns)
        jdb.create_table(table_name, new_table_structure)

        # execute batch import
        jdb.insert_batch(table_name, batch_insert)

        print(f"FINISHED RECREATION AND IMPORT OF TABLE {table_name}.")

        end_time = datetime.datetime.utcnow()

        return end_time - start_time

    except Exception as error:
        return error


def gen_structure_from_columns_default(columns):
    """
    takes a given input of columns and returns the structure sql for the columns

    columns structure:
        {
            "column_name": default_value,
            "column_name": default_value,
        }

    :param columns: columns
    :return: sql column structure
    """

    # calculate types
    types = {}
    for item in columns:
        item = str(item)
        item_val = columns[item]
        if not item.startswith("_") and not str(item_val).startswith("<"):
            types[item] = type(item_val)

    # calculate structure
    structure = {}
    count = 0
    max_primary = 0
    for item in types:
        item_type = str(types[item]).split("'")[1]

        if item_type == "str":
            item_type = "text"
            max_primary = 256
        elif item_type == "int":
            max_primary = 32
        elif item_type.lower().startswith("date"):
            item_sub_type = item_type.lower().split(".")[1]
            if item_sub_type.startswith("time"):
                item_type = "time"
            else:
                item_type = "datetime"
            max_primary = 0

        if count == 0:
            structure[item] = [f"{item_type.upper()}({max_primary})", "PRIMARY KEY"]
            count += 1
        else:
            structure[item] = [f"{item_type.upper()}(0)", "NOT NULL"]

    return structure
