import React, { useEffect, useState } from "react";
import { useSelector } from "react-redux";
import { ModalCreate } from "./ModalRentForm";
import { ModalRentalList } from "./ModalRentalList";
import { fetchfun } from "../../FetchFunction";
import { ModalRentEdit } from "./ModalRentalEdit";

export const ModalRental = (props) => {
  const [load, setLoad] = useState(false);
  const [rent, setRented] = useState(false);
  const [resp, setResp] = useState({});
  const vehicleId = useSelector(
    (state) => state.ModalData.modalDetail.vehicleId
  );

  const fetch = () => {
    const url = `http://127.0.0.1:8000/rent/${vehicleId}/`;
    fetchfun(url, "GET", false, null, true)
      .then((res) => res.json())
      .then((res) => {
        const { active_Rent } = res;
        if (active_Rent === true) {
          setResp(res);
          setRented(true);
        }
        setLoad(true);
      });
  };

  useEffect(() => {
    fetch();
  }, []);

  return (
    <>
      <div>
        {load ? (
          <>
            {rent ? (
              <ModalRentalList
                resp={resp}
                vehicleId={vehicleId}
                setRented={setRented}
                setResp={setResp}
                fetch={fetch}
              />
            ) : (
              <ModalCreate setRented={setRented} fetch={fetch} />
            )}
          </>
        ) : (
          <div>Loading</div>
        )}
      </div>
    </>
  );
};
