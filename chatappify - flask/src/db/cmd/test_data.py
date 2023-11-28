import click
from faker import Faker
from src.db.DAO.UserDAO import UserDAO
from src.db.DTO.UserDTO import UserDTO
from src.db.DAO.ChatroomDAO import ChatroomDAO
from src.db.DTO.ChatroomDTO import ChatroomDTO
from src.db.DAO.ParticipantDAO import ParticipantDAO
from src.db.DTO.ParticipantDTO import ParticipantDTO
from src.db.DAO.PrivateParticipantDAO import PrivateParticipantDAO
from src.db.DTO.PrivateParticipantDTO import PrivateParticipantDTO

userDAO = UserDAO()
chatroomDAO = ChatroomDAO()
participantDAO = ParticipantDAO()
privateParticipantDAO = PrivateParticipantDAO()
fake = Faker()


@click.command("test-data")
def test_data():
    """Creates a user for testing with username and password: admin"""
    try:
        test_user = userDAO.find_by_username("admin")
        users = userDAO.all()
        if len(users) < 2:
            click.echo("Please run fake-data first.")
            return
        for user in users:
            if user["id"] != test_user["id"]:
                chatroomDTO = ChatroomDTO(
                    name=f"{test_user['username']} - {user['username']}",
                    key_room=fake.pystr(10, 10),
                )
                chatroom_id = chatroomDAO.save(chatroomDTO)
                privateParticipantDTO = PrivateParticipantDTO(
                    state="pending",
                    user_id=test_user["id"],
                    user_id2=user["id"],
                    chatroom_id=chatroom_id,
                )
                privateParticipantDAO.save(privateParticipantDTO)
        click.echo("Generated test data.")

    except:
        click.echo("Please run init-db first.")
