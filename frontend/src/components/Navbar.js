import React from "react";
import { Link, useNavigate, useLocation } from "react-router-dom";
import "../styles/Profile.module.css";

const Navbar = ({ setIsAuthenticated }) => {
    const navigate = useNavigate();
    const location = useLocation();
    const isAuthenticated = Boolean(localStorage.getItem("token"));

    const handleLogout = () => {
        // Clear local storage
        localStorage.removeItem("token");
        localStorage.removeItem("user_id");
        localStorage.removeItem("user_type");

        // Ensure the redirection happens to home
        setIsAuthenticated(false);
        navigate("/");
    };

    return (
        <nav className="navbar">
            {/* Fix logo click issue */}
            <div className="logo" onClick={() => navigate("/")}>
                📘 LearnHub
            </div>
            
            <div className="nav-links">
                {isAuthenticated ? (
                    <button className="logout-btn" onClick={handleLogout}>Logout</button>
                ) : (
                    <>
                        {location.pathname !== "/login" && <Link to="/login" className="nav-btn">Login</Link>}
                        {location.pathname !== "/signup" && <Link to="/signup" className="nav-btn">Signup</Link>}
                    </>
                )}
            </div>
        </nav>
    );
};

export default Navbar;
