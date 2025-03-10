import React from "react";
import { Link, useNavigate } from "react-router-dom";
import "../styles/Profile.module.css"; // Ensure you create a Navbar.css for styles

const Navbar = () => {
    const navigate = useNavigate();
    const isAuthenticated = localStorage.getItem("token");

    const handleLogout = () => {
        localStorage.removeItem("token");
        navigate("/"); // Redirect to home after logout
    };

    return (
        <nav className="navbar">
            <div className="logo">
                <Link to="/">📘 LearnHub</Link>
            </div>
            <div className="nav-links">
                {isAuthenticated ? (
                    <>
                        <Link to="/profile" className="nav-btn">Profile</Link>
                        <button className="logout-btn" onClick={handleLogout}>Logout</button>
                    </>
                ) : (
                    <>
                        <Link to="/login" className="nav-btn">Login</Link>
                        <Link to="/signup" className="nav-btn">Signup</Link>
                    </>
                )}
            </div>
        </nav>
    );
};

export default Navbar;
