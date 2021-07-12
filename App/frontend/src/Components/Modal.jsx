import React, { useEffect } from "react";
import { useSelector } from "react-redux";
import bell from "../Assets/bell.svg";
import menu from "../Assets/menu.svg";
import sliders from "../Assets/sliders.svg";
import trending from "../Assets/trending.svg";
import { ModalDetail } from "../../src/Components/ModalComponents/ModalDetail";

export const Modal = (props) => {
  const modalDetail = useSelector((state) => state.ModalData.modalDetail);
  return (
    <div className="modal">
      <div className="modal-content">
        <menu>
          <button>
            <img src={bell} />
          </button>
          <button>
            <img src={menu} />
          </button>
          <button>
            <img src={sliders} />
          </button>
          <button>
            <img src={trending} />
          </button>
        </menu>

        {modalDetail === null || modalDetail === undefined ? (
          <div>Loading</div>
        ) : (
          <ModalDetail modalDetail={modalDetail} />
        )}
      </div>
    </div>
  );
};
