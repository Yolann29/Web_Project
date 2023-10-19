import './App.css';
import React, { useState } from 'react';
import Apply from './Apply.js';


function Offer(props) {

  const [displayApply, setDisplayApply] = useState(false);

  const handleClick = () => {
    setDisplayApply(!displayApply);
};

  return (
    <div className="Offer">
      <button onClick={props.fermer}>Back</button>
      <p>{props.text}</p>
      <button onClick={handleClick}>Apply</button>
      {displayApply && <Apply id={props.id} comp={props.comp} fermer={props.fermer}/>}
    </div>
  );  
}


export default Offer;