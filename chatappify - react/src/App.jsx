import { useState } from "react";
import { AppContext } from "./components/AppContext";
import Authentication from "./layout/Authentication";
import Principal from "./layout/Principal";

const App = () => {
  //#region states
  const [isLogged, setIsLogged] = useState(false);
  const [register, setRegister] = useState(false);
  const [socket, setSocket] = useState({});
  const [user, setUser] = useState({});
  const [error, setError] = useState("");
  const [isLoading, setIsLoading] = useState(true);
  const [contact, setContact] = useState({});
  const [contacts, setContacts] = useState([]);
  const [messages, setMessages] = useState([]);
  const [message, setMessage] = useState("");
  const [search, setSearch] = useState("");
  const [viewProfile, setViewProfile] = useState(true);
  const [viewClientProfile, setViewClientProfile] = useState(false);
  //#endregion

  const contextValues = {
    isLogged,
    setIsLogged,
    register,
    setRegister,
    socket,
    setSocket,
    user,
    setUser,
    error,
    setError,
    isLoading,
    setIsLoading,
    contact,
    setContact,
    contacts,
    setContacts,
    messages,
    setMessages,
    message,
    setMessage,
    search,
    setSearch,
    viewProfile,
    setViewProfile,
    viewClientProfile,
    setViewClientProfile,
  };

  return (
    <AppContext.Provider value={contextValues}>
      <main className="container">
        {isLogged ? <Principal /> : <Authentication />}
      </main>
    </AppContext.Provider>
  );
};

export default App;
