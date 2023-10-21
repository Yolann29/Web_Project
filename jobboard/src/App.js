import React, { useEffect, useState } from 'react';
import './App.css';
import Content from './Content.js';
import Connexion from './Connexion.js';
import Inscription from './Inscription';
import Connexion2 from './Connexion2';
import Pannel from './Pannel';
import Button from "./Button.js";
import Modify from "./Modify.js"

function App() {

  const permissions = localStorage.getItem('permissions')
  const [ anno, setAnno ] = useState([]);
  const [ all, setAll ] = useState([]);

  useEffect(() => {
    fetch('http://127.0.0.1:8000')
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

  useEffect(() => {
    fetch('http://127.0.0.1:8000/superadmin')
      .then((response) => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then((data) => {
        console.log(data);
        setAll(data);
      })
      .catch((error) => {
        console.error('Error fetching data:', error);
      });
  }, []);

  const [connected, setConnected] = useState(false);
  const [register, setRegister] = useState(false);
  const [approved, setApproved] = useState(false)

  const handleConnexion = () => {
    setConnected(true);
  };

  const handleInscription = () => {
    setRegister(true);
  };

  const handleApproved = () => {
    setApproved(true);
    setRegister(false);
    setConnected(false);
  };

  const [activeSection, setActiveSection] = useState(0);
  const [displayModAnn, setDisplayModAnn] = useState(null);

  const handleButton = (num) => {
    setActiveSection(num);
};

const handleClick = (index) => {
  setDisplayModAnn(index);
};

  return (
    <div className="App">
      {!connected && !register && !approved ? (
        <Connexion connect={handleConnexion} connect2={handleInscription}/>
      ) : (
        <>
          {register && !connected ? <Inscription onApproved={handleApproved}/> : null}
          {!register && connected ? <Connexion2 onApproved={handleApproved}/> : null}
          {approved && (
            <>
              <Pannel/>
              {permissions === '3' ? (
                <div className="grid-container1">
                  <Button num="B1" label="Users" onClick={() => handleButton(0)} />
                  <Button num="B2" label="Advertisements" onClick={() => handleButton(1)} />
                  <Button num="B3" label="Job Applications" onClick={() => handleButton(2)} />
                  <Button num="B4" label="Companies" onClick={() => handleButton(3)} />
                  {activeSection === 0 &&
                    <table className='tableau'>
                      <thead>
                        <tr>
                          <th>ID</th>
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
                      {all[0].map((item, index) => (
                        <tr key={index}>
                          <td>{item.id}</td>
                          <td>{item.surname}</td>
                          <td>{item.first_name}</td>
                          <td>{item.username}</td>
                          <td>{item.password}</td>
                          <td>{item.email}</td>
                          <td>{item.permissions}</td>
                          <td>{item.companies}</td>
                        </tr>
                      ))}
                      </tbody>
                    </table>
                  }
                  {activeSection === 1 &&
                    <table className='tableau'>
                      <thead>
                        <tr>
                          <th>ID</th>
                          <th>Title</th>
                          <th>Description</th>
                          <th>Employer</th>
                          <th>Company</th>
                        </tr>
                      </thead>
                      <tbody>
                      {all[1].map((item, index) => (
                        <tr key={index}>
                          <td>{item.id}</td>
                          <td>{item.title}</td>
                          <td>{item.description}</td>
                          <td>{item.cmp}</td>
                          <td>{item.companies}</td>
                        </tr>
                      ))}
                      </tbody>
                    </table>
                  }
                  {activeSection === 2 &&
                    <table className='tableau'>
                      <thead>
                        <tr>
                          <th>ID</th>
                          <th>Advertisement</th>
                          <th>Candidate</th>
                          <th>Last Name</th>
                          <th>First Name</th>
                          <th>Email</th>
                        </tr>
                      </thead>
                      <tbody>
                      {all[2].map((item, index) => (
                        <tr key={index}>
                          <td>{item.id}</td>
                          <td>{item.advert}</td>
                          <td>{item.applicant}</td>
                          <td>{item.surname}</td>
                          <td>{item.first_name}</td>
                          <td>{item.email}</td>
                          <td class="btn2" onClick={() => handleClick(index)}>Modify</td>
                          {displayModAnn === index && <Modify form={item} labels={["id","advert","applicant","surname","first_name","eamil"]} fermer={() => setDisplayModAnn(null)} />}
                        </tr>
                      ))}
                      </tbody>
                    </table>
                  }
                  {activeSection === 3 &&
                    <table className='tableau'>
                      <thead>
                        <tr>
                          <th>ID</th>
                          <th>Name</th>
                        </tr>
                      </thead>
                      <tbody>
                      {all[3].map((item, index) => (
                        <tr key={index}>
                          <td>{item.id}</td>
                          <td>{item.name}</td>
                        </tr>
                      ))}
                      </tbody>
                    </table>
                  }
                </div>
              ) : (
                  <ul>
                    {anno.length > 0 ? (
                    anno.map((item, index) => (
                      <li key={index}>
                        <Content id={item.id} title={item.title} text={item.description} comp={item.companies}/>
                      </li>
                    ))
                    ) : (
                      <p>No advertisements for the moment</p>
                    )}
                  </ul>
              )}
            </>
          )}
        </>
      )}
    </div>
  );
}

export default App;
