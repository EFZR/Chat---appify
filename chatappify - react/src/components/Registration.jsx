import { useContextApp } from "./AppContext";
import { register, login } from "../api/User";
import { motion, AnimatePresence } from "framer-motion";
import "../styles/login.css";

const Registration = () => {
  const { setIsLogged, setRegister, error, setError } = useContextApp();

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const user_form = new FormData(e.target);
      if (user_form.get("password") === user_form.get("repeat_password")) {
        const { status: registerStatus, message: registerMessage } =
          await register(user_form);
        if (registerStatus === "ok") {
          const {
            status: loginStatus,
            message: loginMessage,
            user,
          } = await login(user_form);
          if (loginStatus === "ok") {
            setIsLogged(true);
            localStorage.setItem("user", user);
          } else {
            throw new Error(loginMessage);
          }
        } else {
          throw new Error(registerMessage);
        }
      } else {
        throw new Error("Passwords do not match");
      }
    } catch (e) {
      setError(e.message);
    } finally {
      setTimeout(() => setError(""), 3000);
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
        <h1>Sign Up</h1>
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

          <div className="input-field">
            <input
              type="password"
              name="repeat_password"
              placeholder="Repeat Password"
              className="login-input"
              id="repeat_password"
              autoComplete="off"
            />
            <label htmlFor="repeat_password" className="login-label">
              Repeat Password
            </label>
          </div>

          <input type="submit" value="Register" className="login-submit" />
          <a href="#" onClick={() => setRegister(false)}>
            Back to Login
          </a>
        </form>
      </div>
    </main>
  );
};

export default Registration;
