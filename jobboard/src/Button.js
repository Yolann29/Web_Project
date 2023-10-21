import React from "react";

const Button = ({ num, label, onClick }) => {
  return (
    <button className={`btn2 ${num}`} onClick={onClick}>
      {label}
    </button>
  );
}

export default Button;