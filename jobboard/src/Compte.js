import React, { useEffect, useState } from 'react';
import Modify from "./Modify.js"

function Compte(props) {

    const [ info, setInfo ] = useState(null);

    useEffect(() => {
        fetch('http://127.0.0.1:8000/myinfos', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
                body: JSON.stringify({'username': props.username})
        })
          .then((response) => {
            if (!response.ok) {
              throw new Error('Network response was not ok');
            }
            return response.json();
        })
          .then((data) => {
            setInfo(data);
            console.log(info)
        })
          .catch((error) => {
            console.error('Error fetching data:', error);
          });
      }, []);

    const [displayModify, setDisplayModify] = useState(false);

    const handleClick = () => {
        setDisplayModify(!displayModify);
      };

    return (
        <table className='Offer'>
            <thead>
                <tr>
                    <th>Last Name</th>
                    <th>Fisrt Name</th>
                    <th>Username</th>
                    <th>Password</th>
                    <th>Email</th>
                    <th>Permission</th>
                    <th>Company</th>
                </tr>
            </thead>
            <tbody>
                {info && (
                    <tr>
                        <td>{info.surname}</td>
                        <td>{info.first_name}</td>
                        <td>{info.username}</td>
                        <td>{info.password}</td>
                        <td>{info.email}</td>
                        <td>{info.permissions}</td>
                        <td>{info.companies}</td>  
                        <td className="btn2" onClick={handleClick}>Modify/Delete</td>
                        {displayModify && <Modify reload='true' table="modUser" id={info.id} labels={["surname","first_name","username","password","email"]} fermer={() => setDisplayModify(false)} />}
                    </tr>
                )}
                <button className='btn2' onClick={props.fermer}>Back</button>
            </tbody>
        </table>
    );
}

export default Compte;