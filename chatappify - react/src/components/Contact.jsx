import { useContextApp } from "./AppContext";
import { ws_join } from "../api/Chat";
import { IconContext } from "react-icons";
import { CiUser } from "react-icons/ci";
import "../styles/contact.css";

const Contact = ({ item, setActive }) => {
  const { setContact, user, socket } = useContextApp();

  const openChat = () => {
    setContact(item);
    ws_join(socket, user.username, item.key_room);
    setActive && setActive(false);
  };

  return (
    <div
      className="contact-menu"
      onClick={() => openChat()}
    >
      <div className="contact-info">
        <IconContext.Provider value={{ className: "icon" }}>
          <CiUser />
        </IconContext.Provider>
        <div>
          <span>{`${item.name}`}</span>
          <span className="state">Typing...</span>
        </div>
      </div>
      <div>
        <span>Today</span>
      </div>
    </div>
  );
};

export default Contact;
