import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import logo from './logo.svg';
import './App.css';
import AutoEmailSender from './pages/AutoEmailSender'; // Adjust the import path if necessary

function App() {
  return (
    <Router>
      <div className="App">
        <Routes>
          {/* Default route (existing App content) */}
          <Route
            path="/"
            element={
              <header className="App-header">
                <img src={logo} className="App-logo" alt="logo" />
                <p>
                  Edit <code>src/App.tsx</code> and save to reload.
                </p>
                <a
                  className="App-link"
                  href="https://reactjs.org"
                  target="_blank"
                  rel="noopener noreferrer"
                >
                  Learn React
                </a>
              </header>
            }
          />
          {/* Route for AutoEmailSender */}
          <Route path="/auto_email_sender" element={<AutoEmailSender />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;