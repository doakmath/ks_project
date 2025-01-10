import { useAuth0 } from '@auth0/auth0-react';
import React, { useEffect, useState } from 'react';
import axios from 'axios';
import './MessageBoard.css';

function MessageBoard() {
  const { user, isAuthenticated } = useAuth0();
  const [comments, setComments] = useState([]);
  const [replies, setReplies] = useState([]);
  const [selectedCommentId, setSelectedCommentId] = useState(null);
  const [newComment, setNewComment] = useState('');
  const [newReply, setNewReply] = useState('');

  // Fetch both comments and replies
  useEffect(() => {
    Promise.all([
      axios.get(`${process.env.REACT_APP_API_URL}comment/`),
      axios.get(`${process.env.REACT_APP_API_URL}reply/`)
    ])
      .then(([commentsResponse, repliesResponse]) => {
        // Sort comments in reverse order to display the most recent first
        setComments(commentsResponse.data.sort((a, b) => new Date(b.created_at) - new Date(a.created_at)));
        setReplies(repliesResponse.data);
      })
      .catch(error => console.error(error));
  }, []);

  // Handle new comment submission
  const handleCommentSubmit = () => {
    if (newComment.trim() && isAuthenticated && user) {
      axios.post(`${process.env.REACT_APP_API_URL}comment/`, {
        message: newComment,
        user_sub: user.sub, // Send the user's sub from Auth0
        nickname: user.nickname, // Include the nickname
      })
        .then(response => {
          // Prepend the new comment to the comments array
          setComments([response.data, ...comments]);
          setNewComment('');
        })
        .catch(error => console.error(error));
    }
  };

  // Handle new reply submission
  const handleReplySubmit = (commentId) => {
    if (newReply.trim() && isAuthenticated && user) {
      axios.post(`${process.env.REACT_APP_API_URL}reply/create/`, {
        comment: commentId,
        reply: newReply,
        user_sub: user.sub,
        nickname: user.nickname
      })
        .then(response => {
          setReplies(prevReplies => {
            const updatedReplies = [...prevReplies, response.data];
            return updatedReplies;
          });
          setNewReply('');
          setSelectedCommentId(commentId);  // Ensure replies are visible immediately
        })
        .then(() => {
          // Refetch replies for the specific comment to ensure consistency
          axios.get(`${process.env.REACT_APP_API_URL}reply/?comment=${commentId}`)
            .then(replyResponse => {
              setReplies(prevReplies => {
                const filteredReplies = prevReplies.filter(reply => reply.comment !== commentId);
                const uniqueReplies = [...new Map([...filteredReplies, ...replyResponse.data].map(item => [item.id, item])).values()];
                return uniqueReplies;
              });
            });
        })
        .catch(error => console.error(error));
    }
  };

  return (
    <div className="message-board">
      <h1>Message Board</h1>

      <div className="new-comment">
        <input
          type="text"
          placeholder="Leave a message..."
          value={newComment}
          onChange={(e) => setNewComment(e.target.value)}
        />
        <button onClick={handleCommentSubmit}>Post</button>
      </div>

      <ul>
        {comments.map(comment => (
          <li key={comment.id} className="comment-item">
            <h2>{comment.nickname || 'Anonymous'}</h2>
            <p>{comment.message}</p>
            <p>{new Date(comment.created_at).toLocaleString()}</p>
            <p className="reply-count" onClick={() => setSelectedCommentId(comment.id === selectedCommentId ? null : comment.id)}>
              {replies.filter(reply => reply.comment === comment.id).length} Replies
            </p>

            {/* Show replies if selected */}
            {selectedCommentId === comment.id && (
              <ul className="replies-list">
                {replies.filter(reply => reply.comment === comment.id).map(reply => (
                  <li key={reply.id} className="reply-item">
                    <p>↪ {reply.reply}</p>
                    <p>- {reply.nickname || 'Anonymous'}</p>
                    <p>{new Date(reply.created_at).toLocaleString()}</p>
                  </li>
                ))}
                <li className="new-reply">
                  <input
                    type="text"
                    placeholder="Write a reply..."
                    value={newReply}
                    onChange={(e) => setNewReply(e.target.value)}
                  />
                  <button onClick={() => handleReplySubmit(comment.id)}>Reply</button>
                </li>
              </ul>
            )}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default MessageBoard;
