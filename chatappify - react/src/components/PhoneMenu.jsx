import { useState } from "react";
import { ws_close } from "../api/Chat";
import { useContextApp } from "../components/AppContext";
import { IconContext } from "react-icons";
import { CiUser, CiLogout, CiChat2, CiCircleChevLeft } from "react-icons/ci";
import Contact from "../components/Contact";
import "../styles/menu.css";

const PhoneMenu = () => {
  const {
    contacts,
    viewProfile,
    setViewProfile,
    setViewClientProfile,
    setSearch,
    socket
  } = useContextApp();
  const [active, setActive] = useState(false);

  return (
    <>
      <a
        className="btn-menu"
        onClick={(e) => {
          e.preventDefault();
          setActive(!active);
        }}
      >
        &#10140;
      </a>
      <aside className={`chat-phone-menu ${active && "active"}`}>
        <div className="user-profile-box">
          <div>
            <IconContext.Provider value={{ className: "icon" }}>
              <CiUser
                onClick={() => {
                  setViewProfile(!viewProfile);
                  setActive(!active);
                  setViewClientProfile(false);
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
              <IconContext.Provider value={{ className: "icon close-icon" }}>
                <CiCircleChevLeft onClick={() => setActive(!active)} />
              </IconContext.Provider>
            </IconContext.Provider>
          </div>
        </div>
        <div className="search-box" onChange={(e) => setSearch(e.target.value)}>
          <input
            type="text"
            placeholder="Search a contact"
            id="search-input-phone"
          />
        </div>
        <div className="chats-box">
          {contacts ? (
            contacts.map((item) => (
              <Contact key={item.key_room} item={item} setActive={setActive} />
            ))
          ) : (
            <div className="no-contacts">
              <span>No contacts</span>
            </div>
          )}
        </div>
      </aside>
    </>
  );
};

export default PhoneMenu;
