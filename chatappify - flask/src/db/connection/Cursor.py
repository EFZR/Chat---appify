from .Connection import Connection


class Cursor:
    def __init__(self):
        self.__connection = Connection.connection()
        self.__cursor = None

    def __enter__(self):
        self.__cursor = self.__connection.cursor()
        return self.__cursor

    def __exit__(self, type, value, traceback):
        if value:
            self.__connection.rollback()
        else:
            self.__connection.commit()
        self.__cursor.close()
