function Connexion({connect, connect2}) {

    return (
      <div className="Connexion">
            <h1>Welcome to Jobboard</h1>
            <div>
                <button onClick={connect}>Se connecter</button>
                <button onClick={connect2}>S'inscrire</button>
            </div>
      </div>
    );
  }

export default Connexion;