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
  const [detailed, setDetailed] = useState(null);

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
        setDetailed(response.vehicle);
        console.log(response);
        response.vehicle.vehicleLocation.id = props.index;
        props.dispatch({
          type: "SET/CARLIST/LOCATION",
          payload: { location: response.vehicle.vehicleLocation },
        });
      });
  }, []);

  const dataDispatch = () => {
    props.dispatch({
      type: "SET/MODAL/DATA/DETAIL",
      payload: { modalDetail: detailed },
    });
  };

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
        <div>Rented:</div>
        <div className="stats">False</div>
      </div>
      <div className="info">
        <div>Location:</div>
        {coord.longitude !== undefined ? (
          <Location coord={coord} id={props.index} dispatch={props.dispatch} />
        ) : (
          <div>Loading</div>
        )}
      </div>
      {detailed === null ? (
        <div></div>
      ) : (
        <div className="button_center">
          <button
            className="ren"
            onClick={() => {
              props.setModal(true);
              props.setModalId(props.index);
              dataDispatch();
              props.dispatch({
                type: "SET/MODAL/SHOW",
                payload: { showWhat: "modalDetail" },
              });
            }}
          >
            Detail
          </button>
          <button
            className="ren"
            onClick={() => {
              props.setModal(true);
              props.setModalId(props.index);
              dataDispatch();
              props.dispatch({
                type: "SET/MODAL/SHOW",
                payload: { showWhat: "modalRental" },
              });
            }}
          >
            Rental
          </button>
          <button
            className="req"
            onClick={() => {
              props.setModal(true);
              props.setModalId(props.index);
              dataDispatch();
              props.dispatch({
                type: "SET/MODAL/SHOW",
                payload: { showWhat: "modalCommand" },
              });
            }}
          >
            Request
          </button>
          <button
            className="req"
            onClick={() => {
              props.setModal(true);
              props.setModalId(props.index);
              dataDispatch();
              props.dispatch({
                type: "SET/MODAL/SHOW",
                payload: { showWhat: "modalAlerts" },
              });
            }}
          >
            Notifications
          </button>
        </div>
      )}
    </div>
  );
};
