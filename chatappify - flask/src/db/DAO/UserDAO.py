from werkzeug.exceptions import NotFound
from werkzeug.security import generate_password_hash, check_password_hash
from ..connection.Cursor import Cursor
from ..DTO.UserDTO import UserDTO
from datetime import datetime


class UserDAO:
    __SELECT_ALL = "SELECT * FROM user"
    __SELECT = "SELECT * FROM user WHERE id = ?"
    __INSERT = "INSERT INTO user (username, password) VALUES (?, ?)"
    __UPDATE = "UPDATE user SET username = ?, password = ? WHERE id = ?"
    __DELETE = "DELETE FROM user WHERE id = ?"
    __SELECT_BY_USERNAME = "SELECT * FROM user WHERE username = ?"
    __LAST_LOGIN = "UPDATE user SET last_login = ? WHERE id = ?"

    def save(self, user: UserDTO):
        user.password = generate_password_hash(user.password)
        values = (user.username, user.password)
        with Cursor() as cursor:
            cursor.execute(self.__INSERT, values)
            return cursor.lastrowid

    def delete(self, id: int):
        if self.find(id) is None:
            raise NotFound("User not found")
        with Cursor() as cursor:
            cursor.execute(self.__DELETE, (id,))
            return cursor.rowcount

    def update(self, user: UserDTO):
        values = (user.username, user.password, user.id)
        if self.find(user.id) is None:
            raise NotFound("User not found")
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

    def find_by_username(self, username: str):
        with Cursor() as cursor:
            cursor.execute(self.__SELECT_BY_USERNAME, (username,))
            return cursor.fetchone()

    def update_last_login(self, id: int):
        if self.find(id) is None:
            raise NotFound("User not found")
        values = (datetime.now(), id)
        with Cursor() as cursor:
            cursor.execute(self.__LAST_LOGIN, values)
            return cursor.rowcount
