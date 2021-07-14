import React, { useState } from "react";
import { BrowserRouter as Router } from "react-router-dom";
import { Login } from "./Login";
import { useSelector } from "react-redux";
import { WorkingScreen } from "./Workingscreen";
import Cookies from "js-cookie";

export const Main = () => {
  const loggedinPass = useSelector((state) => state.Login.signin);

  return (
    <Router>
      {typeof Cookies.get("jwt") !== "undefined" ? (
        <WorkingScreen />
      ) : (
        <Login />
      )}
    </Router>
  );
};
