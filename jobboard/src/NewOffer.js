import './App.css';
import React, { useState } from 'react';
import axios from 'axios';

function NewOffer({fermer}) {

    const [name, setName] = useState('');
    const [description, setDescription] = useState('');
    const username = localStorage.getItem('username');

    const ajouterDonnee = () => {
        axios.post('http://127.0.0.1:8000/utilisateur/newoffer', {
            name,
            description,
            username,
            })
            .then(res => {
                console.log(res);
                if (res.status === 200) {
                    alert("Offre postée");
                    console.log("Offre postée");
                }
            })
            .catch(err => console.log(err));
    }

    return (
        <div className="NewOffer">
            <input type="text" placeholder="Name" onChange={e => setName(e.target.value)}/>
            <input type="text" placeholder="Description"onChange={e => setDescription(e.target.value)}/>
            <button onClick={ajouterDonnee}>Send</button>
            <button onClick={fermer}>Close</button>
        </div>
    );
}

export default NewOffer;
