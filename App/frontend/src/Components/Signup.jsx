import React, { useState } from "react";
import { fetchfun } from "../FetchFunction";

export const Signup = (props) => {
  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [phone, setPhone] = useState("");
  const [pass, setPass] = useState("");
  const [account, setAccount] = useState("");
  return (
    <>
      <div className="loginWrapper signup">
        <form className="loginForm">
          <div>Username</div>
          <input
            type="text"
            placeholder="Username"
            onChange={(e) => {
              setUsername(e.target.value);
            }}
          />
          <div>Email</div>
          <input
            type="text"
            placeholder="Email"
            onChange={(e) => {
              setEmail(e.target.value);
            }}
          />
          <div>Phone Number</div>
          <input
            type="text"
            placeholder="Phone Number"
            onChange={(e) => {
              setPhone(e.target.value);
            }}
          />
          <div>Password</div>
          <input
            type="password"
            placeholder="Password"
            minlength="8"
            required
            onChange={(e) => {
              setPass(e.target.value);
            }}
          />
          <div>Account Type</div>
          <select
            name="Account_Type"
            id="Account_Type"
            value={account}
            onChange={(e) => {
              setAccount(e.target.value);
            }}
          >
            <option value="staff">Staff</option>
            <option value="admin">Admin</option>
          </select>
          <button
            onClick={(e) => {
              props.setSign(false);
            }}
          >
            Close
          </button>
          <button
            onClick={(e) => {
              const raw = {
                username: username,
                password: pass,
                email: email,
                phone_number: phone,
              };
              console.log(account);
              if (account === "staff") {
                raw.is_staff = true;
              } else {
                raw.is_admin = true;
              }
              props.setSign(false);
              fetchfun(
                "http://127.0.0.1:8000/create/",
                "POST",
                true,
                JSON.stringify(raw),
                false
              )
                .then((res) => res.json())
                .then((res) => console.log(res));
            }}
          >
            Submit
          </button>
        </form>
      </div>
    </>
  );
};
