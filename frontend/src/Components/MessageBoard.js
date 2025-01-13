import { useAuth0 } from '@auth0/auth0-react';
import React, { useEffect, useState } from 'react';
import axios from 'axios';
import './MessageBoard.css';
import API_URL from '../config';

function MessageBoard() {
  const { user, isAuthenticated } = useAuth0();
  const [comments, setComments] = useState([]);
  const [selectedCommentId, setSelectedCommentId] = useState(null);
  const [newComment, setNewComment] = useState('');
  const [newReply, setNewReply] = useState('');
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  // Fetch comments with replies from the new endpoint
  useEffect(() => {
    setLoading(true);
    axios.get(`${API_URL}/comments-with-replies/`)
      .then((response) => {
        console.log('Fetched comments with replies:', response.data);
        setComments(
          response.data.map(comment => ({
            ...comment,
            replies: comment.replies || [] // Ensure replies is always an array
          })).sort((a, b) => new Date(b.created_at) - new Date(a.created_at))
        );
        setLoading(false);
      })
      .catch(error => {
        console.error(error);
        setError('Failed to load comments and replies. Please try again later.');
        setLoading(false);
      });
  }, []);

  // Handle new comment submission
  const handleCommentSubmit = async () => {
    if (newComment.trim() && isAuthenticated && user) {
      try {
        const response = await axios.post(`${API_URL}/comment/`, {
          message: newComment,
          user_sub: user.sub,
          nickname: user.nickname,
        });
        console.log('New comment response:', response.data);
        setComments([response.data, ...comments]);
        setNewComment('');
      } catch (error) {
        console.error(error);
        setError('Failed to post comment. Please try again later.');
      }
    }
  };

  // Handle new reply submission
  const handleReplySubmit = async (commentId) => {
    if (newReply.trim() && isAuthenticated && user) {
      try {
        const response = await axios.post(`${API_URL}/reply/create/`, {
          comment: commentId,
          reply: newReply,
          user_sub: user.sub,
          nickname: user.nickname,
        });
        console.log('New reply response:', response.data);

        // Update the comments state to include the new reply immediately
        setComments(prevComments => {
          return prevComments.map(comment => {
            if (comment.id === commentId) {
              return {
                ...comment,
                replies: [...(comment.replies || []), response.data.reply] // Ensure replies array exists
              };
            }
            return comment;
          });
        });

        setNewReply('');
      } catch (error) {
        console.error(error);
        setError('Failed to post reply. Please try again later.');
      }
    }
  };

  return (
    <div className="message-board">
      <h1>Message Board</h1>

      {error && <p className="error-message">{error}</p>}

      {loading ? (
        <p>Loading comments and replies...</p>
      ) : (
        <>
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
                <p
                  className="reply-count"
                  onClick={() => setSelectedCommentId(comment.id === selectedCommentId ? null : comment.id)}
                >
                  {(comment.replies ? comment.replies.length : 0)} Replies
                </p>

                {selectedCommentId === comment.id && (
                  <ul className="replies-list">
                    {comment.replies.map(reply => (
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
        </>
      )}
    </div>
  );
}

export default MessageBoard;
