import './App.css';

function Offer(props) {
  return (
    <div className="Offer">
      <button onClick={props.fermer}>Back</button>
      <p>{props.text}</p>
      <button onClick={props.fermer}>Apply</button>
    </div>
  );
}

export default Offer;