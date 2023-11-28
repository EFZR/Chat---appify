from werkzeug.exceptions import NotFound
from ..connection.Cursor import Cursor
from ..DTO.ParticipantDTO import ParticipantDTO


class ParticipantDAO:
    __SELECT_ALL = "SELECT * FROM participant"
    __SELECT = "SELECT * FROM participant WHERE id = ?"
    __INSERT = "INSERT INTO participant (state, user_id, chatroom_id) VALUES (?, ?, ?)"
    __UPDATE = "UPDATE participant SET state = ? WHERE id = ?"
    __DELETE = "DELETE FROM participant WHERE id = ?"
    __SELECT_CHATROOM_LIST = "SELECT * FROM chatroom_list WHERE user_id = ?"

    def save(self, participant: ParticipantDTO):
        values = (participant.state, participant.user_id, participant.chatroom_id)
        with Cursor() as cursor:
            cursor.execute(self.__INSERT, values)
            return cursor.lastrowid

    def delete(self, id: int):
        if self.find(id) is None:
            raise NotFound("Participant not found")
        with Cursor() as cursor:
            cursor.execute(self.__DELETE, (id,))
            return cursor.rowcount

    def update(self, participant: ParticipantDTO):
        values = (participant.state, participant.id)
        if self.find(participant.id) is None:
            raise NotFound("Participant not found")
        with Cursor() as cursor:
            cursor.execute(self.__UPDATE, values)
            return cursor.rowcount

    def find(self, id: int):
        with Cursor() as cursor:
            cursor.execute(self.__SELECT, (id,))
            return cursor.fetchone()

    def all(self):
        with Cursor() as cursor:
            cursor.execute(self.__SELECT_ALL)
            return cursor.fetchall()

    def get_chatroom_list(self, user_id: int):
        with Cursor() as cursor:
            cursor.execute(self.__SELECT_CHATROOM_LIST, (user_id,))
            return cursor.fetchall()
