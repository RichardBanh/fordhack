import React, { useState } from "react";

export const Signup = (props) => {
  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [phone, setPhone] = useState("");
  const [pass, setPass] = useState("");
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
            type="text"
            placeholder="Password"
            onChange={(e) => {
              setPass(e.target.value);
            }}
          />
          <div>Account Type</div>
          <select name="Account_Type" id="Account_Type">
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
        </form>
      </div>
    </>
  );
};
