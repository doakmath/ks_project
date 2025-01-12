import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { useAuth0 } from '@auth0/auth0-react';
import './Home.css';
import API_URL from '../config';

function Lessons() {
  const { user, isAuthenticated } = useAuth0();
  const [lessons, setLessons] = useState([]);
  const [userProgress, setUserProgress] = useState([]);
  const [selectedLesson, setSelectedLesson] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  // Fetch lessons and user progress
  useEffect(() => {
    if (isAuthenticated && user) {
      axios.post(`${API_URL}sync_user/`, {
        sub: user.sub,
        email: user.email,
      })
        .then(response => {
          const userId = response.data.id;

          // Use GET method to fetch lessons and progress
          axios.get(`${API_URL}progress/${userId}/`)
            .then(response => {
              setLessons(response.data.lessons);
              setUserProgress(response.data.progress);
              setLoading(false);
            })
            .catch(error => {
              console.error(error);
              setError('Failed to load lessons. Please try again later.');
              setLoading(false);
            });
        })
        .catch(error => {
          console.error(error);
          setError('Failed to sync user data. Please try again later.');
          setLoading(false);
        });
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
    axios.put(`${API_URL}progress/update/${progress.id}/`, updatedProgress)
      .then(response => {
        // Update the state to reflect the changes
        setUserProgress(userProgress.map(p =>
          p.id === progress.id ? response.data : p
        ));
      })
      .catch(error => {
        console.error(error);
        setError('Failed to update progress. Please try again later.');
      });
  };

  // Function to format lesson content for better readability
  const formatLessonContent = (content) => {
    return content.split('\n').map((line, index) => (
      <p key={index} className="lesson-line" style={{ fontSize: '18px' }}>
        {line.trim() ? line : <br />}
      </p>
    ));
  };

  // Render the selected lesson or the list of lessons
  return (
    <div className="home-container">
      <h1>Lessons</h1>
      {user && <h2>{user.nickname}</h2>}

      {error && <p className="error-message">{error}</p>}

      {loading ? (
        <p>Loading lessons...</p>
      ) : selectedLesson ? (
        <div className="tab-content">
          <button onClick={() => setSelectedLesson(null)} style={{ marginBottom: '20px' }}>Back to Lessons</button>
          <h2>{selectedLesson.title}</h2>
          <div>{formatLessonContent(selectedLesson.content)}</div>
          <label style={{ fontSize: '18px', display: 'block', marginBottom: '10px' }}>
            <input
              type="checkbox"
              checked={userProgress.some(progress => progress.lesson === selectedLesson.id && progress.is_complete)}
              onChange={() => toggleCompletion(selectedLesson.id)}
            />
            Mark as Complete
          </label>
          <button onClick={() => setSelectedLesson(null)} style={{ marginTop: '10px' }}>Back to Lessons</button>
        </div>
      ) : (
        <ul>
          {lessons.map(lesson => (
            <li key={lesson.id} className="lesson-item">
              <h2 onClick={() => setSelectedLesson(lesson)} style={{ cursor: 'pointer' }}>
                {lesson.title}
              </h2>
              <p>
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
