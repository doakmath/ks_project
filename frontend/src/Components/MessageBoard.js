import React, { useEffect, useState } from 'react';
import axios from 'axios';

function MessageBoard() {
  const [comments, setComments] = useState([]);
  const [replies, setReplies] = useState([]);

  // Fetch both comments and replies
  useEffect(() => {
    Promise.all([
      axios.get(`${process.env.REACT_APP_API_URL}comment/`),
      axios.get(`${process.env.REACT_APP_API_URL}reply/`)
    ])
      .then(([commentsResponse, repliesResponse]) => {
        setComments(commentsResponse.data);
        setReplies(repliesResponse.data);
      })
      .catch(error => console.error(error));
  }, []);

  return (
    <div>
      <h1>Message Board</h1>
      <ul>
        {comments.map(comment => (
          <li key={comment.id} style={{ marginBottom: '20px', border: '1px solid #ccc', padding: '10px', borderRadius: '5px' }}>
            <h2>{comment.user}</h2>
            <p>{comment.message}</p>
            <p>{new Date(comment.created_at).toLocaleString()}</p>

            {/* Show replies if they exist */}
            {replies.filter(reply => reply.comment === comment.id).length > 0 && (
              <ul style={{ marginTop: '10px', paddingLeft: '20px', borderLeft: '2px solid #ccc' }}>
                {replies
                  .filter(reply => reply.comment === comment.id)
                  .map(reply => (
                    <li key={reply.id} style={{ marginBottom: '10px' }}>
                      <p>↪ {reply.reply}</p>
                      <p>- {reply.user}</p>
                      <p>{new Date(reply.created_at).toLocaleString()}</p>
                    </li>
                  ))}
              </ul>
            )}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default MessageBoard;
