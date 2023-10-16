import React, { useState , useEffect } from 'react';
import axios from 'axios';

function Inscription(props) {

    useEffect(() => {
        axios.get('http://127.0.0.1:8000/utilisateur/companies')
          .then((response) => {
            setCompanies(response.data);
          })
          .catch((error) => {
            console.error(error);
          });
      }, []);

    const [surname, setSurname] = useState('');
    const [first_name, setFirst_Name] = useState('');
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [email, setEmail] = useState('');
    const [selectedCompany, setSelectedCompany] = useState('');
    const [companies, setCompanies] = useState([]);

    const ajouterDonnee = () => {
        axios.post('http://127.0.0.1:8000/utilisateur/register', {
            surname,
            first_name,
            username,
            password,
            email,
            companies: selectedCompany,
            })
            .then(res => {
                console.log(res);
                if (res.status === 200) {
                    props.onApproved();
                }
            })
            .catch(err => console.log(err));
    }

    return (
        <div className="Inscription">
            <input type="text" placeholder="Surname" onChange={e => setSurname(e.target.value)} />
            <input type="text" placeholder="First Name" onChange={e => setFirst_Name(e.target.value)} />
            <input type="text" placeholder="Username" onChange={e => setUsername(e.target.value)} />
            <input type="password" placeholder="Password" onChange={e => setPassword(e.target.value)} />
            <input type="email" placeholder="Email" onChange={e => setEmail(e.target.value)} />
            <div id="compform">
                <select
                    value={selectedCompany}
                    onChange={(e) => setSelectedCompany(e.target.value)}
                >
                    <option value="">Sélectionnez une entreprise</option>
                    {companies.map((company) => (
                    <option key={company.id} value={company.id}>
                        {company.name}
                    </option>
                    ))}
                </select>
            </div>
            <button onClick={ajouterDonnee}>Ajouter</button>
        </div>
    )

}

export default Inscription;