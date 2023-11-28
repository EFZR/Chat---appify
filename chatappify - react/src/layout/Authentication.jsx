import { useContextApp } from "../components/AppContext";
import { useEffect } from "react";
import Registration from "../components/Registration";
import Login from "../components/Login";

const Authentication = () => {
  const { setIsLogged, register, setError, error, setUser } = useContextApp();

  useEffect(() => {
    const user = JSON.parse(localStorage.getItem("user"));
    if (user) {
      setIsLogged(true);
      setUser(user);
    }

    if (error) {
      setTimeout(() => setError(""), 3000);
    }
  }, []);

  return register ? <Registration /> : <Login />;
};

export default Authentication;
