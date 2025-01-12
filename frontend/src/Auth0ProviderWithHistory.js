import React, { useEffect, useState } from 'react';
import { Auth0Provider } from '@auth0/auth0-react';
import axios from 'axios';

const Auth0ProviderWithHistory = ({ children }) => {
  const [authConfig, setAuthConfig] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    axios.get(`${process.env.REACT_APP_API_URL}/auth0-config/`)
      .then(response => {
        setAuthConfig(response.data);
      })
      .catch(error => {
        console.error('Failed to load Auth0 config:', error);
        setError('Failed to load authentication config. Please try again later.');
      });
  }, []);

  if (error) {
    return (
      <div className="error-message">
        <h2>Error</h2>
        <p>{error}</p>
      </div>
    );
  }

  if (!authConfig) {
    return <div>Loading...</div>;
  }

  return (
    <Auth0Provider
      domain={authConfig.auth0_domain}
      clientId={authConfig.auth0_client_id}
      authorizationParams={{
        redirect_uri: window.location.origin
      }}
    >
      {children}
    </Auth0Provider>
  );
};

export default Auth0ProviderWithHistory;
