class ChatroomDTO:
    def __init__(
        self, id=None, name=None, key_room=None, created_at=None, last_message=None
    ):
        self.__id = id
        self.__name = name
        self.__key_room = key_room
        self.__created_at = created_at
        self.__last_message = last_message

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
    def key_room(self):
        return self.__key_room

    @key_room.setter
    def key_room(self, value):
        self.__key_room = value

    @property
    def created_at(self):
        return self.__created_at

    @created_at.setter
    def created_at(self, value):
        self.__created_at = value

    @property
    def last_message(self):
        return self.__last_message

    @last_message.setter
    def last_message(self, value):
        self.__last_message = value

    def __str__(self):
        return f"{self.id}: {self.name}"
