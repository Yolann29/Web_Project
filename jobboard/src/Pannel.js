function Pannel() {

    const supprimerDonnees = () => {
        localStorage.removeItem('username');
        localStorage.removeItem('permissions');
        window.location.reload();
    }

    return (
      <div className="Pannel">
            <div id="username">{localStorage.getItem('username')}</div>
            <div id="disconnect" onClick={supprimerDonnees}>Log out</div>
      </div>
    );
  }

export default Pannel;