import React, { useEffect, useState } from 'react';
import axios from 'axios';
import './QuoteModal.css';
import API_URL from '../config';

function QuoteModal() {
  const [randomQuote, setRandomQuote] = useState(null);
  const [randomImage, setRandomImage] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    setLoading(true);
    Promise.all([
      axios.get(`${API_URL}quotes/`),
      axios.get(`${API_URL}image/`)
    ])
      .then(([quotesResponse, imagesResponse]) => {
        if (quotesResponse.data.length > 0 && imagesResponse.data.length > 0) {
          const randomQuoteIndex = Math.floor(Math.random() * quotesResponse.data.length);
          const randomImageIndex = Math.floor(Math.random() * imagesResponse.data.length);
          setRandomQuote(quotesResponse.data[randomQuoteIndex]);
          setRandomImage(imagesResponse.data[randomImageIndex]);
        } else {
          setError('No quotes or images available.');
        }
        setLoading(false);
      })
      .catch(error => {
        console.error('Failed to load quotes or images:', error);
        setError('Failed to load quotes or images. Please try again later.');
        setLoading(false);
      });
  }, []);

  if (loading) {
    return <div>Loading...</div>;
  }

  if (error) {
    return <div className="error-message">{error}</div>;
  }

  return (
    <div className="quote-modal">
      <div className="quote-modal-content">
        {randomImage && <img src={randomImage.image_url} alt="Random" className="quote-image" />}
        {randomQuote && <h3 className="quote-text">{randomQuote.quote}</h3>}
      </div>
    </div>
  );
}

export default QuoteModal;
