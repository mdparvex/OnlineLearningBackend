import React, { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import axios from "axios";
import styles from "../styles/Signup.module.css";

const API_BASE_URL = "http://localhost:8000/auth";

const Signup = () => {
  const [formData, setFormData] = useState({ username: "", email: "", password: "", user_type: "" });
  const [message, setMessage] = useState("");
  const navigate = useNavigate();
  const options = [
  { label: "Teacher", value: "1" },
  { label: "Student", value: "2" },
];

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      console.log(formData)
      await axios.post(`${API_BASE_URL}/signup/`, formData);
      setMessage("Signup successful! Redirecting to login...");
      setTimeout(() => navigate("/login"), 1500);
    } catch (error) {
      setMessage("Signup failed. Try again.");
    }
  };

  return (
    <div className={styles.container}>
      <h2>Signup</h2>
      <form onSubmit={handleSubmit}>
        <input type="text" name="username" placeholder="Username" onChange={handleChange} required />
        <input type="email" name="email" placeholder="Email" onChange={handleChange} required />
        <input type="password" name="password" placeholder="Password" onChange={handleChange} required />
        <select name="user_type" onChange={handleChange} required>
          <option value="">Please choose user type</option>
          {options.map((option, index) => (
            <option key={index} value={option.value}>
              {option.label}
            </option>
          ))}
        </select>
        <button type="submit">Signup</button>
      </form>
      <p>{message}</p>
      <p>Already have an account? <Link to="/login">Login</Link></p>
    </div>
  );
};

export default Signup;
