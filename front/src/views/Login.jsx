import { Link } from "react-router-dom";
import useAppContext from "../context/AppContext";

export const Login = () => {
  const { actions, store } = useAppContext();

  return (
    <div className="container">
      <h1 className="text-center mt-4 display-4">Login</h1>
      <form
        onSubmit={actions.handleOnSubmitLogin}
        className="form-control row d-flex flex-columns gap-4 w-50 mx-auto mt-4 shadow"
      >
        <label className="mt-3" htmlFor="Nickname">
          Nickname
          <input
            className="form-control"
            type="text"
            name="nickname"
            placeholder="Username"
            id="Nickname"
            onChange={actions.handleUserInput}
          />
        </label>

        <label htmlFor="Password">
          Password
          <input
            className="form-control"
            type="password"
            name="password"
            placeholder="Password"
            id="Password"
            onChange={actions.handleUserInput}
          />
        </label>

        <button className="btn btn-primary" type="submit">
          Login
        </button>
        <Link to="/register" className="nav-link text-center mb-3">
          Register
        </Link>
      </form>
    </div>
  );
};
