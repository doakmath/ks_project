import React, { useEffect, useState } from 'react';
import axios from 'axios';
import API_URL from '../config';

function Video() {
  const [video, setVideo] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    setLoading(true);
    axios.get(`${API_URL}video/`)
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
          <li key={vid.id}>
            <h2>{vid.title}</h2>
            <p>{vid.description}</p>
            {vid.video_url ? (
              <iframe
                width="560"
                height="315"
                src={vid.video_url}
                title={vid.title}
                frameBorder="0"
                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                allowFullScreen
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
