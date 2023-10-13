import './App.css';
import React, { useState } from 'react';
import Offer from './Offer.js';

function Content(props) {

    const [displayOffer, setDisplayOffer] = useState(false);

    const handleClick = () => {
        setDisplayOffer(!displayOffer);
    };

  return (
    <div className="Content">
        <h1>{props.title}</h1>
        <p>{props.text}</p>
        <button onClick={handleClick}>Learn more</button>
        {displayOffer && <Offer fermer={() => setDisplayOffer(false)} ad="CAPGEMINI"/>}
    </div>
  );
}

export default Content;
