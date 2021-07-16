import React, { useEffect, useState } from "react";
import { useSelector } from "react-redux";
import { ModalCreate } from "./ModalRentForm";
import { ModalRentalList } from "./ModalRentalList";
import { fetchfun } from "../../FetchFunction";
import { ModalRentEdit } from "./ModalRentalEdit";

export const ModalRental = (props) => {
  const [load, setLoad] = useState(false);
  const [rent, setRented] = useState(false);
  const vehicleId = useSelector(
    (state) => state.ModalData.modalDetail.vehicleId
  );

  useEffect(() => {
    const url = `http://127.0.0.1:8000/rent/${vehicleId}/`;
    fetchfun(url, "GET", false, null, true)
      .then((res) => res.json())
      .then((res) => {
        console.log(res);
        const { active_Rent } = res;
        if (active_Rent === true) {
          const {
            rental_by_phone,
            rental_length_days,
            rental_miles_limits,
            req_date,
          } = res;
          setRented(true);
        }
        setLoad(true);
      });
  }, []);

  return (
    <>
      <div>
        {load ? (
          <>{rent ? <ModalRentalList /> : <ModalCreate />}</>
        ) : (
          <div>Loading</div>
        )}
      </div>
      <div></div>
    </>
  );
};
