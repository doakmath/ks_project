import React, { useEffect, useState } from 'react';
import axios from 'axios';
import './Home.css';

function Resource() {
  const [resources, setResources] = useState([]);
  const [selectedResource, setSelectedResource] = useState(null);

  // Fetch resources from the API
  useEffect(() => {
    axios.get(`${process.env.REACT_APP_API_URL}resource/`)
      .then(response => setResources(response.data))
      .catch(error => console.error(error));
  }, []);

  // Function to handle selecting/deselecting a resource
  const toggleResource = (resource) => {
    if (selectedResource && selectedResource.id === resource.id) {
      setSelectedResource(null); // Deselect if the same resource is clicked again
    } else {
      setSelectedResource(resource); // Select the clicked resource
    }
  };

  // Function to format resource description for better readability
  const formatDescription = (content) => {
    return content.split('\n').map((line, index) => (
      <p key={index} className="resource-line" style={{ fontSize: '18px' }}>
        {line.trim() ? line : <br />}
      </p>
    ));
  };

  // Render the selected resource or the list of resources
  return (
    <div className="home-container">
      <h1>Resources</h1>

      {selectedResource ? (
        <div className="tab-content">
          <h2 onClick={() => setSelectedResource(null)} style={{ cursor: 'pointer', color: '#007bff', textDecoration: 'underline' }}>{selectedResource.title}</h2>
          {selectedResource.description && formatDescription(selectedResource.description)}
          {selectedResource.link && (
            <p>
              <a href={selectedResource.link} target="_blank" rel="noopener noreferrer">
                {selectedResource.link}
              </a>
            </p>
          )}
        </div>
      ) : (
        <ul>
          {resources.map(resource => (
            <li key={resource.id} className="resource-item">
              <h2
                onClick={() => toggleResource(resource)}
                style={{ cursor: 'pointer', color: '#007bff', textDecoration: 'underline' }}
                onMouseEnter={(e) => (e.target.style.textDecoration = 'none')}
                onMouseLeave={(e) => (e.target.style.textDecoration = 'underline')}
              >
                {resource.title}
              </h2>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default Resource;
