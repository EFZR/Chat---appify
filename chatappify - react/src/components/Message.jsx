import "../styles/message.css";

const Message = ({ message, receiver, date }) => {
  return (
    <div
      className={`message ${
        receiver == "user" ? "user-message" : "client-message"
      }`}
    >
      <p className="content-message">{message}</p>
      <p className="date-message">{date}</p>
    </div>
  );
};

export default Message;
