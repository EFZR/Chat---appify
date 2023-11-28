import { io } from "socket.io-client";

export const ws_connect = (messages, setMessages) => {
  const socket = io(`${import.meta.env.VITE_CHATAPPIFY_URL}/chat`);

  socket.on("send_message", (data) => {
    add_message(messages, setMessages, data.message, "client");
  });

  socket.on("typing", (data) => {
    console.log(data);
  });

  return socket;
};

export const ws_sendMessage = (socket, username, room, message) => {
  socket.emit("send_message", { username, room, message });
};

export const ws_typing = (socket, username, room) => {
  socket.emit("typing", { username, room });
};

export const ws_leave = (socket, username, room) => {
  socket.emit("leave", { username, room });
};

export const ws_join = (socket, username, room) => {
  socket.emit("join", { username, room });
};

export const ws_close = (socket) => {
  socket.close();
};

