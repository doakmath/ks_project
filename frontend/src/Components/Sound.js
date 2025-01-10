import React, { useEffect, useState } from 'react';
import axios from 'axios';


function Sound() {

    const [sound, setSound] = useState([]);

    useEffect(() => {
        axios.get(`${process.env.REACT_APP_API_URL}sound/`)
          .then(response => setSound(response.data))
          .catch(error => console.error(error));
      }, []);

      console.log('sound:', sound)



  return (
    <div>
        <h1>sound div--------------------------------------</h1>
        <ul>
        {sound.map(soun => (
            <li key={soun.id}>
            <h2>{soun.title}</h2>
            <p>{soun.sound_url}</p>
            <p>{soun.description}</p>
            </li>
      ))}
    </ul>
    </div>
  );
}

export default Sound;
