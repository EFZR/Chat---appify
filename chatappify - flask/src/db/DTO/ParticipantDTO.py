class ParticipantDTO:
    def __init__(self, id=None, state=None, user_id=None, chatroom_id=None):
        self.__id = id
        self.__state = state
        self.__user_id = user_id
        self.__chatroom_id = chatroom_id

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, value):
        self.__state = value

    @property
    def user_id(self):
        return self.__user_id

    @user_id.setter
    def user_id(self, value):
        self.__user_id = value

    @property
    def chatroom_id(self):
        return self.__chatroom_id

    @chatroom_id.setter
    def chatroom_id(self, value):
        self.__chatroom_id = value

    def __str__(self):
        return f"Participant: {self.__id}"
