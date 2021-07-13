import React, { useState } from "react";
import { useSelector } from "react-redux";
import bell from "../Assets/bell.svg";
import menu from "../Assets/menu.svg";
import sliders from "../Assets/sliders.svg";
import trending from "../Assets/trending.svg";
import { ModalDetail } from "../../src/Components/ModalComponents/ModalDetail";

import { ModalCommand } from "./ModalComponents/ModalCommand";

export const Modal = (props) => {
  const modalDetail = useSelector((state) => state.ModalData.modalDetail);
  const modalLocation = useSelector((state) => state.CarLocation.locations);
  console.log(modalLocation);
  const [showCommand, setShow] = useState("modalDetail");
  let component = <></>;

  switch (showCommand) {
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

    default:
      break;
  }
  return (
    <div className="modal">
      <div className="modal-content">
        <menu>
          <button>
            <img src={bell} />
          </button>
          <button onClick={() => setShow("modalDetail")}>
            <img src={menu} />
          </button>
          <button onClick={() => setShow("modalCommand")}>
            <img src={sliders} />
          </button>
          <button>
            <img src={trending} />
          </button>
        </menu>

        {modalDetail === null || modalDetail === undefined ? (
          <div>Loading</div>
        ) : (
          component
        )}
      </div>
    </div>
  );
};
