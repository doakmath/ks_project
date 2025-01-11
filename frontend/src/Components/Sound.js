import React, { useEffect, useState } from 'react';
import axios from 'axios';

function Sound() {
  const [sound, setSound] = useState([]);

  useEffect(() => {
    axios.get(`${process.env.REACT_APP_API_URL}sound/`)
      .then(response => setSound(response.data))
      .catch(error => console.error(error));
  }, []);

  // Function to convert Freesound URLs to iframe embed links
  const getFreesoundEmbedLink = (url) => {
    if (url.includes('freesound.org/s/')) {
      const soundId = url.split('/s/')[1].split('/')[0];
      return `https://freesound.org/embed/sound/iframe/${soundId}/simple/large/`;
    }
    return null;
  };

  return (
    <div>
      <h1>Sound Library</h1>
      <ul>
        {sound.map(soun => (
          <li key={soun.id}>
            <h2>{soun.title}</h2>
            <p>{soun.description}</p>

            {getFreesoundEmbedLink(soun.sound_url) ? (
              <iframe
                frameBorder="0"
                scrolling="no"
                src={getFreesoundEmbedLink(soun.sound_url)}
                width="920"
                height="245"
              ></iframe>
            ) : (
              <audio controls>
                <source src={soun.sound_url} type="audio/mpeg" />
                Your browser does not support the audio element.
              </audio>
            )}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Sound;
