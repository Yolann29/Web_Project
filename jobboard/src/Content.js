import './App.css';
import React, { useState } from 'react';
import Offer from './Offer.js';

function Content(props) {

  const [displayOffer, setDisplayOffer] = useState(false);

  const handleClick1 = () => {
      setDisplayOffer(!displayOffer);
  };

  return (
    <div className="Content">
        <h1>{props.title}</h1>
        <h2>{props.comp}</h2>
        <button onClick={handleClick1}>Learn more</button>
        {displayOffer && <Offer id={props.id} text={props.text} fermer={() => setDisplayOffer(false)}/>}
    </div>
  );
}

export default Content;
