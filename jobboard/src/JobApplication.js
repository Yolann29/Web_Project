import './App.css';
import React, { useState , useEffect } from 'react';

function JobApplication() {

    const [ anno, setAnno ] = useState([]);
    const anno2 = 'test';

    const data = {
    'applicant': localStorage.getItem("username")
    };
    console.log(data);

    useEffect(() => {
        fetch('http://127.0.0.1:8000/job', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })
          .then((response) => {
            if (!response.ok) {
              throw new Error('Network response was not ok');
            }
            return response.json();
          })
          .then((data) => {
            console.log(data);
            setAnno(data);
            console.log(anno.length);
            console.log(anno);
          })
          .catch((error) => {
            console.error('Error fetching data:', error);
          });
      }, []);

  const deleteApply = (articleId) => {
    fetch(`http://127.0.0.1:8000/delete_apply/${articleId}/`, {
      method: 'DELETE',
    })
    .then((response) => {
      if (response.status === 204) {
        console.log('Article supprimé avec succès');
      } else {
        console.log('Erreur lors de la suppression');
      }
    })
    .catch((error) => {
      console.log('Erreur réseau ou autre : ', error);
    });
  };

    return (
        <div className="JobApplication">
            <ul>
                {anno.length > 0 ? (
                anno.map((item, index) => (
                    <li key={index}>
                        <p>{item.surname}</p>
                        <p>{item.first_name}</p>
                        <p>{item.email}</p>
                        <button onClick={deleteApply}>Delete</button>
                    </li>
                ))
                ) : (
                    <p>{anno2}</p>
                )}
            </ul>
        </div>
    );
}

export default JobApplication;
