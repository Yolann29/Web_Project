import './App.css';
import React, { useState } from 'react';
import Offer from './Offer.js';
import ModAnn from './ModAnn.js';

function Content(props) {

  const [displayOffer, setDisplayOffer] = useState(false);
  const [displayModAnn, setDisplayModAnn] = useState(false);
  const permissions = localStorage.getItem('permissions');

  const handleClick1 = () => {
      setDisplayOffer(!displayOffer);
  };

  const handleClick2 = () => {
    setDisplayModAnn(!displayModAnn);
  };

  return (
    <div className="Content">
        <h1>{props.title}</h1>
        <h2>{props.comp}</h2>
        <button onClick={handleClick1}>Learn more</button>
        {displayOffer && <Offer comp={props.comp} text={props.text} fermer={() => setDisplayOffer(false)}/>}
        {permissions === '1' ? (
                <div class="btn2" onClick={handleClick2}>Modify</div>
            ) : null}
            {displayModAnn && <ModAnn fermer={() => setDisplayModAnn(false)} />}
    </div>
  );
}

export default Content;
