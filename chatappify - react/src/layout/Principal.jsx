import { useEffect, useRef } from "react";
import { io } from "socket.io-client";
import { useContextApp } from "../components/AppContext";
import { getContacts } from "../api/Contacts";
import Menu from "../components/Menu";
import Chat from "../components/Chat";
import PhoneMenu from "../components/PhoneMenu";
import Loader from "../components/Loader";

const Principal = () => {
  const {
    setIsLogged,
    setContacts,
    search,
    setError,
    isLoading,
    setIsLoading,
    setSocket,
    messages,
    setMessages,
  } = useContextApp();

  const ws_connection = () => {
    const socket = io(`${import.meta.env.VITE_CHATAPPIFY_URL}/chat`);

    socket.on("send_message", async (data) => {
      setMessages([
        ...messages,
        {
          message: data.message,
          receiver: "client",
          date: new Date().toLocaleTimeString(),
        },
      ]);
    });

    socket.on("typing", (data) => {
      console.log(data);
    });

    setSocket(socket);
  };

  const fetchContacts = async () => {
    try {
      const user = await JSON.parse(localStorage.getItem("user"));
      const { contacts, status, message } = await getContacts(user.token);
      if (status === "error") {
        throw new Error(message);
      }
      setContacts(contacts);
    } catch (error) {
      localStorage.removeItem("user");
      setIsLogged(false);
      setError(error.message);
    } finally {
      setTimeout(() => setIsLoading(false), 1000);
      ws_connection();
    }
  };

  useEffect(() => {
    fetchContacts();
  }, []);

  useEffect(() => {
    console.log(messages);
  }, [messages]);

  useEffect(() => {}, [search]);

  return isLoading ? (
    <Loader />
  ) : (
    <>
      <div className="chat-container">
        <Menu />
        <Chat />
        <PhoneMenu />
      </div>
    </>
  );
};

export default Principal;
