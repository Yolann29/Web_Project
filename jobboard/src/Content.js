import './App.css';

function Content(props) {
  return (
    <div className="Content">
        <h1>{props.title}</h1>
        <p>{props.text}</p>
        <button>Learn more</button>
    </div>
  );
}

export default Content;
