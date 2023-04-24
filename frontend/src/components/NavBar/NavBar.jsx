import React from "react";
import { useContext } from "react";
import { useNavigate, Link } from "react-router-dom";
import AuthContext from "../../context/AuthContext";
import "./NavBar.css";

const Navbar = () => {
  const { logoutUser, user } = useContext(AuthContext);
  const navigate = useNavigate();
  return (
    <div className="navBar">
      <ul>
        <li className="brand">
          <Link to="/" style={{ textDecoration: "none", color: "white" }}>
            <b>PBIS App</b>
          </Link>
        </li>
        <li className="brand">
          <Link to="/teacher" style={{ textDecoration: "none", color: "white" }}>
            <b>TeacherPage</b>
          </Link>
        </li>
        <li className="brand">
          <Link to="/student" style={{ textDecoration: "none", color: "white" }}>
            <b>StudentPage</b>
          </Link>
        </li>
        <li className="brand">
          <Link to="/store" style={{ textDecoration: "none", color: "white" }}>
            <b>Store</b>
          </Link>
        </li>
        <li className="brand">
          <Link to="/cart" style={{ textDecoration: "none", color: "white" }}>
            <b>Shopping Cart</b>
          </Link>
        </li>
        <li className="brand">
          <Link to="/transactions" style={{ textDecoration: "none", color: "white" }}>
            <b>Transaction History</b>
          </Link>
        </li>
        <li>
          {user ? (
            <button onClick={logoutUser}>Logout</button>
          ) : (
            <button onClick={() => navigate("/login")}>Login</button>
          )}
        </li>
      </ul>
    </div>
  );
};

export default Navbar;
