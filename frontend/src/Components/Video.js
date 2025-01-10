import React, { useEffect, useState } from 'react';
import axios from 'axios';


function Video() {

    const [video, setVideo] = useState([]);

    useEffect(() => {
        axios.get(`${process.env.REACT_APP_API_URL}video/`)
          .then(response => setVideo(response.data))
          .catch(error => console.error(error));
      }, []);

      console.log('video:', video)



  return (
    <div>
        <h1>video div--------------------------------------</h1>
        <ul>
        {video.map(vid => (
            <li key={vid.id}>
            <h2>{vid.title}</h2>
            <p>{vid.video_url}</p>
            <p>{vid.description}</p>
            </li>
      ))}
    </ul>
    </div>
  );
}

export default Video;
