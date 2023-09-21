import { NavLink } from "react-router-dom";
import "./navbar.css";

const NavBar = () => {
    return (
        <nav>
            <h1 id="title">Budgeteer</h1>
            <NavLink className="nav-link" to="/">Home</NavLink>
            <NavLink className="nav-link" to="/register">Sign Up</NavLink>
            <NavLink className="nav-link" to="/login">Log In</NavLink>
            <NavLink className="nav-link" to="/logout">Log out</NavLink>
            <NavLink className="nav-link" to="/budget">Budget</NavLink>
            <NavLink className="nav-link" to="/credit">Credit</NavLink>
            <NavLink className="nav-link" to="/savings">Savings</NavLink>
        </nav>
    );
}
export default NavBar;