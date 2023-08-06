from jdatabase.jdatabase import Jdatabase
from jdatabase import processors
import random, string, datetime


"""
create helper tables when the dataclass is imported.

when the dataclass is used, any changes will only be recorded on the database when the save() method is run.
after the class that is inheriting the dataclass, in the same module, the make method must be called on the class
(ex DataClass.make(SubClass)).

the columns in the table are completely based on the class variables of the sub class, and the column types are based
on the variables default value. the primary key is the first instance argument/variable. if a column is set to another
class (ex tickets = Tickets) that inherits the DataClass, the other classes primary key will be stored in the column
for that variable, however that variable can be treated as the instance of the other class when accessed by the class.

class init takes in kwargs, have method called in init of sub class to search with these vars for the object init
"""


class DataClass:
    """
    class that creates a table in the connected database based on any class that inherits this class when the creation
    process is run
    """

    _jdb = None
    _jd = None
    _columns = []
    _search_keys = {}
    _data = {}
    _types = {}
    _structure = {}

    _name = None
    _classname = None

    __created_tables = []

    def __init__(self):
        self._jd = None
        self._columns = []
        self._search_keys = {}
        self._data = {}
        self._types = {}
        self._structure = {}
        self._classname = str(self.__class__.__name__).lower()
        self._name = self._classname
        self._init_setup()
        if self._jdb is not None:
            self.__init_tables()
            if len(self._columns) > 1:
                for item in self.__dict__:
                    if not item.startswith("_"):
                        self._search_keys[item] = self.__dict__[item]
                self.__init_table_structure()
                self.__init_check_for_table()

    def __init_tables(self):

        # recreates the tables if their structure has changed
        def check_recreate(self, controller_structure, import_log_structure):

            def calculate_columns_from_structure(structure):
                store = []
                for item in structure:
                    store.append(item)
                return store

            # checks column match given structure and columns
            def match_check(columns, structure):
                if structure == columns:
                    return True
                return False

            controller_columns = self._jdb.get_one("jdatabase_info", where=("table_name=%s", ["jdatabase_controller"]))[1]
            import_log_columns = self._jdb.get_one("jdatabase_info", where=("table_name=%s", ["jdatabase_import_log"]))[1]

            if not match_check(controller_columns, controller_structure):
                processors.import_table_same_name(self._jdb, "jdatabase_controller",
                                                  controller_columns,
                                                  calculate_columns_from_structure(controller_structure))
            if not match_check(import_log_columns, import_log_structure):
                processors.import_table_same_name(self._jdb, "jdatabase_controller",
                                                  controller_columns,
                                                  calculate_columns_from_structure(controller_structure))

        """
        creates Jdatabase tables if not created

        Tables:
          jdatabase_controller - tracks all table names, columns, and column values
          jdatabase_import_log - tracks all table imports and their changes
        """
        controller_structure = {
            "table_name": ["VARCHAR(256)", "PRIMARY KEY"],
            "class_name": ["TEXT(0)", "NOT NULL"],
            "test": ["TEXT(0)", "NOT NULL"],
        }
        import_log_structure = {
            "jd": ["VARCHAR(32)", "PRIMARY KEY"],  # TODO randomize 32 chars
            "table_name": ["TEXT(0)", "NOT NULL"],
            "old_columns": ["TEXT(0)", "NOT NULL"],
            "new_columns": ["TEXT(0)", "NOT NULL"],
            "old_structure": ["TEXT(0)", "NOT NULL"],
            "new_structure": ["TEXT(0)", "NOT NULL"],
            "import_runtime": ["TIME(0)", "NOT NULL"],
            "import_datetime": ["DATETIME(0)", "NOT NULL"],
        }
        self._jdb.create_table_if_false_check("jdatabase_controller", controller_structure)
        self._jdb.create_table_if_false_check("jdatabase_import_log", import_log_structure)
        check_recreate(self, controller_structure, import_log_structure)

    def _init_setup(self):
        """
        gets columns, data, and types from subclass
        """
        for item in self.__dir__():
            item = str(item)
            item_val = self.__getattribute__(item)
            if not item.startswith("_") and not str(item_val).startswith("<"):
                self._columns.append(item)
                self._data[item] = item_val
                self._types[item] = type(item_val)
            # if str(item_val).startswith("<"):
                # TODO

    def __init_table_structure(self):
        """
        sets up _structure for creating the table
        """
        count = 0
        max_primary = 0
        for item in self._types:
            item_type = str(self._types[item]).split("'")[1]

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
                self._structure[item] = [f"{item_type.upper()}({max_primary})", "PRIMARY KEY"]
                count += 1
            else:
                self._structure[item] = [f"{item_type.upper()}(0)", "NOT NULL"]

    def __init_check_for_table(self):
        """
        checks to see if there is a table in the database corresponding to the subclass structure
        """
        data = self._jdb.get_one("jdatabase_controller", where=("class_name=%s", [str(self._classname)]))
        if data is not None:
            if data[3] == str(self._columns):
                self._name = data[1]
                if not self.__get_data():
                    self.__upload_data()
                return
            else:
                def string_remove(remove_string, *args):
                    for arg in args:
                        remove_string = remove_string.replace(arg, "")
                    return remove_string
                self.__init_create_table()
                data_cols = string_remove(data[3], "[", "]", ",", "'").split()
                runtime = processors.import_table(self._jdb,
                                                  {"table_name": data[1],
                                                   "columns": {
                                                       col_name: None for col_name in data_cols
                                                   }},
                                                  {"table_name": self._name,
                                                   "columns": {
                                                       col_name: self._data[col_name] for col_name in self._columns
                                                   }})
                self._jdb.drop_table(data[1])
                self._jdb.delete("jdatabase_controller", where=("table_name=%s", [data[1]]))
                self._jdb.insert("jdatabase_import_log", {"jd": self._jd,
                                                          "old_table_name": data[1],
                                                          "new_table_name": self._name,
                                                          "old_columns": data[3],
                                                          "new_columns": str(self._columns),
                                                          "old_structure": data[4],
                                                          "new_structure": str(self._structure),
                                                          "import_runtime": runtime,
                                                          "import_datetime": datetime.datetime.utcnow(),
                                                          })
                if not self.__get_data():
                    self.__upload_data()
                return
        self.__init_create_table()
        return

    def __init_create_table(self):
        self._jd = self.__key_gen()
        self._name = self._name + "_" + self._jd
        self._jdb.create_table(self._name, self._structure)
        self._jdb.insert("jdatabase_controller", {"jd": self._jd,
                                                  "table_name": self._name,
                                                  "class_name": self._classname,
                                                  "columns": str(self._columns),
                                                  "structure": str(self._structure),
                                                  "creation_datetime": datetime.datetime.utcnow()})

    def __upload_data(self):
        self._jdb.insert_or_update(self._name, self._data, keys=self.__get_where_keys())

    def __get_data(self):
        rdata = self._jdb.get_one(self._name, where=self.__get_where())
        if rdata is not None:
            count = 0
            for item in self._data:
                self.__setattr__(item, rdata[count])
                self._data[item] = rdata[count]
                count += 1
            return True
        return False

    def __get_where(self):
        where_construct = ""
        where_vals = []
        for skey in self._search_keys:
            where_construct += f"{skey}=%s" if len(where_construct) <= 1 else f" and {skey}=%s"
            where_vals.append(self._search_keys[skey])
        return where_construct, where_vals

    def __get_where_keys(self):
        keys = []
        for skey in self._search_keys:
            keys.append(skey)
        return keys

    """ GENERATOR methods """
    @staticmethod
    def __r_gen(length):
        return ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(length))

    def __jd_gen(self):
        return self.__r_gen(64)

    def __key_gen(self):
        return self.__r_gen(6)
    """ end GENERATOR methods """

    """ CLASS USAGE methods """
    def get(self, what):
        """
        retrieves the data from the database, and then give you the value for the corresponding variable 'what'
        also updates the object variable and internal data store

        :param what: variable name for data to be returned
        :return: data belonging to the variable in the database
        """
        self.__get_data()
        return self._data[str(what)]

    def get_all(self):
        """
        pulls and returns the data for the entire object from the database

        :return: intrenal data store
        """
        self.__get_data()
        return self._data

    def set(self, what, to):
        """
        sets the objects variable 'what' to a value 'to' in the database, internal data store, and the object itself

        :param what: variable name
        :param to: value to set variable to
        :return: True
        """
        self.__setattr__(str(what), to)
        self._data[str(what)] = to
        self.__upload_data()
        self.__get_data()
        return True

    def set_all(self):
        """
        sets the objects variables values to the values in the database

        :return: True
        """
        for item in self._data:
            self._data[item] = vars(self)[item]
        self.__upload_data()
        self.__get_data()
        return True
    """ end CLASS USAGE methods """

    """ SETUP methods """
    def connect(self, host, user, passwd, db):
        """
        sets up the connection for all instances of DataClass

        :param host: database hostname
        :param user: database username
        :param passwd: database passwd
        :param db: database name
        :return: True
        """
        DataClass._jdb = Jdatabase(host=host, user=user, passwd=passwd, db=db, track=True)
        return True

    @staticmethod
    def make():
        pass

    def make_all(self):
        pass
    """ end SETUP methods """


class Tickets(DataClass):
    id = int(0)
    message_count = int(0)

    @staticmethod
    def make():
        super().make()

    def __init__(self, id):
        self.id = id


class Messages(DataClass):
    id = int(0)
    user = str(0)

    def __init__(self, id):
        self.id = id

    @staticmethod
    def make():
        super().make()


# Tickets.make()
# Messages.make()
#
# messages = [Messages(0), Messages(1), Messages(2), Messages(3), Messages(4)]
