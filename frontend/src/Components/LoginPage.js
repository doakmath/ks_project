import React, { useState } from 'react';
import { useAuth0 } from '@auth0/auth0-react';
import './LoginPage.css';

function LoginPage() {
  const { loginWithRedirect, logout, user, isAuthenticated } = useAuth0();
  const [error, setError] = useState(null);

  const handleLogin = async () => {
    try {
      await loginWithRedirect();
    } catch (err) {
      setError('Login failed. Please try again later.');
    }
  };

  const handleLogout = async () => {
    try {
      await logout({ returnTo: window.location.origin });
    } catch (err) {
      setError('Logout failed. Please try again later.');
    }
  };

  return (
    <div style={styles.container}>
      {error && <p className="error-message">{error}</p>}

      {!isAuthenticated ? (
        <>
          <h1>Welcome to KS App</h1>
          <p>Please log in or sign up to continue.</p>
          <button style={styles.button} onClick={handleLogin}>Log In / Sign Up</button>
        </>
      ) : (
        <>
          <h1>Welcome, {user?.name || 'User'}!</h1>
          <p>Email: {user?.email || 'N/A'}</p>
          <button style={styles.button} onClick={handleLogout}>Log Out</button>
        </>
      )}
    </div>
  );
}

const styles = {
  container: {
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
    justifyContent: 'center',
    height: '100vh',
    backgroundColor: '#f0f0f0',
    textAlign: 'center',
  },
  button: {
    padding: '10px 20px',
    fontSize: '18px',
    marginTop: '20px',
    cursor: 'pointer',
    backgroundColor: '#007bff',
    color: '#fff',
    border: 'none',
    borderRadius: '5px',
  },
};

export default LoginPage;
