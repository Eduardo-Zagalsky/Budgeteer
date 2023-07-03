import { NavLink } from "react-router-dom";
import "./navbar.css";

const NavBar = () => {
    return (
        <nav>
            <h1 id="title">Shop Budget</h1>
            <NavLink className="nav-link" to="/">Home</NavLink>
            <NavLink className="nav-link" to="/register">Sign Up</NavLink>
            <NavLink className="nav-link" to="/login">Sign In</NavLink>
            <NavLink className="nav-link" to="/logout">Sign out</NavLink>
            <NavLink className="nav-link" to="/budget">Budget</NavLink>
            <NavLink className="nav-link" to="/shop">Shopping</NavLink>
        </nav>
    );
}
export default NavBar;