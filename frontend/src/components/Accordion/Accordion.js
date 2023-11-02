import React, { useEffect, useRef, useState } from "react";
import burgerMenu from '../../assets/icons/Group 2340.svg'
import "./accordion.css";

function Accordion(props) {
  const [active, setActive] = useState(false);
  const content = useRef(null);
  const [height, setHeight] = useState("0px");

  useEffect(() => {
  }, [height]);

  function toggleAccordion() {
    setActive(!active);
    setHeight(active ? "0px" : `${content.current.scrollHeight}px`);
  }

  return (
    <div className="accordion__section">
      <div
        className={`accordion ${active ? "active" : ""}`}
        onClick={toggleAccordion}
      >
        <p className="accordion__title">{props.title}</p>
        <span style={{ marginLeft: "20px" }}><img src={burgerMenu} alt="menu"/></span>
      </div>
      <div
        ref={content}
        style={{ maxHeight: `${height}` }}
        className="accordion__content"
      >
        <div
        // className="accordion__text"
        >{props.content}</div>
      </div>     
    </div>
  );
}

export default Accordion;