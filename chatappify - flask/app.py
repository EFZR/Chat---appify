import os
from flask import Flask, send_from_directory
from flask_socketio import SocketIO
from flask_cors import CORS
from src.db.cmd.init_db import init_db_command
from src.db.cmd.fake_data import fake_data
from src.db.cmd.test_data import test_data
from src.views.errorHandler import error_handler
from src.views.user import user
from src.views.chatroom import chatroom
from src.views.participant import participant
from src.views.privateParticipant import pParticipant
from src.views.contactManagement import contactManagement
from src.namespace.ChatNamespace import ChatNamespace


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="dev",
        DATABASE=os.path.join(app.instance_path, "app.sqlite"),
        UPLOAD_FOLDER=os.path.join(app.instance_path, "uploads"),
        ALLOWED_EXTENSIONS=set(["png", "jpg", "jpeg", "gif"]),
        SESSION_COOKIE_SAMESITE="None",
    )

    if test_config is None:
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
        os.makedirs(app.config["UPLOAD_FOLDER"])
    except OSError:
        pass

    app.cli.add_command(init_db_command)
    app.cli.add_command(fake_data)
    app.cli.add_command(test_data)

    app.register_blueprint(error_handler)
    app.register_blueprint(user)
    app.register_blueprint(chatroom)
    app.register_blueprint(participant)
    app.register_blueprint(pParticipant)
    app.register_blueprint(contactManagement)

    @app.route("/helloworld")
    def hello_world():
        return "<p>Hello, World!</p>"

    return app


if __name__ == "__main__":
    allowed_origins = [
        "http://127.0.0.1:5500",
        "http://localhost:5173",
    ]
    app = create_app()
    CORS(app, origins=allowed_origins)
    socketio = SocketIO(app, cors_allowed_origins=allowed_origins)
    socketio.on_namespace(ChatNamespace("/chat"))
    socketio.run(app=app, port=5000, debug=True)
