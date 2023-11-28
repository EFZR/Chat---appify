import random
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


@click.command("fake-data")
def fake_data(length=10):
    """Gernerate Dummy Data

    Args:
        length (int, optional): Scale of data. Defaults to 10.
    """
    try:
        for i in range(length):
            chatroomDTO = ChatroomDTO(name=fake.text(10), key_room=fake.pystr(10, 10))
            chatroomDAO.save(chatroomDTO)
            for i in range(random.randint(1, 10)):
                userDTO = UserDTO(username=fake.name(), password=fake.password())
                userDAO.save(userDTO)

        total_users = len(userDAO.all())
        total_chatrooms = len(chatroomDAO.all())

        for i in range(total_chatrooms):
            semafore = random.choice([True, False])
            state = "pending"
            if semafore:
                user_id = random.randint(1, total_users)
                user_id2 = random.randint(1, total_users)
                while user_id == user_id2:
                    user_id2 = random.randint(1, total_users)

                privateParticipantDTO = PrivateParticipantDTO(
                    state=state, user_id=user_id, user_id2=user_id2, chatroom_id=i + 1
                )
                privateParticipantDAO.save(privateParticipantDTO)

            else:
                users = userDAO.all()
                for user in users:
                    particiapantDTO = ParticipantDTO(
                        state=state, user_id=user["id"], chatroom_id=i + 1
                    )
                    participantDAO.save(particiapantDTO)
        click.echo("Generated fake data.")

    except:
        click.echo("Please run init-db first.")
