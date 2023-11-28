class UserDTO:
    def __init__(
        self,
        id=None,
        username=None,
        password=None,
        is_active=None,
        date_joined=None,
        last_login=None,
    ):
        self.__id = id
        self.__username = username
        self.__password = password
        self.__is_active = is_active
        self.__date_joined = date_joined
        self.__last_login = last_login

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        self.__username = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        self.__password = value

    @property
    def is_active(self):
        return self.__is_active

    @is_active.setter
    def is_active(self, value):
        self.__is_active = value

    @property
    def date_joined(self):
        return self.__date_joined

    @date_joined.setter
    def date_joined(self, value):
        self.__date_joined = value

    @property
    def last_login(self):
        return self.__last_login

    @last_login.setter
    def last_login(self, value):
        self.__last_login = value

    def __str__(self) -> str:
        return f"{self.id}: {self.username}"
