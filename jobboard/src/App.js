import React, { useState } from 'react';
import './App.css';
import Content from './Content.js';
import Connexion from './Connexion.js';

function App() {

  const [connected, setConnected] = useState(false);

  const handleConnexion = () => {
    setConnected(true);
  };

  return (
    <div className="App">
      {!connected ? (
        <Connexion connect={handleConnexion} />
      ) : (
        <>
          <Content title="Job 1" text="Ceci est la première annonce"/>
          <Content title="Job 2" text="Ceci est la deuxième annonce"/>
          <Content title="Job 3" text="Ceci est la troisième annonce"/>
          <Content title="Job 4" text="Ceci est la quatrième annonce"/>
          <Content title="Job 5" text="Ceci est la cinquième annonce"/>
          <Content title="Job 6" text="Ceci est la sixième annonce"/>
          <Content title="Job 7" text="Ceci est la septième annonce"/>
          <Content title="Job 8" text="Ceci est la huitième annonce"/>
        </>
      )}
    </div>
  );
}

export default App;
