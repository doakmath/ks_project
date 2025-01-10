import React, { useEffect, useState } from 'react';
import axios from 'axios';


function Resource() {

    const [resource, setResource] = useState([]);

    useEffect(() => {
        axios.get(`${process.env.REACT_APP_API_URL}resource/`)
          .then(response => setResource(response.data))
          .catch(error => console.error(error));
      }, []);

      console.log('resource:', resource)



  return (
    <div>
        <h1>resource div--------------------------------------</h1>
        <ul>
        {resource.map(resourc => (
            <li key={resourc.id}>
            <h2>{resourc.title}</h2>
            <p>{resourc.link}</p>
            <p>{resourc.description}</p>
            </li>
      ))}
    </ul>
    </div>
  );
}

export default Resource;
