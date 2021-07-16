import React, { useState } from "react";
import { notification } from "../../NotificationFunction";
import { useDispatch, useSelector } from "react-redux";

export const ModalCreate = () => {
  const [showInfo, setShow] = useState(false);
  const [phone, setPhone] = useState("");
  const [startDate, setSDate] = useState("");
  const [endDate, setEDate] = useState("");
  const [mile, setMile] = useState("");
  const dispatch = useDispatch();
  const vehicleId = useSelector(
    (state) => state.ModalData.modalDetail.vehicleId
  );
  const onSub = () => {
    console.log(vehicleId);
    const date1 = new Date(startDate);
    const date2 = new Date(endDate);
    const diffTime = Math.abs(date2 - date1);
    const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24));
    const raw = {
      vehicleId: vehicleId,
      rental_length_days: diffDays + "",
      rental_by_phone: phone,
      rental_mile_limits: mile,
    };
    const stringified = JSON.stringify(raw);
    console.log(stringified);
    notification(
      "http://127.0.0.1:8000/rent/",
      "POST",
      true,
      stringified,
      true,
      dispatch,
      "OK"
    );
  };
  return (
    <div>
      <form
        onSubmit={(e) => {
          e.preventDefault();
          onSub();
        }}
      >
        <div>
          Start Date:
          <input
            type="date"
            onChange={(e) => {
              setSDate(e.target.value);
            }}
          />
        </div>
        <div>
          End Date:
          <input
            type="date"
            onChange={(e) => {
              setEDate(e.target.value);
            }}
          />
        </div>
        <div>
          Renter's Phone
          <input
            id="telNo"
            name="telNo"
            type="tel"
            required
            pattern="[0-9]{11}"
            placeholder="17789527551"
            value={phone}
            onChange={(e) => setPhone(e.target.value)}
          />
          <span class="validity"></span>
        </div>
        <div>
          Mile limits:
          <input
            type="number"
            onChange={(e) => {
              setMile(e.target.value);
            }}
          />
        </div>
        <button>Submit</button>
      </form>
    </div>
  );
};
