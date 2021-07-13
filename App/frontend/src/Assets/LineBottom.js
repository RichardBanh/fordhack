import React from "react";

export const LineBottom = (props) => {
  let style = "";
  if (props.class === "rightsid") {
    style = props.class;
  } else {
    style = "";
  }
  return (
    <svg
      width="5px"
      height="47px"
      viewBox="0 0 5 47"
      version="1.1"
      className={style}
    >
      <g
        id="Page-1"
        stroke="none"
        stroke-width="1"
        fill="none"
        fill-rule="evenodd"
        stroke-linecap="square"
      >
        <g
          id="Desktop"
          transform="translate(-215.000000, -289.000000)"
          stroke={props.color}
          stroke-width="3"
        >
          <line x1="217" y1="291" x2="217.5" y2="333.5" id="Line"></line>
        </g>
      </g>
    </svg>
  );
};
