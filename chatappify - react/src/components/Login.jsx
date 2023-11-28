import { useContextApp } from "./AppContext";
import { login } from "../api/User";
import { motion, AnimatePresence } from "framer-motion";
import "../styles/login.css";

const Login = () => {
  const { setIsLogged, setRegister, error, setError, setUser } =
    useContextApp();

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const user_form = new FormData(e.target);
      const { status, message, user } = await login(user_form);
      if (status === "ok") {
        setIsLogged(true);
        localStorage.setItem("user", JSON.stringify(user));
        setUser(user);
      } else {
        throw new Error(message);
      }
    } catch (e) {
      if (e instanceof Error) {
        setError(e.message);
        setTimeout(() => setError(""), 3000);
      } else {
        setError("An error has occurred");
        setTimeout(() => setError(""), 3000);
      }
    }
  };

  return (
    <main className="login-container">
      <AnimatePresence>
        {error && (
          <motion.div
            className="error-container"
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            transition={{ duration: 0.3 }}
          >
            <p className="error-text">{error}</p>
          </motion.div>
        )}
      </AnimatePresence>
      <div>
        <h1>Sign In</h1>
      </div>
      <div>
        <form className="input-container" onSubmit={handleSubmit}>
          <div className="input-field">
            <input
              type="text"
              name="username"
              placeholder="Username"
              className="login-input"
              id="username"
              autoComplete="off"
            />
            <label htmlFor="username" className="login-label">
              Username
            </label>
          </div>

          <div className="input-field">
            <input
              type="password"
              name="password"
              placeholder="Password"
              className="login-input"
              id="password"
              autoComplete="off"
            />
            <label htmlFor="password" className="login-label">
              Password
            </label>
          </div>

          <a href="#">Forgot Password ?</a>
          <input type="submit" value="Login" className="login-submit" />
          <a href="#" onClick={() => setRegister(true)}>
            Become a member
          </a>
        </form>
      </div>
    </main>
  );
};

export default Login;
