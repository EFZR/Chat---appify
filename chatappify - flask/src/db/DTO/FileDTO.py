class FileDTO:
    def __init__(
        self,
        id=None,
        name=None,
        path=None,
        size=None,
        type=None,
        entity_id=None,
        table_id=None,
        created_at=None,
    ):
        self.__id = id
        self.__name = name
        self.__path = path
        self.__size = size
        self.__type = type
        self.__entity_id = entity_id
        self.__table_id = table_id
        self.__created_at = created_at

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def path(self):
        return self.__path

    @path.setter
    def path(self, value):
        self.__path = value

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, value):
        self.__type = value

    @property
    def entity_id(self):
        return self.__entity_id

    @entity_id.setter
    def entity_id(self, value):
        self.__entity_id = value

    @property
    def table_id(self):
        return self.__table_id

    @table_id.setter
    def table_id(self, value):
        self.__table_id = value

    @property
    def created_at(self):
        return self.__created_at

    @created_at.setter
    def created_at(self, value):
        self.__created_at = value

    def __str__(self):
        return f"File({self.name}: {self.id})"
