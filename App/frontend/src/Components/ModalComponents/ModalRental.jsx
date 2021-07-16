import React, { useEffect } from "react";
import { useSelector } from "react-redux";
import { ModalCreate } from "./ModalRentForm";
export const ModalRental = (props) => {
  const rented = useSelector((state) => state.ModalData.modalRental);
  let component = <></>;
  return (
    <>
      <div>
        <div>Currently Rented</div>
        {rented === null || rented === undefined ? (
          //   <div>Loading</div>
          <ModalCreate />
        ) : (
          component
        )}
      </div>
      <div></div>
    </>
  );
};
