from flask import jsonify, request, Blueprint
from werkzeug.exceptions import BadRequest, NotFound
from src.db.DAO.ParticipantDAO import ParticipantDAO
from src.db.DTO.ParticipantDTO import ParticipantDTO
from src.db.DAO.UserDAO import UserDAO
from src.views.user import login_required

participantDAO = ParticipantDAO()
userDAO = UserDAO()

participant = Blueprint("participant", __name__, url_prefix="/api/participant")


@participant.route("/", methods=["GET"])
@login_required
def get_all():
    data = participantDAO.all()
    if len(data) == 0:
        raise NotFound("Participants not found")
    return jsonify({"participants": data, "status": "ok"}), 200


@participant.route("/<int:id>", methods=["GET"])
@login_required
def get(id):
    data = participantDAO.find(id)
    if data is None:
        raise NotFound("Participant not found")
    return jsonify({"participant": data, "status": "ok"}), 200


@participant.route("/", methods=["POST"])
@login_required
def save():
    state = request.form["state"]
    user_id = request.form["user_id"]
    chatroom_id = request.form["chatroom_id"]
    error = None

    if state is None:
        error = "State is required."
    if user_id is None:
        error = "User_id is required."
    if chatroom_id is None:
        error = "Chatroom_id is required."

    if error is None:
        participantDTO = ParticipantDTO(
            state=state, user_id=user_id, chatroom_id=chatroom_id
        )
        participantDAO.save(participantDTO)
        return (
            jsonify({"message": "Participant created successfully", "status": "ok"}),
            201,
        )

    raise BadRequest(error)


@participant.route("/<int:id>", methods=["PUT"])
@login_required
def update(id):
    state = request.form["state"]
    error = None

    if state is None:
        error = "State is required."

    if error is None:
        participantDTO = ParticipantDTO(state=state, id=id)
        participantDAO.update(ParticipantDTO)
        return (
            jsonify({"message": "Participant updated successfully", "status": "ok"}),
            200,
        )

    raise BadRequest(error)


@participant.route("/<int:id>", methods=["DELETE"])
@login_required
def delete(id):
    participantDAO.delete(id)
    return (
        jsonify({"message": "Participant deleted successfully", "status": "ok"}),
        200,
    )
