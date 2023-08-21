import { Link } from "react-router-dom";
import useAppContext from "../context/AppContext";

export const Register = () => {
  const { actions, store } = useAppContext();

  return (
    <div className="container">
      <h1 className="text-center mt-4 display-4">Register</h1>
      <form
        onSubmit={actions.handleOnSubmitRegister}
        className="form-control row d-flex flex-columns gap-4 w-50 mx-auto mt-4 shadow"
      >
        <label className="mt-3" htmlFor="Nickname">
          Username
          <input
            onChange={actions.handleUserInput}
            className="form-control"
            type="text"
            name="nickname"
          />
        </label>

        <label>
          Email
          <input
            onChange={actions.handleUserInput}
            className="form-control"
            type="email"
            name="email"
          />
        </label>

        <label>
          Password
          <input
            onChange={actions.handleUserInput}
            className="form-control"
            type="password"
            name="password"
          />
        </label>

        <button className="btn btn-primary" type="submit">
          Register
        </button>
        <Link to="/login" className="nav-link text-center mb-3">
          Login
        </Link>
      </form>
    </div>
  );
};
