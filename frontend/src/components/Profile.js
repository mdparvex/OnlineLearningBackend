import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";
import styles from "../styles/Profile.module.css";

const API_BASE_URL = "http://localhost:8000/auth";

const Profile = () => {
  const [user, setUser] = useState(null);
  const [isEditing, setIsEditing] = useState(false);
  const [formData, setFormData] = useState({ first_name: "", last_name: "", photo: null });
  const navigate = useNavigate();

  useEffect(() => {
    const token = localStorage.getItem("token");
    const user_id = localStorage.getItem("user_id");
    const user_type = localStorage.getItem("user_type");

    if (!token || !user_id || !user_type) {
      navigate("/login");
      return;
    }

    const fetchUserDetails = async (userId, userType) => {
      try {
        const endpoint = userType === "1" ? `instructor/${userId}/` : `student/${userId}/`;
        const response = await axios.get(`${API_BASE_URL}/${endpoint}`, {
          headers: { Authorization: `Token ${token}` },
        });

        const userData = response.data.user_data; // Access the correct structure
        console.log("data")
        console.log(userData)
        setUser(userData);
        setFormData({
          first_name: userData.first_name,
          last_name: userData.last_name,
          photo: userData.photo,
        });
      } catch (error) {
        console.error("Error fetching user:", error);
        localStorage.clear();
        navigate("/login");
      }
    };

    fetchUserDetails(user_id, user_type);
  }, [navigate]);

  const handleEdit = () => setIsEditing(true);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prev) => ({ ...prev, [name]: value }));
  };

  const handleFileChange = (e) => {
    setFormData((prev) => ({ ...prev, photo: e.target.files[0] }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const token = localStorage.getItem("token");
    const user_id = localStorage.getItem("user_id");
    const user_type = localStorage.getItem("user_type");

    const endpoint = user_type === "1" ? `instructor/${user_id}/` : `student/${user_id}/`;

    const formDataToSend = new FormData();
    formDataToSend.append("first_name", formData.first_name);
    formDataToSend.append("last_name", formData.last_name);
    if (formData.photo instanceof File) {
      formDataToSend.append("photo", formData.photo);
    }

    try {
      const response = await axios.patch(`${API_BASE_URL}/${endpoint}`, formDataToSend, {
        headers: {
          Authorization: `Token ${token}`,
          "Content-Type": "multipart/form-data",
        },
      });
      setUser(response.data.user_data);
      setIsEditing(false);
    } catch (error) {
      console.error("Error updating profile", error);
    }
  };

  return user ? (
    <div className={styles.container}>
      <nav>
        <h2>{localStorage.getItem("user_type") === "1" ? "Instructor" : "Student"}</h2>
      </nav>
      <h2>
        Welcome, {user.first_name || "No First Name"} {user.last_name || "No Last Name"}
      </h2>
      {user.photo && <img src={new URL(user.photo, API_BASE_URL).href} alt="Profile" width={100} height={100} />}

      {isEditing ? (
        <form onSubmit={handleSubmit}>
          <input type="text" name="first_name" value={formData.first_name} onChange={handleChange} required />
          <input type="text" name="last_name" value={formData.last_name} onChange={handleChange} required />
          <input type="file" name="photo" accept="learning/image/*" onChange={handleFileChange} />
          <button type="submit">Save</button>
          <button type="button" onClick={() => setIsEditing(false)}>
            Cancel
          </button>
        </form>
      ) : (
        <button onClick={handleEdit}>Edit</button>
      )}
    </div>
  ) : (
    <p>Loading...</p>
  );
};

export default Profile;


