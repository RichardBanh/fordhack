import React, { useState, useCallback } from "react";
import response from "../Assets/response.png";

function truncate(str, n) {
  return str.length > n ? str.substr(0, n - 1) : str;
}

export const ListBlk = (props) => {
  const shortenId = truncate(props.data.vehicleId, 7);
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
        <div>Connection On:</div>
        <div className="stats">{"" + props.data.modemEnabled}</div>
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
