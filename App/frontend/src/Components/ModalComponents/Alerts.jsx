import React, { useState, useEffect } from "react";
import { fetchfun } from "../../FetchFunction";
export const Alert = (props) => {
  const [load, setLoad] = useState(false);
  const [alerts, setAlert] = useState([]);

  useEffect(() => {
    const raw = { action: "ONE/NOTIFICATIONS", vehicleId: props.vehicleId };
    const stringify = JSON.stringify(raw);
    fetchfun(
      "http://127.0.0.1:8000/notifcations/",
      "POST",
      true,
      stringify,
      true
    )
      .then((res) => {
        res.json();
      })
      .then((res) => {
        setAlert(res);
        setLoad(true);
      });
  }, []);

  const alertComp = () => {
    alerts.forEach((x) => (
      <div>
        <div>
          Message Type:
          <div>{x.messageType}</div>
        </div>
        <div>
          Message:
          <div>{x.message}</div>
        </div>
      </div>
    ));
  };
  return load ? alertComp : <div>Loading</div>;
};
