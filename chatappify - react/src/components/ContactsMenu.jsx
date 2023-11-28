import { useContextApp } from "./AppContext";
import { ws_close } from "../api/Chat";
import { IconContext } from "react-icons";
import { CiUser, CiLogout, CiChat2 } from "react-icons/ci";
import Contact from "../components/Contact";
import "../styles/menu.css";

const ContactsMenu = () => {
  const {
    contacts,
    setSearch,
    viewProfile,
    setViewProfile,
    setViewClientProfile,
    socket
  } = useContextApp();
  return (
    <aside className="chat-menu">
      <div className="user-profile-box">
        <div>
          <IconContext.Provider value={{ className: "icon" }}>
            <CiUser
              onClick={() => {
                setViewClientProfile(false);
                setViewProfile(!viewProfile);
              }}
            />
          </IconContext.Provider>
        </div>
        <div>
          <IconContext.Provider value={{ className: "icon" }}>
            <CiChat2 />
            <CiLogout
              onClick={() => {
                ws_close(socket);
                localStorage.removeItem("user");
                window.location.reload();
              }}
            />
          </IconContext.Provider>
        </div>
      </div>
      <div className="search-box" onChange={(e) => setSearch(e.target.value)}>
        <input type="text" placeholder="Search a contact" id="search-input" />
      </div>
      <div className="chats-box">
        {contacts ? (
          contacts.map((item) => <Contact key={item.key_room} item={item} />)
        ) : (
          <div className="no-contacts">
            <span>No contacts</span>
          </div>
        )}
      </div>
    </aside>
  );
};

export default ContactsMenu;
