import React, { useState } from 'react';
import QuoteModal from './QuoteModal';
import Lessons from './Lessons';
import Resource from './Resource';
import Sound from './Sound';
import Video from './Video';
import MessageBoard from './MessageBoard';
import './Home.css'; // Import a CSS file for styling

function Home() {
  // State to keep track of which tab is active
  const [activeTab, setActiveTab] = useState('Lessons');

  // Function to render the active tab's component
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
      {/* Quote Modal at the top */}
      <QuoteModal />

      {/* Tabs for navigation */}
      <div className="tab-navigation">
        <button className={activeTab === 'Lessons' ? 'active' : ''} onClick={() => setActiveTab('Lessons')}>Lessons</button>
        <button className={activeTab === 'Videos' ? 'active' : ''} onClick={() => setActiveTab('Videos')}>Videos</button>
        <button className={activeTab === 'Sound' ? 'active' : ''} onClick={() => setActiveTab('Sound')}>Sound</button>
        <button className={activeTab === 'Resources' ? 'active' : ''} onClick={() => setActiveTab('Resources')}>Resources</button>
        <button className={activeTab === 'MessageBoard' ? 'active' : ''} onClick={() => setActiveTab('MessageBoard')}>Message Board</button>
      </div>

      {/* Render the content based on the active tab */}
      <div className="tab-content">
        {renderTabContent()}
      </div>
    </div>
  );
}

export default Home;
