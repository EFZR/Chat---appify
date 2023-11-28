import jwt, functools
from flask import Blueprint, request, jsonify, session, g, current_app
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.exceptions import BadRequest, NotFound, Unauthorized
from datetime import datetime, timedelta
from src.utils.TokenHelper import TokenHelper
from src.utils.FileHandler import FileHandler
from src.db.DAO.UserDAO import UserDAO
from src.db.DTO.UserDTO import UserDTO

user = Blueprint("user", __name__, url_prefix="/api/user")
userDAO = UserDAO()
fileHandler = FileHandler()


@user.route("/register", methods=["POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        error = None

        if not username:
            error = "Username is required."
        elif not password:
            error = "Password is required."
        elif userDAO.find_by_username(username) is not None:
            error = f"User {username} is already registered."

        if error is None:
            userDTO = UserDTO(username=username, password=password)
            newUserId = userDAO.save(userDTO)

            if request.files:
                file = request.files["file"]
                fileHandler.upload_file(file, newUserId, "user")

            return (
                jsonify({"message": "User created successfully", "status": "ok"}),
                201,
            )

        raise BadRequest(error)


@user.route("/login", methods=["POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user_data = userDAO.find_by_username(username)
        error = None

        if user_data is None:
            error = "Incorrect Username."
        elif not check_password_hash(user_data["password"], password):
            error = "Incorrect Password."

        if error is None:
            session.clear()
            token_payload = {
                "id": user_data["id"],
                "username": user_data["username"],
                "exp": datetime.utcnow() + timedelta(hours=1),
            }
            token = jwt.encode(
                token_payload, current_app.config["SECRET_KEY"], algorithm="HS256"
            )
            session["user_id"] = user_data["id"]
            userDAO.update_last_login(user_data["id"])
            user_data["token"] = token
            return (
                jsonify(
                    {"message": "Login successfully", "user": user_data, "status": "ok"}
                ),
                200,
            )

        raise BadRequest(error)


@user.route("/logout")
def logout():
    session.clear()
    return jsonify({"message": "Logout successfully"}), 200


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        TokenHelper.verify_token(request)
        return view(**kwargs)

    return wrapped_view


@user.route("/", methods=["GET"])
@login_required
def get_users():
    users = userDAO.all()
    if len(users) == 0:
        raise NotFound("Users not found")
    return jsonify({"users": users, "status": "ok"}), 200


@user.route("/<int:id>", methods=["GET"])
@login_required
def get_user(id):
    user = userDAO.find(id)
    if user is None:
        raise NotFound("User not found")
    if request.args.get("file") == "true":
        user["file"] = fileHandler.get_file(id, "user")
    return jsonify({"user": user, "status": "ok"}), 200


@user.route("/<int:id>", methods=["PUT"])
@login_required
def update_user(id):
    username = request.form["username"]
    password = request.form["password"]
    error = None

    if not username:
        error = "Username is required."
    elif not password:
        error = "Password is required."

    if error is None:
        password = generate_password_hash(password)
        userDTO = UserDTO(id=id, username=username, password=password)
        userDAO.update(userDTO)
        if request.files:
            file = request.files["file"]
            fileHandler.modify_file(file, id, "user")
        return jsonify({"message": "User updated successfully", "status": "ok"}), 200

    raise BadRequest(error)


@user.route("/<int:id>", methods=["DELETE"])
@login_required
def delete_user(id):
    userDAO.delete(id)
    fileHandler.delete_file(id, "user")
    return (
        jsonify({"message": "User deleted successfully", "status": "ok"}),
        200,
    )
