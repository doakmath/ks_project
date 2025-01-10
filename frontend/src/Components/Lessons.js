import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { useAuth0 } from '@auth0/auth0-react';

function Lessons() {
  const { user, isAuthenticated } = useAuth0();
  const [lessons, setLessons] = useState([]);
  const [userProgress, setUserProgress] = useState([]);
  const [selectedLesson, setSelectedLesson] = useState(null);

  // Fetch lessons and user progress
  useEffect(() => {
    if (isAuthenticated && user) {
      axios.post(`${process.env.REACT_APP_API_URL}sync_user/`, {
        sub: user.sub,
        email: user.email,
      })
        .then(response => {
          const userId = response.data.id;

          // Use GET method to fetch lessons and progress
          axios.get(`${process.env.REACT_APP_API_URL}progress/${userId}/`)
            .then(response => {
              setLessons(response.data.lessons);
              setUserProgress(response.data.progress);
            })
            .catch(error => console.error(error));
        })
        .catch(error => console.error(error));
    }
  }, [isAuthenticated, user]);

  // Function to toggle completion status of a lesson
  const toggleCompletion = (lessonId) => {
    const progress = userProgress.find(progress => progress.lesson === lessonId);

    if (!progress) {
      console.error('Progress not found for this lesson');
      return;
    }

    // Toggle the completion status
    const updatedProgress = {
      ...progress,
      is_complete: !progress.is_complete,
    };

    // Use PUT method to update progress in the backend
    axios.put(`${process.env.REACT_APP_API_URL}progress/update/${progress.id}/`, updatedProgress)
      .then(response => {
        // Update the state to reflect the changes
        setUserProgress(userProgress.map(p =>
          p.id === progress.id ? response.data : p
        ));
      })
      .catch(error => console.error(error));
  };

  // Render the selected lesson or the list of lessons
  return (
    <div>
      <h1>Lessons</h1>

      {selectedLesson ? (
        <div>
          <h2>{selectedLesson.title}</h2>
          <p>{selectedLesson.content}</p>
          <label>
            <input
              type="checkbox"
              checked={userProgress.some(progress => progress.lesson === selectedLesson.id && progress.is_complete)}
              onChange={() => toggleCompletion(selectedLesson.id)}
            />
            Mark as Complete
          </label>
          <button onClick={() => setSelectedLesson(null)}>Back to Lessons</button>
        </div>
      ) : (
        <ul>
          {lessons.map(lesson => (
            <li key={lesson.id}>
              <h2 onClick={() => setSelectedLesson(lesson)} style={{ cursor: 'pointer' }}>
                {lesson.title}
              </h2>
              <p>
                Complete?{" "}
                {userProgress.some(progress => progress.lesson === lesson.id && progress.is_complete)
                  ? "✅ Completed"
                  : "❌ Not Completed"}
              </p>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default Lessons;
