import ContactsMenu from "../components/ContactsMenu";
import Profile from "../components/Profile"
import ClientProfile from "../components/ClientProfile";

const Menu = () => {
  return (
    <>
      <ContactsMenu />
      <ClientProfile />
      <Profile />
    </>
  );
};

// css for this component is in src\styles\menu.css
export default Menu;
