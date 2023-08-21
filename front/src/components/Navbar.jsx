import "./Navbar.css";
import logo from "../../public/Star-Wars-Logo.png";
import useAppContext from "../context/AppContext";
import { Link } from "react-router-dom";
export const Navbar = () => {
  return (
    <header className="container-fluid bg-body-secondary">
      <div className="row-12 d-flex justify-content-between p-3 align-items-center">
        <Link to="/" className="col-auto">
          <img className="logo" src={logo} alt="logo_star_wars" />
        </Link>
        <nav className="d-flex gap-2 align-items-center">
          <Link className="btn btn-primary" to="/login">
            Login
          </Link>
          <Link
            to="/private"
            className="btn btn-outline-primary fs-5 rounded-circle"
          >
            <i class="bi bi-person"></i>
          </Link>
        </nav>
      </div>
    </header>
  );
};
