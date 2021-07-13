import React from "react";

export const LineTop = (props) => {
  let style = "";
  if (props.class === "rightsid") {
    style = props.class;
  } else {
    style = "";
  }
  return (
    <svg
      width="4px"
      height="57px"
      viewBox="0 0 4 57"
      version="1.1"
      className={style}
    >
      <title>Line</title>
      <desc>Created with Sketch.</desc>
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
          transform="translate(-215.000000, -230.000000)"
          stroke={props.color}
          stroke-width="3"
        >
          <line x1="217" y1="232" x2="217" y2="285" id="Line"></line>
        </g>
      </g>
    </svg>
  );
};
