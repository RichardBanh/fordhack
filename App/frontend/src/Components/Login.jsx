import React, { useState } from "react";
import { useDispatch } from "react-redux";
import { loginFetch } from "../Fetch-cookie/loginFetch";
import { Signup } from "./Signup";
export const Login = () => {
  const dis = useDispatch();
  const [userName, setUsername] = useState("");
  const [password, setPass] = useState("");
  const [showSignup, setSign] = useState(false);
  return (
    <>
      {showSignup ? (
        <Signup setSign={setSign} />
      ) : (
        <div className="loginWrapper">
          <form className="loginForm">
            <div>Username</div>
            <input
              type="text"
              placeholder="Username"
              onChange={(e) => {
                setUsername(e.target.value);
              }}
            />
            <div>Password</div>
            <input
              type="password"
              placeholder="Password"
              onChange={(e) => {
                setPass(e.target.value);
              }}
            />
            <button
              onClick={async (e) => {
                e.preventDefault();
                loginFetch(
                  { username: userName, password: password },
                  dis,
                  "SIGNIN",
                  { username: userName, signin: true }
                );
              }}
            >
              Login
            </button>
            <button
              onClick={() => {
                setSign(true);
              }}
            >
              Sign up!
            </button>
          </form>
        </div>
      )}
    </>
  );
};
