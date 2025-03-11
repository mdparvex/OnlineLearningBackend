import React, { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import axios from "axios";
import styles from "../styles/Login.module.css";

const API_BASE_URL = "http://localhost:8000/auth";

const Login = ({ setIsAuthenticated }) => {
  const [formData, setFormData] = useState({ username_or_email: "", password: "" });
  const [message, setMessage] = useState("");
  const navigate = useNavigate();

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post(`${API_BASE_URL}/login/`, formData);
      console.log("Login response:", response.data);

      if (response.data.token) {
        localStorage.setItem("token", response.data.token);
        localStorage.setItem("user_id", response.data.user_id);
        localStorage.setItem("user_type", response.data.user_type);

        setIsAuthenticated(true); // Update auth state to trigger re-render
        navigate("/profile");
      } else {
        throw new Error("Invalid login response");
      }
    } catch (error) {
      console.error("Login error:", error);
      setMessage("Login failed. Check credentials.");
    }
  };

  return (
    <div className={styles.container}>
      <h2>Login</h2>
      <form onSubmit={handleSubmit}>
        <input type="text" name="username_or_email" placeholder="Username or Email" onChange={handleChange} required />
        <input type="password" name="password" placeholder="Password" onChange={handleChange} required />
        <button type="submit">Login</button>
      </form>
      <p>{message}</p>
      <p>Do not have an account? <Link to="/signup">Signup</Link></p>
    </div>
  );
};

export default Login;
