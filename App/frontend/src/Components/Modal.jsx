import React from "react";
import { useSelector } from "react-redux";
import bell from "../Assets/bell.svg";
import menu from "../Assets/menu.svg";
import sliders from "../Assets/sliders.svg";
import trending from "../Assets/trending.svg";
import { ModalDetail } from "../../src/Components/ModalComponents/ModalDetail";
import { Notification } from "./Notification";

import { ModalCommand } from "./ModalComponents/ModalCommand";
import { ModalRental } from "./ModalComponents/ModalRental";
import { Alert } from "./ModalComponents/Alerts";
import x from "../Assets/x.svg";
export const Modal = (props) => {
  const modalDetail = useSelector((state) => state.ModalData.modalDetail);
  const modalLocation = useSelector((state) => state.CarLocation.locations);
  const showModal = useSelector((state) => state.ModalData.show);

  const notificationShow = useSelector(
    (state) => state.NotificationReducer.notification
  );

  let component = <></>;

  switch (showModal) {
    case "modalDetail":
      component = (
        <ModalDetail modalDetail={modalDetail} modalLocation={modalLocation} />
      );
      break;

    case "modalCommand":
      component = (
        <ModalCommand modalDetail={modalDetail} modalLocation={modalLocation} />
      );
      break;

    case "modalRental":
      component = <ModalRental vehicleId={modalDetail.vehicleId} />;
      break;

    case "modalAlerts":
      component = <Alert vehicleId={modalDetail.vehicleId} />;
      break;

    default:
      break;
  }
  return (
    <div className="modal">
      <div className="modal-content">
        <menu>
          <div>
            <button>
              <img src={bell} />
            </button>
            <button
              onClick={() => {
                props.dispatch({
                  type: "SET/MODAL/SHOW",
                  payload: { showWhat: "modalDetail" },
                });
              }}
            >
              <img src={menu} />
            </button>
            <button
              onClick={() => {
                props.dispatch({
                  type: "SET/MODAL/SHOW",
                  payload: { showWhat: "modalCommand" },
                });
              }}
            >
              <img src={sliders} />
            </button>
            <button
              onClick={() => {
                props.dispatch({
                  type: "SET/MODAL/SHOW",
                  payload: { showWhat: "modalRental" },
                });
              }}
            >
              <img src={trending} />
            </button>
          </div>
          <button
            onClick={() => {
              props.setModal(false);
            }}
          >
            <img src={x} />
          </button>
        </menu>
        {notificationShow ? <Notification dispatch={props.dispatch} /> : <></>}
        {modalDetail === null || modalDetail === undefined ? (
          <div>Loading</div>
        ) : (
          component
        )}
      </div>
    </div>
  );
};
