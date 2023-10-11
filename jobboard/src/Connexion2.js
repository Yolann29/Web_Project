import React, { useState } from 'react';
import axios from 'axios';

function Connexion2() {

    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');

    const ajouterDonnee = () => {
        axios.post('http://127.0.0.1:8000/utilisateur/login', {
            username,
            password
            })
            .then(res => console.log(res))
            .catch(err => console.log(err));
    }

    return (
        <div className="Connexion2">
            <input type="text" placeholder="Username" onChange={e => setUsername(e.target.value)} />
            <input type="password" placeholder="Password" onChange={e => setPassword(e.target.value)} />
            <button onClick={ajouterDonnee}>Se connecter</button>
        </div>
    )

}

export default Connexion2;