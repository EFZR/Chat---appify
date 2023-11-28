import os
import click
from flask import current_app
from src.db.connection.Cursor import Cursor
from src.db.DAO.UserDAO import UserDAO
from src.db.DTO.UserDTO import UserDTO


@click.command("init-db")
def init_db_command():
    """Clear the existing data and create new tables."""
    with Cursor() as cursor:
        with open(os.path.join(current_app.instance_path, "./scripts/init_db.sql")) as f:
            cursor.executescript(f.read())
    user = UserDTO(username="admin", password="admin")
    userDAO = UserDAO()
    userDAO.save(user)
    click.echo("Initialized the database.")
