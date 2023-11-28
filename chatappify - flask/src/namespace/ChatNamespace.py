from flask_socketio import Namespace, emit, join_room, leave_room
from datetime import datetime


class ChatNamespace(Namespace):
    def on_connect(self):
        print("Client connected")

    def on_disconnect(self):
        print("Client disconnected")

    def on_join(self, data):
        username = data["username"]
        room = data["room"]
        join_room(room)
        print(f"{username} joined the room {room}")
        emit("join", {"username": username, "room": room}, room=room)

    def on_leave(self, data):
        username = data["username"]
        room = data["room"]
        leave_room(room)
        print(f"{username} left the room {room}")
        emit("leave", {"username": username, "room": room}, room=room)

    def on_send_message(self, data):
        username = data["username"]
        room = data["room"]
        message = data["message"]
        date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"{username} sent message to room {room}: {message}")
        emit(
            "send_message",
            {"username": username, "room": room, "message": message, "date": date},
            to=room,
            include_self=False,
            broadcast=True,
        )

    def on_typing(self, data):
        username = data["username"]
        room = data["room"]
        emit("typing", {"username": username, "room": room}, room=room)

    def on_error(self, data):
        print("Error: " + data["error"])
