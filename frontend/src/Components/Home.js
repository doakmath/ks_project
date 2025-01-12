import React, { useState, useEffect } from 'react';
import { useAuth0 } from '@auth0/auth0-react';
import QuoteModal from './QuoteModal';
import Lessons from './Lessons';
import Resource from './Resource';
import Sound from './Sound';
import Video from './Video';
import MessageBoard from './MessageBoard';
import './Home.css';

function Home() {
  const { logout, isAuthenticated } = useAuth0();
  const [activeTab, setActiveTab] = useState(localStorage.getItem('activeTab') || 'Lessons');
  const [error, setError] = useState(null);

  // Store tab selection in localStorage
  useEffect(() => {
    localStorage.setItem('activeTab', activeTab);
  }, [activeTab]);

  // Function to handle tab rendering with error boundary
  const renderTabContent = () => {
    try {
      switch (activeTab) {
        case 'Lessons':
          return <Lessons />;
        case 'Videos':
          return <Video />;
        case 'Sound':
          return <Sound />;
        case 'Resources':
          return <Resource />;
        case 'MessageBoard':
          return <MessageBoard />;
        default:
          return <Lessons />;
      }
    } catch (err) {
      setError('Failed to load the tab content. Please try again later.');
      return <p className="error-message">{error}</p>;
    }
  };

  return (
    <div className="home-container">
      <QuoteModal />

      <div className="tab-navigation">
        <button className={activeTab === 'Lessons' ? 'active' : ''} onClick={() => setActiveTab('Lessons')}>Lessons</button>
        <button className={activeTab === 'Videos' ? 'active' : ''} onClick={() => setActiveTab('Videos')}>Videos</button>
        <button className={activeTab === 'Sound' ? 'active' : ''} onClick={() => setActiveTab('Sound')}>Sound</button>
        <button className={activeTab === 'Resources' ? 'active' : ''} onClick={() => setActiveTab('Resources')}>Resources</button>
        <button className={activeTab === 'MessageBoard' ? 'active' : ''} onClick={() => setActiveTab('MessageBoard')}>Message Board</button>

        {isAuthenticated && (
          <button className="logout-button" onClick={() => logout({ returnTo: window.location.origin })}>
            Log Out
          </button>
        )}
      </div>

      <div className={`tab-content ${activeTab === 'MessageBoard' ? 'message-board-tab' : ''}`}>
        {error ? <p className="error-message">{error}</p> : renderTabContent()}
      </div>
    </div>
  );
}

export default Home;
