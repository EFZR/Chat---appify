from werkzeug.exceptions import NotFound
from ..connection.Cursor import Cursor
from ..DTO.FileDTO import FileDTO


class FileDAO:
    __SELECT_ALL = "SELECT * FROM file"
    __SELECT_BY_ENTITY = "SELECT * FROM file WHERE entity_id = ? AND table_id = ?"
    __SELECT = "SELECT * FROM file WHERE id = ?"
    __INSERT = "INSERT INTO file (name, path, size, type, entity_id, table_id) VALUES (?, ?, ?, ?, ?, ?)"
    __UPDATE = "UPDATE file SET name = ?, path = ?, size = ?, type = ?, entity_id = ?, table_id = ? WHERE id = ?"
    __DELETE = "DELETE FROM file WHERE id = ?"

    def save(self, file: FileDTO):
        values = (
            file.name,
            file.path,
            file.size,
            file.type,
            file.entity_id,
            file.table_id,
        )
        with Cursor() as cursor:
            cursor.execute(self.__INSERT, values)
            return cursor.lastrowid

    def delete(self, id: int):
        if self.find(id) is None:
            raise NotFound("File not found")
        with Cursor() as cursor:
            cursor.execute(self.__DELETE, (id,))
            return cursor.rowcount

    def update(self, file: FileDTO):
        values = (
            file.name,
            file.path,
            file.size,
            file.type,
            file.entity_id,
            file.table_id,
            file.id,
        )
        if self.find(file.id) is None:
            raise NotFound("File not found")
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

    def find_by_entity(self, entity_id: int, table_id: str):
        values = (entity_id, table_id)
        with Cursor() as cursor:
            cursor.execute(self.__SELECT_BY_ENTITY, values)
            return cursor.fetchone()

    def find_by_entity_all(self, entity_id: int, table_id: str):
        values = (entity_id, table_id)
        with Cursor() as cursor:
            cursor.execute(self.__SELECT_BY_ENTITY, values)
            return cursor.fetchall()
