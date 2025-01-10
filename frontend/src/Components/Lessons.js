import React, { useEffect, useState } from 'react';
import axios from 'axios';


function Lessons() {
const [lessons, setLessons] = useState([]);

useEffect(() => {
  axios.get(`${process.env.REACT_APP_API_URL}lessons/`)
    .then(response => setLessons(response.data))
    .catch(error => console.error(error));
}, []);

return (
  <div>
    <h1>lessons div ----------------------------</h1>
    <ul>
      {lessons.map(lesson => (
        <li key={lesson.id}>
          <h2>{lesson.title}</h2>
          <p>{lesson.content}</p>
          <p>Complete? {lesson.is_complete === true ? "Yes" : "No"}</p>
        </li>
      ))}
    </ul>
  </div>
);
}


export default Lessons;
