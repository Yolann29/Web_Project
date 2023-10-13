import './App.css';
import React, { useEffect, useState } from 'react';

function Offer({ fermer }) {
  const [ anno, setAnno] = useState(null);

  useEffect(() => {
    fetch('http://127.0.0.1:8000')
      .then((response) => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then((data) => {
        console.log(data);
        setAnno(data);
      })
      .catch((error) => {
        console.error('Error fetching data:', error);
      });
  }, []);

  return (
    <div className="Offer">
      <button onClick={fermer}>Back</button>
      {anno && (
      <div>
        <p>Superuser: {anno.superuser}</p>
        <p>Company Name: {anno.companies_name}</p>
        <p>Description: {anno.description}</p>
      </div>
      )}
    </div>
  );
}

export default Offer;