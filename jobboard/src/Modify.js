import React, { useState } from 'react';

function Modify(props) {

    const handleSubmit = async (sub) => {
        sub.preventDefault();

        console.log(formulaire);

        try {
            const response = await fetch(`http://127.0.0.1:8000/${props.table}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json'
            },
                body: JSON.stringify(formulaire)
            });

            if (!response.ok) {
                throw new Error('Network response was not ok');
            } else {
                alert("Update completed successfully, please reload to see the result")
            }

            console.log(response);
        } catch (error) {
            console.error('Error fetching data:', error);
        }
    };

    const handledelete = async (sub) => {
        sub.preventDefault();

        try {
            const response = await fetch(`http://127.0.0.1:8000/${props.table}`, {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json'
            },
                body: JSON.stringify({'id' : props.id})
            });

            if (!response.ok) {
                throw new Error('Network response was not ok');
            } else {
                alert("Deleted successfully, please reload to see the result")
            }

            console.log(response);
        } catch (error) {
            console.error('Error fetching data:', error);
        }
    };

    const [formulaire, setFormulaire] = useState({'id' : props.id});

    const handleInputChange = (lab, value) => {
        setFormulaire({ ...formulaire, [lab]: value });
      };

    return (
        <div className='modify'>
            {props.labels.map((lab,index) => (
                <div key={index}>
                    <label id={index}>{lab}</label>
                    <input type="text" id={index} name={lab} value={formulaire[index]} onChange={(ev) => handleInputChange(lab, ev.target.value)} />
                </div>
            ))}
            <input type="submit" onClick={handleSubmit} />
            <button onClick={handledelete}>Delete</button>
            <button onClick={props.fermer}>Back</button>
        </div>
    );
}

export default Modify;