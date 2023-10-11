import React, { useState } from 'react';
import axios from 'axios';

function Inscription() {

    const [surname, setSurname] = useState('');
    const [first_name, setFirst_Name] = useState('');
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [email, setEmail] = useState('');

    const ajouterDonnee = () => {
        axios.post('http://127.0.0.1:8000/utilisateur/register', {
            surname,
            first_name,
            username,
            password,
            email
            })
            .then(res => console.log(res))
            .catch(err => console.log(err));
    }

    return (
        <div className="Inscription">
            <input type="text" placeholder="Surname" onChange={e => setSurname(e.target.value)} />
            <input type="text" placeholder="First Name" onChange={e => setFirst_Name(e.target.value)} />
            <input type="text" placeholder="Username" onChange={e => setUsername(e.target.value)} />
            <input type="password" placeholder="Password" onChange={e => setPassword(e.target.value)} />
            <input type="email" placeholder="Email" onChange={e => setEmail(e.target.value)} />
            <button onClick={ajouterDonnee}>Ajouter</button>
        </div>
    )

}

export default Inscription;