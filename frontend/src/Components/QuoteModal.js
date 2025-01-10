import React, { useEffect, useState } from 'react';
import axios from 'axios';

function QuoteModal() {
  const [quotes, setQuotes] = useState([]);
  const [images, setImages] = useState([]);
  const [randomQuote, setRandomQuote] = useState(null);
  const [randomImage, setRandomImage] = useState(null);

  // Fetch quotes and images from the API
  useEffect(() => {
    Promise.all([
      axios.get(`${process.env.REACT_APP_API_URL}quotes/`),
      axios.get(`${process.env.REACT_APP_API_URL}image/`)
    ])
      .then(([quotesResponse, imagesResponse]) => {
        setQuotes(quotesResponse.data);
        setImages(imagesResponse.data);

        // Select random quote and image
        const randomQuoteIndex = Math.floor(Math.random() * quotesResponse.data.length);
        const randomImageIndex = Math.floor(Math.random() * imagesResponse.data.length);
        setRandomQuote(quotesResponse.data[randomQuoteIndex]);
        setRandomImage(imagesResponse.data[randomImageIndex]);
      })
      .catch(error => console.error(error));
  }, []);

  // Render only if both quote and image are loaded
  if (!randomQuote || !randomImage) {
    return <div>Loading...</div>;
  }

  return (
    <div className="quote-modal" style={{ backgroundImage: `url(${randomImage.image_url})` }}>
      <h1>quote modal -------------------------------------------</h1>
      <div className="quote-content">
        <h3>{randomQuote.quote}</h3>
      </div>
    </div>
  );
}

export default QuoteModal;
