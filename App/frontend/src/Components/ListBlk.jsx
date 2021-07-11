import React, { useEffect, useState } from "react";
import response from "../Assets/response.png";
import { fetchfun } from "../FetchFunction";
import { Location } from "./Location";
function truncate(str, n) {
  return str.length > n ? str.substr(0, n - 1) : str;
}

export const ListBlk = (props) => {
  const shortenId = truncate(props.data.vehicleId, 7);
  const [coord, setCoord] = useState({});
  const [detailed, setDetailed] = useState({});

  useEffect(() => {
    const raw = JSON.stringify({
      type: "ONE/DETAIL",
      vehicleId: props.data.vehicleId,
    });
    fetchfun("http://127.0.0.1:8000/carlist/", "POST", true, raw, true)
      .then((res) => {
        return res.json();
      })
      .then((response) => {
        setCoord(response.vehicle.vehicleLocation);
        setDetailed(response);
      });
  }, []);

  return (
    <div className="rec_blk">
      <img className="image_sq" src={response} />
      <div className="info">
        <div>Car Id:</div>
        <div className="stats">{shortenId}</div>
      </div>
      <div className="info">
        <div>Model:</div>
        <div className="stats">{props.data.modelName}</div>
      </div>
      <div className="info">
        <div>Model Year:</div>
        <div className="stats">{props.data.modelYear}</div>
      </div>
      <div className="info">
        <div>Color:</div>
        <div className="stats">{props.data.color}</div>
      </div>
      <div className="info">
        <div>Modem Connection On:</div>
        <div className="stats">{"" + props.data.modemEnabled}</div>
      </div>
      <div className="info">
        <div>Location:</div>
        {coord.longitude !== undefined ? (
          <Location coord={coord} />
        ) : (
          <div>Loading</div>
        )}
      </div>
      <div className="button_center">
        <button className="ren">Detail</button>
        <button className="ren">Rental</button>
        <button className="req">Request</button>
        <button className="req">Notifications</button>
      </div>
    </div>
  );
};

//location fetch call here

{
  /* <div className="info">
        <div>Engine Type:</div>
        <div className="stats">ICE</div>
      </div>
      <div className="info">
        <div>Fuel Level:</div>
        <div className="stats">-5.0</div>
      </div>
      <div className="info">
        <div>Odometer:</div>
        <div className="stats">600</div>
      </div>
      <div className="info">
        <div>Location:</div>
        <div className="stats">Rental Lot</div>
      </div>
      <div className="info">
        <div>Rental Status:</div>
        <div className="stats">Home</div>
      </div> */
}
