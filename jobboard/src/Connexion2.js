import React, { useState , useEffect } from 'react';
import axios from 'axios';

function Connexion2(props) {

    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');

    useEffect(() => {
        const storedUsername = localStorage.getItem('username');
        const storedPermissions = localStorage.getItem('permissions');
        if (storedUsername && storedPermissions) {
            props.onApproved();
        }
    }, []);

    const ajouterDonnee = () => {
        axios.post('http://127.0.0.1:8000/utilisateur/login', {
            username,
            password
            })
            .then(res => {
                console.log(res);
                if (res.status === 200) {
                    localStorage.setItem('username', res.data.username);
                    localStorage.setItem('permissions', res.data.permissions);
                    console.log("Données stockées: ", localStorage.getItem('username'), localStorage.getItem('permissions'));
                    props.onApproved();
                }
            })
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