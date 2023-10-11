function Connexion({connect, connect2, connect3}) {

    return (
      <div className="Connexion">
            <h1>Welcome to Jobboard</h1>
            <div>
                <button onClick={connect}>Sign in</button>
                <button onClick={connect2}>User register</button>
                <button onClick={connect3}>Admin register</button>
            </div>
      </div>
    );
  }

export default Connexion;