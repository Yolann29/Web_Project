function Connexion({connect}) {
    return (
      <div className="Connexion">
            <h1>Welcome to Jobboard</h1>
            <div>
                <button onClick={connect}>Se connecter</button>
                <button onClick={connect}>S'inscrire</button>
            </div>
      </div>
    );
  }

export default Connexion;