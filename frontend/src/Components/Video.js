import React, { useEffect, useState } from 'react';
import axios from 'axios';
import API_URL from '../config';

function Video() {
  const [video, setVideo] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    setLoading(true);
    axios.get(`${API_URL}/video/`)
      .then(response => {
        setVideo(response.data);
        setLoading(false);
      })
      .catch(error => {
        console.error(error);
        setError('Failed to load videos. Please try again later.');
        setLoading(false);
      });
  }, []);

  if (loading) {
    return <p>Loading videos...</p>;
  }

  if (error) {
    return <p className="error-message">{error}</p>;
  }

  return (
    <div>
      <h1>Video Library</h1>
      <ul>
        {video.map(vid => (
          <li key={vid.id} style={{ marginBottom: '20px' }}>
            <h2>{vid.title}</h2>
            <p>{vid.description}</p>
            {vid.video_url ? (
              <iframe
                width="392"  /* Adjusted to 30% smaller width */
                height="220"  /* Adjusted to 30% smaller height */
                src={vid.video_url}
                title={vid.title}
                frameBorder="0"
                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                allowFullScreen
                style={{ borderRadius: '12px', boxShadow: '0 4px 8px rgba(0, 0, 0, 0.1)' }}
              ></iframe>
            ) : (
              <p>No video available.</p>
            )}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Video;
