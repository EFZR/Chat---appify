import { useContextApp } from "./AppContext";
import { IconContext } from "react-icons";
import { CiCircleChevLeft, CiUser } from "react-icons/ci";
import "../styles/profile.css";

const ClientProfile = () => {
  const { contact, viewClientProfile, setViewClientProfile } = useContextApp();
  return (
    <aside className={`profile ${viewClientProfile && "active"}`}>
      <div className="header">
        <IconContext.Provider value={{ className: "icon" }}>
          <CiCircleChevLeft
            onClick={() => setViewClientProfile(!viewClientProfile)}
          />
        </IconContext.Provider>
        <span>{contact.name}</span>
      </div>
      <div className="information">
        <div className={viewClientProfile === true ? "scale-up" : ""}>
          <IconContext.Provider value={{ className: "icon" }}>
            <CiUser />
          </IconContext.Provider>
        </div>
        <div className="data">
          <p className="info-label">Name</p>
          <p className="personal-info">{contact.name}</p>
        </div>
      </div>
    </aside>
  );
};

export default ClientProfile;
