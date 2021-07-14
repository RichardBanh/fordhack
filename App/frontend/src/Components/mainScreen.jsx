import React, { useState, useEffect } from "react";
import { BrowserRouter as Router } from "react-router-dom";
import { Login } from "./Login";
import { useSelector } from "react-redux";
import { WorkingScreen } from "./Workingscreen";
import Cookies from "js-cookie";

export const Main = () => {
  const loggedinPass = useSelector((state) => state.Login.signin);
  const [jwt, setJwt] = useState("");
  useEffect(() => {
    const jw = Cookies.get("jwt");
    if (jw === undefined) {
    } else {
      setJwt(jw);
    }
  }, []);
  return (
    <Router>
      {jwt !== "" ? <WorkingScreen jwt={jwt} /> : <Login setJwt={setJwt} />}
    </Router>
  );
};
