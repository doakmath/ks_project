import React, { useEffect, useState } from 'react';
import axios from 'axios';

function Video() {
  const [video, setVideo] = useState([]);

  useEffect(() => {
    axios.get(`${process.env.REACT_APP_API_URL}video/`)
      .then(response => setVideo(response.data))
      .catch(error => console.error(error));
  }, []);

  return (
    <div>
      <h1>Video Library</h1>
      <ul>
        {video.map(vid => (
          <li key={vid.id}>
            <h2>{vid.title}</h2>
            <p>{vid.description}</p>
            {vid.video_url && (
              <iframe
                width="560"
                height="315"
                src={vid.video_url}
                title={vid.title}
                frameBorder="0"
                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                allowFullScreen
              ></iframe>
            )}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Video;
