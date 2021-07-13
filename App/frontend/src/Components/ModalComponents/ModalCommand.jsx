import React from "react";
import CarDoors from "../../Assets/CarDoors.svg";

import { LineBottom } from "../../Assets/LineBottom";
import { LineTop } from "../../Assets/LineTop";
import { notification } from "../../NotificationFunction";

const determineCloseDoor = (array) => {
  const closed = array.find(({ value }) => value === "Open");

  if (closed === undefined) {
    return false;
  } else {
    return true;
  }
};

export const ModalCommand = (props) => {
  const { vehicleId, modemEnabled } = props.modalDetail;

  const {
    ignitionStatus,
    remoteStartStatus,
    tirePressureWarning,
    doorStatus,
    firmwareUpgradeInProgress,
  } = props.modalDetail.vehicleStatus;

  const { speed, direction } = props.modalLocation[0];

  const open = determineCloseDoor(doorStatus);

  let driverDoor = "";
  let passRightDoor = "";
  let passLeftBottomDoor = "";
  let passRearRight = "";

  if (doorStatus[0].value === "CLOSED") {
    driverDoor = "#c21c03";
  } else {
    driverDoor = "#45F54A";
  }
  if (doorStatus[1].value === "CLOSED") {
    passRightDoor = "#c21c03";
  } else {
    passRightDoor = "#45F54A";
  }
  if (doorStatus[3].value === "CLOSED") {
    passLeftBottomDoor = "#c21c03";
  } else {
    passLeftBottomDoor = "#45F54A";
  }
  if (doorStatus[4].value === "CLOSED") {
    passRearRight = "#c21c03";
  } else {
    passRearRight = "#45F54A";
  }

  return (
    <>
      <div className="modal-command-blk">
        <div className="modal-command">
          <button
            onClick={() => {
              const raw = { action: "UNLOCK/VEHICLE", vehicleId: vehicleId };
              const stringified = JSON.stringify(raw);
              notification(
                "http://127.0.0.1:8000/fleetcommand/",
                "POST",
                true,
                stringified,
                true,
                props.dispatch,
                "UNLOCKED"
              );
            }}
          >
            Unlock Doors
          </button>
          <button
            onClick={() => {
              const raw = { action: "LOCK/VEHICLE", vehicleId: vehicleId };
              const stringified = JSON.stringify(raw);
              notification(
                "http://127.0.0.1:8000/fleetcommand/",
                "POST",
                true,
                stringified,
                true,
                props.dispatch,
                "UNLOCKED"
              );
            }}
          >
            Lock Doors
          </button>
          <button
            onClick={() => {
              const raw = { action: "WAKE/VEHICLE", vehicleId: vehicleId };
              const stringified = JSON.stringify(raw);
              notification(
                "http://127.0.0.1:8000/fleetcommand/",
                "POST",
                true,
                stringified,
                true,
                props.dispatch,
                "UNLOCKED"
              );
            }}
          >
            Wake Vehicle Modem
          </button>
          <div>
            <div>Emergency Engine Turn Off</div>
            <input type="text" name="" id="" />
            <button>Request Turn Off</button>
          </div>
          <div>
            <div>Send Request to Supervisor Phone Number</div>
            <input type="text" name="" id="" />
            <button>Request Turn Off</button>
          </div>
          <div>
            <div>Ok Engine Turn Off</div>
            <input type="text" name="" id="" />
            <button>Request Turn Off</button>
          </div>
        </div>
        <div className="modal-command-info">
          <div className="doors">
            <div>Doors</div>
            <div>
              {open ? (
                <div className="command-open">Open</div>
              ) : (
                <div className="command-closed">Closed</div>
              )}
            </div>
          </div>
          <div className="car">
            <div className="left">
              <LineTop color={driverDoor} />
              <LineBottom color={passLeftBottomDoor} />
            </div>
            <img src={CarDoors} alt="" className="command-car-diagram" />
            <div className="rightside">
              <LineTop class="rightsid" color={passRightDoor} />
              <LineBottom color={passRearRight} />
            </div>
          </div>
          <div>Vehicle Status</div>
          <div>
            Ignition Status: {ignitionStatus.value} @ {ignitionStatus.timeStamp}
            <br />
            Firmware Being Upgraded: {"" + firmwareUpgradeInProgress}
            <br />
            Tire Pressure Warning: {"" + tirePressureWarning}
          </div>
          <div>
            Location: {props.modalLocation[0].googleLocation.formatted_address}
          </div>
          <div>Speed: {speed}</div>
          <div>Direction: {direction}</div>
          <div>Vehicle Modem Connected: {"" + modemEnabled}</div>
        </div>
      </div>
    </>
  );
};
