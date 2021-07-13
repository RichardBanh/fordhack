import React, { useEffect, useState } from "react";
import { fetchfun } from "../FetchFunction";
export const Location = (props) => {
  const [street, setStreet] = useState("");
  useEffect(() => {
    const long = props.coord.longitude;
    const lat = props.coord.latitude;
    const url = `https://maps.googleapis.com/maps/api/geocode/json?latlng=${lat},${long}&key=AIzaSyDjmq8FIkvICMQwQIVlx2pzZ_IbY-tBeG0`;
    fetchfun(url, "GET", null, false, false)
      .then((res) => res.json())
      .then((res) => {
        setStreet(res.results[0].address_components[1].long_name);
        props.dispatch({
          type: "ADD/STREET/INFO",
          payload: { googleLocation: res.results[0], id: props.id },
        });
        console.log(res.results[0]);
      });
  }, []);
  return (
    <>
      {street === undefined ? (
        <div>Loading</div>
      ) : (
        <div className="stats">{street}</div>
      )}
    </>
  );
};
