from jdatabase.jdatabase import Jdatabase
import datetime


class Logger:
    """
    class that creates a table in the database based on the name given on instantiation, can then be used to 'log'
    items in that table with one method.
    """

    table_name = None
    _jdb = None

    def __init__(self, name):
        self.table_name = "jdatabase_" + str(name) + "_log"

    def log(self, timestamp=datetime.datetime.utcnow(), system=None, user=None, content=None):
        """
        forms a log entry and inserts it into the database table corresponding to the instantiation name as a row

        :param timestamp:
        :param system:
        :param user:
        :param content:
        :return:
        """
        pass

    def connect(self, host, user, passwd, db):
        """
        sets up the connection for all instances of Logger

        :param host: database hostname
        :param user: database username
        :param passwd: database passwd
        :param db: database name
        :return: True
        """
        Logger._jdb = Jdatabase(host=host, user=user, passwd=passwd, db=db)
        return True
