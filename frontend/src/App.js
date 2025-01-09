import React, { useEffect, useState } from 'react';
import axios from 'axios';

function App() {
  const [lessons, setLessons] = useState([]);

  useEffect(() => {
    axios.get(`${process.env.REACT_APP_API_URL}lessons/`)
      .then(response => setLessons(response.data))
      .catch(error => console.error(error));
  }, []);

  return (
    <div>
      <h1>Lessons</h1>
      <ul>
        {lessons.map(lesson => (
          <li key={lesson.id}>
            <h2>{lesson.title}</h2>
            <p>{lesson.content}</p>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
