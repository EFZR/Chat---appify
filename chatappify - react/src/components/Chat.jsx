import { useRef, useEffect } from "react";
import { ws_sendMessage } from "../api/Chat";
import { useContextApp } from "./AppContext";
import { IconContext } from "react-icons";
import {
  CiUser,
  CiSettings,
  CiFaceSmile,
  CiCirclePlus,
  CiPaperplane,
  CiChat2,
} from "react-icons/ci";
import Message from "./Message";
import "../styles/Chat.css";

const Chat = () => {
  const chatBoxRef = useRef(null);

  const {
    contact,
    viewClientProfile,
    setViewClientProfile,
    setViewProfile,
    setMessage,
    message,
    messages,
    setMessages,
    user,
    socket,
  } = useContextApp();

  const handleMessageInput = () => {
    setMessages([
      ...messages,
      {
        message,
        receiver: "user",
        date: new Date().toLocaleTimeString(),
      },
    ]);
    ws_sendMessage(socket, user.username, contact.key_room, message);
    setMessage("");
  };

  useEffect(() => {
    chatBoxRef.current.scrollTop = chatBoxRef.current.scrollHeight;
  }, [contact]);

  return contact.key_room ? (
    <section className="chat">
      <div className="client-profile-box">
        <div className="contact-info">
          <IconContext.Provider value={{ className: "icon" }}>
            <CiUser
              onClick={() => {
                setViewClientProfile(!viewClientProfile);
                setViewProfile(true);
              }}
            />
          </IconContext.Provider>
          <div>
            <span>{contact.name}</span>
            <span className="state">Typing...</span>
          </div>
        </div>
        <div>
          <IconContext.Provider value={{ className: "icon" }}>
            <CiSettings />
          </IconContext.Provider>
        </div>
      </div>
      <div className="chat-box" ref={chatBoxRef}>
        {messages.length > 0 ? (
          messages.map((message, index) => (
            <Message
              key={index}
              message={message.message}
              receiver={message.receiver}
              date={message.date}
            />
          ))
        ) : (
          <div className="empty-chat">
            <h1>Start a conversation</h1>
            <p>Start a conversation with {contact.name} by typing a message</p>
          </div>
        )}
      </div>
      <div className="input-box">
        <IconContext.Provider value={{ className: "icon" }}>
          <CiFaceSmile />
          <CiCirclePlus />
        </IconContext.Provider>
        <input
          type="text"
          placeholder="Type a message..."
          id="chat-input"
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          onKeyDown={(e) => e.key === "Enter" && handleMessageInput()}
          autoComplete="off"
        />
        <IconContext.Provider value={{ className: "icon" }}>
          <CiPaperplane onClick={() => handleMessageInput()} />
        </IconContext.Provider>
      </div>
    </section>
  ) : (
    <section className="wait-section" ref={chatBoxRef}>
      <IconContext.Provider value={{ className: "start-icon" }}>
        <CiChat2 />
      </IconContext.Provider>
      <div>
        <h1 className="wait-message">Chat - Appify 🎈</h1>
      </div>
    </section>
  );
};

export default Chat;
