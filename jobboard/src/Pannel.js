import React, { useState } from 'react';
import NewOffer from './NewOffer';

function Pannel() {

  const [displayNewOffer, setDisplayNewOffer] = useState(false);
  const permissions = localStorage.getItem('permissions');

  const supprimerDonnees = () => {
      localStorage.removeItem('username');
      localStorage.removeItem('permissions');
      window.location.reload();
  }

  const handleClick = () => {
      setDisplayNewOffer(!displayNewOffer);
  };

  return (
    <div className="Pannel">
      {permissions === '1' ? (
        <div class="btn2" onClick={handleClick}>New Advertisement</div>
      ) : null}
        {displayNewOffer && <NewOffer fermer={() => setDisplayNewOffer(false)} />}
      <div class="btn1">{localStorage.getItem('username')}</div>
      <div class="btn2" onClick={supprimerDonnees}>Log out</div>
    </div>
  );
}

export default Pannel;