from flask import Blueprint, jsonify, request
from werkzeug.exceptions import NotFound
from src.views.user import login_required
from src.utils.TokenHelper import TokenHelper
from src.utils.FileHandler import FileHandler
from src.db.DAO.UserDAO import UserDAO
from src.db.DAO.FileDAO import FileDAO
from src.db.DAO.ParticipantDAO import ParticipantDAO
from src.db.DAO.PrivateParticipantDAO import PrivateParticipantDAO

fileDAO = FileDAO()
userDAO = UserDAO()
fileHandler = FileHandler()
participantDAO = ParticipantDAO()
privateParticipantDAO = PrivateParticipantDAO()


contactManagement = Blueprint(
    "contactManagement", __name__, url_prefix="/api/contactManagement"
)


@contactManagement.route("/contacts", methods=["GET"])
@login_required
def contacts():
    tokenPayload = TokenHelper.verify_token(request)
    user_id = tokenPayload["id"]
    if userDAO.find(user_id) is None:
        raise NotFound("User not found")
    participants = participantDAO.get_chatroom_list(user_id)
    privateParticipants = privateParticipantDAO.get_chatroom_list(user_id)
    contacts = []
    contacts += [participant for participant in participants]
    contacts += [privateParticipant for privateParticipant in privateParticipants]
    contacts = fileHandler.get_contacts_file(contacts, user_id)
    response = jsonify({"contacts": contacts, "status": "ok"})
    return response, 200
