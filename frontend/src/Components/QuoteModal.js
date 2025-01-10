import React, { useEffect, useState } from 'react';
import axios from 'axios';
import './QuoteModal.css';

function QuoteModal() {
  const [quotes, setQuotes] = useState([]);
  const [images, setImages] = useState([]);
  const [randomQuote, setRandomQuote] = useState(null);
  const [randomImage, setRandomImage] = useState(null);

  useEffect(() => {
    Promise.all([
      axios.get(`${process.env.REACT_APP_API_URL}quotes/`),
      axios.get(`${process.env.REACT_APP_API_URL}image/`)
    ])
      .then(([quotesResponse, imagesResponse]) => {
        setQuotes(quotesResponse.data);
        setImages(imagesResponse.data);

        const randomQuoteIndex = Math.floor(Math.random() * quotesResponse.data.length);
        const randomImageIndex = Math.floor(Math.random() * imagesResponse.data.length);
        setRandomQuote(quotesResponse.data[randomQuoteIndex]);
        setRandomImage(imagesResponse.data[randomImageIndex]);
      })
      .catch(error => console.error(error));
  }, []);

  if (!randomQuote || !randomImage) {
    return <div>Loading...</div>;
  }

  return (
    <div className="quote-modal">
      <div className="quote-modal-content">
        <img src={randomImage.image_url} alt="Random" className="quote-image" />
        <h3 className="quote-text">{randomQuote.quote}</h3>
      </div>
    </div>
  );
}

export default QuoteModal;
