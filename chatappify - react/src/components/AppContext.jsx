import { useContext, createContext } from "react";

const initialState = {
  isLogged: false,
  setIsLogged: () => {},
  register: false,
  setRegister: () => {},
  socket: {},
  setSocket: () => {},
  user: {},
  setUser: () => {},
  error: "",
  setError: () => {},
  isLoading: true,
  setIsLoading: () => {},
  contact: {},
  setContact: () => {},
  contacts: [],
  setContacts: () => {},
  messages: [],
  setMessages: () => {},
  message: "",
  setMessage: () => {},
  search: "",
  setSearch: () => {},
  viewProfile: true,
  setViewProfile: () => {},
  viewClientProfile: false,
  setViewClientProfile: () => {},
};

export const AppContext = createContext(initialState);

export const useContextApp = () => {
  const context = useContext(AppContext);
  return context;
};
