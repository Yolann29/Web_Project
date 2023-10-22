import React, { useEffect, useState } from 'react';
import JobApplication from './JobApplication';
import Modify from "./Modify.js"

function Ads(props) {

    const [ anno, setAnno ] = useState([]);

    useEffect(() => {
        fetch('http://127.0.0.1:8000/myads', {
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
            setAnno(data);
        })
          .catch((error) => {
            console.error('Error fetching data:', error);
          });
      }, []);

    const [displayJobApplication, setDisplayJobApplication] = useState(null);
    const [displayModify, setDisplayModify] = useState(null);

    const handleClick1 = (index) => {
        setDisplayJobApplication(index);
    };

    const handleClick2 = (index) => {
        setDisplayModify(index);
      };

    return (
        <table className='Offer'>
            <thead>
                <tr>
                    <th>Title</th>
                    <th>Description</th>
                    <th>Your Company</th>
                    <th>Job Applications</th>
                </tr>
            </thead>
            <tbody>
                {anno.length > 0 ? (
                    anno.map((item, index) => (
                        <tr key={index}>
                            <td>{item.title}</td>
                            <td>{item.description}</td>
                            <td>{item.companies}</td>
                            <td className='btn2' onClick={() => handleClick1(index)}>Consult Job Application</td>
                            {displayJobApplication === index && <JobApplication parametre="myapps" donnee={{'id' : item.id}} fermer={() => setDisplayJobApplication(null)} />}
                            <td class="btn2" onClick={() => handleClick2(index)}>Modify/Delete</td>
                            {console.log(item.id)}
                            {displayModify === index && <Modify table="modAnn" id={item.id} labels={["title","description"]} fermer={() => setDisplayModify(null)} />}
                        </tr>
                    ))
                ) : (
                    <tr>
                        <td>No advertisements have been posted at this time.</td>
                        <td></td>
                        <td></td>
                        <td></td>
                    </tr>
                )}
                <button className='btn2' onClick={props.fermer}>Back</button>
            </tbody>
        </table>
    );
}

export default Ads;