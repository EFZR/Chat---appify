import os, string, random
from flask import Flask
from werkzeug.exceptions import NotFound, BadRequest
from src.db.DAO.FileDAO import FileDAO
from src.db.DTO.FileDTO import FileDTO


class FileHandler:
    def __init__(self):
        self.__APP = Flask(__name__)
        self.__UPLOAD_FOLDER = os.path.join(self.__APP.instance_path, "uploads")
        self.__ALLOWED_EXTENSIONS = set(["png", "jpg", "jpeg", "gif"])
        self.__fileDAO = FileDAO()

    def is_allowed_file(self, filename: str):
        """Checks the file extension

        Args:
            filename (str): name of the file

        Raises:
            BadRequest: when the file extension is not allowed

        Returns:
            True: when the file extension is allowed
        """
        if (
            "." in filename
            and filename.rsplit(".", 1)[1].lower() in self.__ALLOWED_EXTENSIONS
        ):
            return True
        raise BadRequest("File extension not allowed")

    def generate_random_filename(self, filename: str, length=10):
        """Creates a random string and adds it to the filename

        Args:
            filename (str): name of the File
            length (int, optional): Size of the new filename. Defaults to 10.

        Returns:
            str: new name of the file with a random string and the respective extension
        """
        letters = string.ascii_lowercase
        if self.is_allowed_file(filename):
            extension = filename.rsplit(".", 1)[1].lower()
            return (
                "".join(random.choice(letters) for i in range(length)) + "." + extension
            )

    def upload_file(self, file, entity_id: int, table_id: str):
        """Saves a file in the uploads folder and its information in the database

        Args:
            file (file): file get in the request of the endpoint
            entity_id (int): id of the element which the file belongs to
            table_id (str): id of the table which the file belongs to

        Raises:
            BadRequest: if no file is selected
            Exception: if there is an error uploading the file
        """
        if file.filename == "":
            raise BadRequest("No file selected")
        try:
            filename = self.generate_random_filename(file.filename)
            file.save(os.path.join(self.__UPLOAD_FOLDER, filename))
            path = f"/uploads/{filename}"
            size = os.path.getsize(os.path.join(self.__UPLOAD_FOLDER, filename))
            type = filename.rsplit(".", 1)[1].lower()
            fileDTO = FileDTO(
                name=filename,
                path=path,
                size=size,
                type=type,
                entity_id=entity_id,
                table_id=table_id,
            )
            self.__fileDAO.save(fileDTO)
        except Exception as e:
            self.__APP.logger.error(f"Error uploading file: {e}")
            raise Exception(f"Error uploading file: {e}")

    def delete_file(self, entity_id: int, table_id: str):
        """Deletes a file in the uploads folder and its information in the database

        Args:
            entity_id (int): id of the element which the file belongs to
            table_id (str): id of the table which the file belongs to

        Raises:
            NotFound: if the file is not found or does not exist
            Exception: if there is an error deleting the file
        """
        try:
            file = self.__fileDAO.find_by_entity(entity_id=entity_id, table_id=table_id)
            if file is None:
                return
            os.remove(os.path.join(self.__UPLOAD_FOLDER, file["name"]))
            self.__fileDAO.delete(file["id"])
        except Exception as e:
            self.__APP.logger.error(f"Error deleting file: {e}")
            raise Exception(f"Error deleting file: {e}")

    def modify_file(self, file, entity_id: int, table_id: str):
        """Modifies a file in the database and uploads folder

        Args:
            file (file): file get in the request of the endpoint
            entity_id (int): id of the element which the file belongs to
            table_id (_type_): id of the table which the file belongs to

        Raises:
            Exception: if there is an error modifying the file
        """
        try:
            self.delete_file(entity_id, table_id)
            self.upload_file(file, entity_id, table_id)
        except Exception as e:
            self.__APP.logger.error(f"Error modifying file: {e}")
            raise Exception(f"Error modifying file: {e}")

    def get_file(self, entity_id: int, table_id: str):
        """Searches for information of a file in the database

        Args:
            entity_id (int): id of the element which the file belongs to
            table_id (str): id of the table which the file belongs to

        Returns:
            dict: The file data
        """
        file_data = self.__fileDAO.find_by_entity(
            entity_id=entity_id, table_id=table_id
        )
        return file_data

    def get_files(self, data: list, table_id: str):
        """Searches for information of files in the database

        Args:
            data (list): list of elements with vital information for the file search
            table_id (int): id of the table which the file belongs to

        Returns:
            list: Data list with the file information
        """
        for element in data:
            file_data = self.__fileDAO.find_by_entity(
                entity_id=element["id"], table_id=table_id
            )
            element["file"] = file_data
        return data

    def get_contacts_file(self, contacts: list, user_id: int):
        """Searches for information of contact files in the database

        Args:
            contacts (list): list of contacts with vital information for the file search
            user_id (int): id of the user, used to search for the file

        Returns:
            list: Contacts list with the file information
        """
        for contact in contacts:
            if contact["type"] == "private":
                if contact["user_id"] != user_id:
                    file_data = self.__fileDAO.find_by_entity(
                        entity_id=contact["user_id"], table_id=contact["metadata_table"]
                    )
                    contact["file"] = file_data
                else:
                    file_data = self.__fileDAO.find_by_entity(
                        entity_id=contact["user_id2"],
                        table_id=contact["metadata_table"],
                    )
                    contact["file"] = file_data
            else:
                file_data = self.__fileDAO.find_by_entity(
                    entity_id=contact["chatroom_id"], table_id=contact["metadata_table"]
                )
                contact["file"] = file_data
        return contacts
