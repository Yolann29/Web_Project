import './App.css';
import React, { useState , useEffect } from 'react';
import Modify from "./Modify.js"

function JobApplication(props) {

    const [ anno, setAnno ] = useState([]);
    const permissions = localStorage.getItem('permissions');

    console.log(props.donnee);

    useEffect(() => {
        fetch(`http://127.0.0.1:8000/${props.parametre}`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(props.donnee)
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
      if (response.status === 200) {
        console.log('Article supprimé avec succès');
        const updatedAnno = anno.filter(item => item.id !== articleId); // Créer une nouvelle liste sans l'article supprimé
        setAnno(updatedAnno); // Mettre à jour l'état
      } else {
        console.log('Erreur lors de la suppression');
      }
    })
    .catch((error) => {
      console.log('Erreur réseau ou autre : ', error);
    });
  };

  const [displayModify, setDisplayModify] = useState(null);

  const handleClick = (index) => {
    setDisplayModify(index);
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
                        {permissions === '2' ? (
                          <>
                            <p>{item.title}</p>
                            <p>{item.company}</p>
                            <button class="btn2" onClick={() => deleteApply(item.id)}>Delete</button>
                            <button class="btn2" onClick={() => handleClick(index)}>Modify</button>
                            {displayModify === index && <Modify table="modJobApp" id={item.id} labels={["surname","first_name","email"]} fermer={() => setDisplayModify(null)} />}
                          </>
                        ) : null}
                    </li>
                ))
                ) : (
                    <p>No applications for the moment</p>
                )}
                <button className='btn2' onClick={props.fermer}>Back</button>
            </ul>
        </div>
    );
}

export default JobApplication;
