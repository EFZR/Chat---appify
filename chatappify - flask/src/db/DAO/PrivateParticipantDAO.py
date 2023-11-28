from werkzeug.exceptions import NotFound
from ..connection.Cursor import Cursor
from ..DTO.PrivateParticipantDTO import PrivateParticipantDTO


class PrivateParticipantDAO:
    __SELECT_ALL = "SELECT * FROM private_participant"
    __SELECT = "SELECT * FROM private_participant WHERE id = ?"
    __INSERT = "INSERT INTO private_participant (state, user_id, user_id2, chatroom_id) VALUES (?, ?, ?, ?)"
    __UPDATE = "UPDATE private_participant SET state = ? WHERE id = ?"
    __DELETE = "DELETE FROM private_participant WHERE id = ?"
    __SELECT_CHATROOM_LIST = (
        "SELECT * FROM private_chatroom_list WHERE user_id = ? OR user_id2 = ?"
    )

    def save(self, private_participant: PrivateParticipantDTO):
        values = (
            private_participant.state,
            private_participant.user_id,
            private_participant.user_id2,
            private_participant.chatroom_id,
        )
        with Cursor() as cursor:
            cursor.execute(self.__INSERT, values)
            return cursor.lastrowid

    def delete(self, id: int):
        if self.find(id) is None:
            raise NotFound("Private Participant not found")
        with Cursor() as cursor:
            cursor.execute(self.__DELETE, (id,))
            return cursor.rowcount

    def update(self, private_participant: PrivateParticipantDTO):
        if self.find(private_participant.id) is None:
            raise NotFound("Private Participant not found")
        values = (private_participant.state, private_participant.id)
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
        values = (user_id, user_id)
        with Cursor() as cursor:
            cursor.execute(self.__SELECT_CHATROOM_LIST, values)
            return cursor.fetchall()
