from werkzeug.exceptions import NotFound
from ..connection.Cursor import Cursor
from ..DTO.ChatroomDTO import ChatroomDTO


class ChatroomDAO:
    __SELECT_ALL = "SELECT * FROM chatroom"
    __SELECT = "SELECT * FROM chatroom WHERE id = ?"
    __INSERT = "INSERT INTO chatroom (name, key_room) VALUES (?, ?)"
    __UPDATE = "UPDATE chatroom SET last_message = ? WHERE id = ?"
    __DELETE = (
        "DELETE FROM message WHERE chatroom_id = ?;"
        "DELETE FROM participant WHERE chatroom_id = ?;"
        "DELETE FROM private_participant WHERE chatroom_id = ?;"
        "DELETE FROM chatroom WHERE id = ?;"
    )

    def save(self, chatroom: ChatroomDTO):
        values = (chatroom.name, chatroom.key_room)
        with Cursor() as cursor:
            cursor.execute(self.__INSERT, values)
            return cursor.lastrowid

    def delete(self, id: int):
        if self.find(id) is None:
            raise NotFound("Chatroom not found")
        with Cursor() as cursor:
            script = self.__DELETE.replace("?", str(id))
            cursor.executescript(script)
            return cursor.rowcount

    def update(self, chatroom: ChatroomDTO):
        values = (chatroom.last_message, chatroom.id)
        if self.find(chatroom.id) is None:
            raise NotFound("Chatroom not found")
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
