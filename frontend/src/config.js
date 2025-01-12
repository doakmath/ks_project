// src/config.js

const API_URL =
  process.env.NODE_ENV === 'development'
    ? 'http://localhost:8000/'
    : process.env.REACT_APP_API_URL || console.warn('Missing REACT_APP_API_URL environment variable.');

export default API_URL;
