import React, { useState } from "react";
import { useDispatch } from "react-redux";
import { fetchfun } from "../FetchFunction";
import { loginFetch } from "../Redux/Middleware/loginFetch";
import { Signup } from "./Signup";
import { storeCookieJWT } from "../CookieFunctions/Cookie";
export const Login = (props) => {
  const dispatch = useDispatch();
  const [userName, setUsername] = useState("");
  const [password, setPass] = useState("");
  const [showSignup, setSign] = useState(false);
  const login = () => {
    const raw = { username: userName, password: password };
    fetchfun(
      "http://127.0.0.1:8000/token/",
      "POST",
      true,
      JSON.stringify(raw),
      false
    )
      .then((res) => res.json())
      .then((res) => {
        props.setJwt(res.access);
        storeCookieJWT("refresh", "jwt", res);
      })
      .catch((res) => {
        console.log(res);
      });
  };
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
              onClick={(e) => {
                e.preventDefault();
                login();
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
