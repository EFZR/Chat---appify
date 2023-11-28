from flask import jsonify, request, Blueprint
from werkzeug.exceptions import BadRequest, NotFound
from datetime import datetime
from src.utils.FileHandler import FileHandler
from src.utils.TokenHelper import TokenHelper
from src.db.DAO.ChatroomDAO import ChatroomDAO
from src.db.DTO.ChatroomDTO import ChatroomDTO
from src.views.user import login_required

chatroomDAO = ChatroomDAO()
fileHandler = FileHandler()

chatroom = Blueprint("chatroom", __name__, url_prefix="/api/chatroom")


@chatroom.route("/", methods=["GET"])
@login_required
def get_all():
    data = chatroomDAO.all()
    if len(data) == 0:
        raise NotFound("Chatrooms not found")
    if request.args.get("file") == "true":
        data = fileHandler.get_files(data, "chatroom")
    return jsonify({"chatrooms": data, "status": "ok"}), 200


@chatroom.route("/<int:id>", methods=["GET"])
@login_required
def get(id):
    data = chatroomDAO.find(id)
    if data is None:
        raise NotFound("Chatroom not found")
    if request.args.get("file") == "true":
        file = fileHandler.get_file(id, "chatroom")
        data["file"] = file
    return jsonify({"chatroom": data, "status": "ok"}), 200


@chatroom.route("/", methods=["POST"])
@login_required
def save():
    name = request.form["name"]
    key_room = TokenHelper.generate_secret_key()
    error = None

    if not name:
        error = "Name is required."

    if error is None:
        chatroomDTO = ChatroomDTO(name=name, key_room=key_room)
        newChatroomId = chatroomDAO.save(chatroomDTO)

        if request.files:
            file = request.files["file"]
            fileHandler.upload_file(file, newChatroomId, "chatroom")

        return (
            jsonify({"message": "Chatroom created successfully", "status": "ok"}),
            201,
        )

    raise BadRequest(error)


@chatroom.route("/<int:id>", methods=["PUT"])
@login_required
def update(id):
    lastMessage = request.form["last_message"]
    error = None

    if not lastMessage:
        error = "Last message is required."
    elif datetime.strptime(lastMessage, "%Y-%m-%d %H:%M:%S") > datetime.utcnow():
        error = "Last message date is not valid."

    if error is None:
        chatroomDTO = ChatroomDTO(last_message=lastMessage, id=id)
        chatroomDAO.update(chatroomDTO)
        return (
            jsonify({"message": "Chatroom updated successfully", "status": "ok"}),
            200,
        )

    raise BadRequest(error)


@chatroom.route("/<int:id>/img", methods=["PUT"])
@login_required
def update_img(id):
    if request.files:
        file = request.files["file"]
        fileHandler.modify_file(file, id, "chatroom")
        return (
            jsonify({"message": "Chatroom updated successfully", "status": "ok"}),
            200,
        )
    raise BadRequest("No file selected")


@chatroom.route("/<int:id>", methods=["DELETE"])
@login_required
def delete(id):
    chatroomDAO.delete(id)
    fileHandler.delete_file(id, "chatroom")
    return (
        jsonify({"message": "Chatroom deleted successfully", "status": "ok"}),
        200,
    )
