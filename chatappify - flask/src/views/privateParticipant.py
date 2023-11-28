from flask import jsonify, request, Blueprint
from werkzeug.exceptions import BadRequest, NotFound
from src.db.DAO.PrivateParticipantDAO import PrivateParticipantDAO
from src.db.DTO.PrivateParticipantDTO import PrivateParticipantDTO
from src.db.DAO.UserDAO import UserDAO
from src.views.user import login_required

pParticipantDAO = PrivateParticipantDAO()
userDAO = UserDAO()

pParticipant = Blueprint(
    "private_participant", __name__, url_prefix="/api/private_participant"
)


@pParticipant.route("/", methods=["GET"])
@login_required
def get_all():
    data = pParticipantDAO.all()
    if len(data) == 0:
        raise NotFound("Participants not found")
    return jsonify({"private_participants": data, "status": "ok"}), 200


@pParticipant.route("/<int:id>", methods=["GET"])
@login_required
def get(id):
    data = pParticipantDAO.find(id)
    print(data)
    if data is None:
        raise NotFound("Participant not found")
    return jsonify({"private_participants": data, "status": "ok"}), 200


@pParticipant.route("/", methods=["POST"])
@login_required
def save():
    state = request.form["state"]
    user_id = request.form["user_id"]
    user_id2 = request.form["user_id2"]
    chatroom_id = request.form["chatroom_id"]
    error = None

    if state is None:
        error = "State is required."
    if user_id is None:
        error = "User_id is required."
    if user_id2 is None:
        error = "User_id2 is required."
    if chatroom_id is None:
        error = "Chatroom_id is required."

    if error is None:
        pParticipantDTO = PrivateParticipantDTO(
            state=state, user_id=user_id, user_id2=user_id2, chatroom_id=chatroom_id
        )
        pParticipantDAO.save(pParticipantDTO)
        return (
            jsonify({"message": "Participant created successfully", "status": "ok"}),
            201,
        )

    raise BadRequest(error)


@pParticipant.route("/<int:id>", methods=["PUT"])
@login_required
def update(id):
    state = request.form["state"]
    error = None

    if state is None:
        error = "State is required."

    if error is None:
        pParticipantDTO = PrivateParticipantDTO(id=id, state=state)
        pParticipantDAO.update(pParticipantDTO)
        return (
            jsonify({"message": "Participant updated successfully", "status": "ok"}),
            200,
        )

    raise BadRequest(error)


@pParticipant.route("/<int:id>", methods=["DELETE"])
@login_required
def delete(id):
    pParticipantDAO.delete(id)
    return (
        jsonify({"message": "Participant deleted successfully", "status": "ok"}),
        201,
    )

