import React, { Component } from "react";

import { useSelector } from "react-redux";
export const Notification = (props) => {
  const message = useSelector((state) => state.NotificationReducer.message);
  return (
    <div>
      <button
        onClick={() => {
          props.dispatch({ type: "NOTIFICATION/OFF" });
        }}
      >
        Close
      </button>
      <div className="modal-content">{message}</div>
    </div>
  );
};
