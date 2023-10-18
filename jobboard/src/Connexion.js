function Connexion({connect, connect2 }) {

    return (
      <div className="Connexion">
            <h1>Welcome to Jobboard</h1>
            <div>
                <button onClick={connect}>Sign in</button>
                <button onClick={connect2}>Register</button>
            </div>
      </div>
    );
  }

export default Connexion;