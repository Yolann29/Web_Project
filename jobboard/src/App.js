import React, { useEffect, useState } from 'react';
import './App.css';
import Content from './Content.js';
import Connexion from './Connexion.js';
import Inscription from './Inscription';
import Connexion2 from './Connexion2';
import Pannel from './Pannel';

function App() {
  const [ anno, setAnno] = useState([]);

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

  const [connected, setConnected] = useState(false);
  const [register, setRegister] = useState(false);
  const [approved, setApproved] = useState(false)

  const handleConnexion = () => {
    setConnected(true);
  };

  const handleInscription = () => {
    setRegister(true);
  }

  const handleApproved = () => {
    setApproved(true);
    setRegister(false);
    setConnected(false);
  }

  return (
    <div className="App">
      {!connected && !register && !approved ? (
        <Connexion connect={handleConnexion} connect2={handleInscription} connect3={handleInscription}/>
      ) : (
        <>
          {register && !connected ? <Inscription onApproved={handleApproved}/> : null}
          {!register && connected ? <Connexion2 onApproved={handleApproved}/> : null}
          {approved && (
            <>
              <Pannel />
              {anno && (
              <ul>
                {anno.map((item, index) => (
                  <li key={index}>
                    <Content disp={item.superuser} comp={item.companies_name} text={item.description}/>
                  </li>
                ))}
              </ul>
              )}
            </>
          )}
        </>
      )}
    </div>
  );
}

export default App;
