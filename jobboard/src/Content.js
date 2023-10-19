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
        <h2>{props.comp}</h2>
        <button onClick={handleClick}>Learn more</button>
        {displayOffer && <Offer text={props.text} fermer={() => setDisplayOffer(false)}/>}
    </div>
  );
}

export default Content;
