import './App.css';
import React, { useState } from 'react';
import Apply from './Apply.js';


function Offer(props) {

  const [displayApply, setDisplayApply] = useState(false);
  const permissions = localStorage.getItem('permissions');

  const handleClick = () => {
    setDisplayApply(!displayApply);
};

  return (
    <div className="Offer">
      <button onClick={props.fermer}>Back</button>
      <p>{props.text}</p>
      {permissions === '2' ? (
        <button onClick={handleClick}>Apply</button>
      ) : null}
      {displayApply && <Apply id={props.id} fermer={props.fermer}/>}
    </div>
  );  
}


export default Offer;