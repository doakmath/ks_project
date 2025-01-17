import Lessons from "./Components/Lessons";
import Comment from "./Components/MessageBoard";
import Resource from "./Components/Resource";
import Sound from "./Components/Sound";
import Video from "./Components/Video";
import Quotes from "./Components/QuoteModal";
import LoginPage from './Components/LoginPage.js';
import Home from './Components/Home.js';
import React from 'react';
import { Routes, Route, Navigate } from 'react-router-dom';
import { useAuth0 } from '@auth0/auth0-react';
import './App.css';

function App() {
  const { isAuthenticated } = useAuth0();

  return (
    <div className="app-container">
      <Routes>
        <Route path="/" element={<Navigate to={isAuthenticated ? "/home" : "/login"} />} />
        <Route path="/login" element={<LoginPage />} />
        <Route path="/home" element={<Home />} />
        <Route path="/lessons" element={<Lessons />} />
        <Route path="/comment" element={<Comment />} />
        <Route path="/resource" element={<Resource />} />
        <Route path="/sound" element={<Sound />} />
        <Route path="/video" element={<Video />} />
        <Route path="/quotes" element={<Quotes />} />
      </Routes>
    </div>
  );
}

export default App;
