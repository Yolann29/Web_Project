import React, { useState } from 'react';
import Offer from './Offer.js';

function Apply(props) {
    const [lname, setLname] = useState(null);
    const [fname, setFname] = useState(null);
    const [email, setEmail] = useState(null);

    const handleSubmit = async (sub) => {
        sub.preventDefault();
        props.fermer();

        const data = {
        'company': props.comp,
        'applicant': localStorage.getItem("username"),
        'surname': lname,
        'first_name': fname,
        'email': email
        };
        console.log(data);

        try {
            const response = await fetch('http://127.0.0.1:8000/apply', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(data)
            });

            if (!response.ok) {
                throw new Error('Network response was not ok');
            } else {
                alert("Applying successfully")
            };
            

            const responseData = await response.json();
            console.log(responseData);
        } catch (error) {
            console.error('Error fetching data:', error);
        };
    };
    
    return (
        <form onSubmit={handleSubmit}>
            <label id="surname">Last name :</label>
            <input type="text" id="surname" name="surname" value={lname} onChange={(ev) => setLname(ev.target.value)}/>
            <label id="first_name">Fisrt name :</label>
            <input type="text" id="first_name" name="first_name" value={fname} onChange={(ev) => setFname(ev.target.value)}/>
            <label id="email">Email :</label>
            <input type="email" id="email" name="email" value={email} onChange={(ev) => setEmail(ev.target.value)}/>
            <input type="submit" value="Confirm" />
        </form>
  );
}

export default Apply;