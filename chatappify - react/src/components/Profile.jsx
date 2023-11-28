import { useContextApp } from "./AppContext";
import { IconContext } from "react-icons";
import { CiCircleChevLeft, CiUser } from "react-icons/ci";
import "../styles/profile.css";

const Profile = () => {
  const { viewProfile, setViewProfile, user } = useContextApp();
  return (
    <aside className={`profile ${viewProfile || "active"}`}>
      <div className="header">
        <IconContext.Provider value={{ className: "icon" }}>
          <CiCircleChevLeft onClick={() => setViewProfile(!viewProfile)} />
        </IconContext.Provider>
        <span>Profile</span>
      </div>
      <div className="information">
        <div className={viewProfile === false ? "scale-up" : ""}>
          <IconContext.Provider value={{ className: "icon" }}>
            <CiUser />
          </IconContext.Provider>
        </div>
        <div className="data">
          <p className="info-label">Your Name</p>
          <p className="personal-info">{user.username}</p>
        </div>
      </div>
    </aside>
  );
};

export default Profile;
