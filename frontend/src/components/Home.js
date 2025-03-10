import React from "react";
import { Link } from "react-router-dom";
import "../styles/Home.css"; // Ensure styles match original

const Home = () => {
    return (
        <div>
            {/* Hero Section */}
            <header className="hero">
                <h1>Learn at Your Own Pace</h1>
                <p>Join thousands of learners and start your journey today.</p>
                <Link to="/signup" className="cta-btn">Get Started</Link>
            </header>

            {/* Features Section */}
            <section className="features">
                <div className="feature">
                    <h2>📚 Wide Course Selection</h2>
                    <p>Explore a variety of courses across different domains.</p>
                </div>
                <div className="feature">
                    <h2>🕒 Learn Anytime, Anywhere</h2>
                    <p>Access courses from any device, anytime.</p>
                </div>
                <div className="feature">
                    <h2>🎓 Earn Certificates</h2>
                    <p>Get certified upon course completion.</p>
                </div>
            </section>

            {/* Footer */}
            <footer>
                <p>&copy; 2025 LearnHub. All rights reserved.</p>
            </footer>
        </div>
    );
};

export default Home;
