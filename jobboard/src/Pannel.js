import React, { useState } from 'react';
import NewOffer from './NewOffer';
import JobApplication from './JobApplication';

function Pannel() {

    const [displayNewOffer, setDisplayNewOffer] = useState(false);
    const [displayJobApplication, setDisplayJobApplication] = useState(false);
    const permissions = localStorage.getItem('permissions');

    const supprimerDonnees = () => {
        localStorage.removeItem('username');
        localStorage.removeItem('permissions');
        window.location.reload();
    }

    const handleClick1 = () => {
        setDisplayNewOffer(!displayNewOffer);
    };

    const handleClick2 = () => {
      setDisplayJobApplication(!displayJobApplication);
  };

    return (
      <div className="Pannel">
            {permissions === '1' ? (
                <div class="btn2" onClick={handleClick1}>New Advertisement</div>
            ) : null}
            {permissions === '2' ? (
                <div class="btn2" onClick={handleClick2}>Consult Job Application</div>
            ) : null}
            {displayNewOffer && <NewOffer fermer={() => setDisplayNewOffer(false)} />}
            {displayJobApplication && <JobApplication fermer={() => setDisplayJobApplication(false)} />}
            <div class="btn1">{localStorage.getItem('username')}</div>
            <div class="btn2" onClick={supprimerDonnees}>Log out</div>
      </div>
    );
  }

export default Pannel;