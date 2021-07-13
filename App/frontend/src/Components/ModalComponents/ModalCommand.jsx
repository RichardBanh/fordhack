import React, { useState } from "react";
import CarDoors from "../../Assets/CarDoors.svg";

import { LineBottom } from "../../Assets/LineBottom";
import { LineTop } from "../../Assets/LineTop";
export const ModalCommand = (props) => {
  const { vehicleId, modemEnabled } = props.modalDetail;

  const {
    ignitionStatus,
    remoteStartStatus,
    tirePressureWarning,
    doorStatus,
    firmwareUpgradeInProgress,
  } = props.modalDetail.vehicleStatus;

  console.log(ignitionStatus);
  const color = "#c21c03";
  return (
    <>
      <div className="modal-command-blk">
        <div className="modal-command">
          <button>Unlock Doors</button>
          <button>Lock Doors</button>
          <button>Wake Vehicle Modem</button>
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
          <div>
            <div>Doors</div>
            <div>Open</div>
          </div>
          <div className="car">
            <div className="left">
              <LineTop color={color} />
              <LineBottom color={color} />
            </div>

            <img src={CarDoors} alt="" />
            <div className="rightside">
              <LineTop class="rightsid" color={color} />
              <LineBottom color={color} />
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
          <div>Location</div>
          <div>Vehicle Modem: {"" + modemEnabled}</div>
        </div>
      </div>
    </>
  );
};
