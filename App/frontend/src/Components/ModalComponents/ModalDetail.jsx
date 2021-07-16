import React, { useEffect } from "react";
import { useSelector } from "react-redux";

export const ModalDetail = (props) => {
  const {
    color,
    engineType,
    lastUpdated,
    modelName,
    modelYear,
    modemEnabled,
    nickName,
    vehicleId,
  } = props.modalDetail;

  const { batteryChargeLevel, fuelLevel, mileage, odometer } =
    props.modalDetail.vehicleDetails;

  return (
    <>
      <div className="detail">
        <div>
          <div>
            <div className="title">Car Id</div>
            <div className="stats">{vehicleId}</div>
          </div>
          <div>
            <div className="title">Nickname</div>
            <div className="stats">{nickName}</div>
          </div>
          <div>
            <div className="title">Model Year</div>
            <div className="stats">{modelYear}</div>
          </div>
          <div>
            <div className="title">Model Name</div>
            <div className="stats">{modelName}</div>
          </div>
          <div>
            <div className="title">Engine Type</div>
            <div className="stats">{engineType}</div>
          </div>
          <div>
            <div className="title">Last Updated</div>
            <div className="stats">{lastUpdated}</div>
          </div>
          <div>
            <div className="title">Connection on</div>
            <div className="stats">{"" + modemEnabled} </div>
          </div>
          <div>
            <div className="title">Color</div>
            <div className="stats">{color}</div>
          </div>
          <div>
            <div className="title">Odometer</div>
            <div className="stats">{odometer} Miles</div>
          </div>
        </div>
        <div>
          <div>
            <div className="title">Battery Milage to Empty</div>
            <div className="stats">
              {batteryChargeLevel.distanceToEmpty} Miles Availible
            </div>
          </div>
          <div>
            <div className="title">Amount of Charge</div>
            <div className="stats">{batteryChargeLevel.value} KWH</div>
          </div>
          <div>
            <div className="title">Gas Milage to Empty</div>
            <div className="stats">
              {fuelLevel.distanceToEmpty} Miles Availible
            </div>
          </div>
          <div>
            <div className="title">Amount of Gas</div>
            <div className="stats">{fuelLevel.value} Gallons</div>
          </div>
          <div>
            <div className="title">Mileage for Trip</div>
            <div className="stats">{mileage} Miles</div>
          </div>
          <div>
            <div className="title">Odometer</div>
            <div className="stats">{odometer} Miles</div>
          </div>
        </div>
      </div>
    </>
  );
};
