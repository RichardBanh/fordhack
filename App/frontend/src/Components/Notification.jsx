import React, { Component } from "react";

import { useSelector } from "react-redux";
export const Notification = () => {
  const message = useSelector((state) => state.NotificationReducer.message);
  return <div className="modal-content">{message}</div>;
};
