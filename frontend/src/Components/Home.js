import React, { useState } from 'react';
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
  const [activeTab, setActiveTab] = useState('Lessons');

  const renderTabContent = () => {
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
        {renderTabContent()}
      </div>
    </div>
  );
}

export default Home;
