import React, { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { fetchfun } from "../../FetchFunction";
export const ModalRentalList = (props) => {
  const { rental_by_phone, rental_length_days, rental_mile_limits, req_date } =
    props.resp;
  const [edit, setEdit] = useState(false);
  const [phone, setPhone] = useState("");
  const [days, setDays] = useState("");
  const [mile, setMile] = useState("");
  const dispatch = useDispatch();

  const compareFunc = () => {
    if (phone != rental_by_phone) {
      let raw = {
        vehicleId: props.vehicleId,
        action: "CHANGE/PHONE",
        rental_by_phone: phone,
      };
      let stringified = JSON.stringify(raw);
      fetchfun("http://127.0.0.1:8000/rent/", "PUT", true, stringified, true)
        .then((res) => {
          return res.json();
        })
        .then((response) => {
          if (typeof response === "string") {
            dispatch({
              type: "NOTIFICATION/ON",
              payload: { message: response },
            });
            props.setRented(true);
            props.fetch();
          } else {
            dispatch({
              type: "NOTIFICATION/ON",
              payload: { message: "Ford Request Failed" },
            });
          }
        });
    }
    if (days != rental_length_days) {
      let raw = {
        vehicleId: props.vehicleId,
        action: "CHANGE/DAYS",
        rental_length_days: days,
      };
      let stringified = JSON.stringify(raw);
      fetchfun("http://127.0.0.1:8000/rent/", "PUT", true, stringified, true)
        .then((res) => {
          return res.json();
        })
        .then((response) => {
          if (typeof response === "string") {
            dispatch({
              type: "NOTIFICATION/ON",
              payload: { message: response },
            });
            props.setRented(true);
            props.fetch();
          } else {
            dispatch({
              type: "NOTIFICATION/ON",
              payload: { message: "Ford Request Failed" },
            });
          }
        });
    }
    if (mile != rental_mile_limits) {
      let raw = {
        vehicleId: props.vehicleId,
        action: "CHANGE/DAYS",
        rental_mile_limits: mile,
      };
      let stringified = JSON.stringify(raw);
      fetchfun("http://127.0.0.1:8000/rent/", "PUT", true, stringified, true)
        .then((res) => {
          return res.json();
        })
        .then((response) => {
          if (typeof response === "string") {
            dispatch({
              type: "NOTIFICATION/ON",
              payload: { message: response },
            });
            props.setRented(true);
            props.fetch();
          } else {
            dispatch({
              type: "NOTIFICATION/ON",
              payload: { message: "Ford Request Failed" },
            });
          }
        });
    }
  };
  const endRental = () => {
    const raw = {
      action: "FINISH/RENT",
      vehicleId: props.vehicleId,
    };
    const stringified = JSON.stringify(raw);
    fetchfun("http://127.0.0.1:8000/rent/", "PUT", true, stringified, true)
      .then((res) => res.json())
      .then((res) => {
        dispatch({
          type: "NOTIFICATION/ON",
          payload: { message: res },
        });
        props.setRented(false);
        props.setResp({});
      });
  };
  useEffect(() => {
    setPhone(rental_by_phone);
    setDays(parseInt(rental_length_days));
    setMile(parseInt(rental_mile_limits));
  }, []);
  return (
    <div>
      {edit ? (
        <div>
          <div>
            Phone of renter:{" "}
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
          </div>
          <div>
            Rental days length:
            <input
              type="number"
              value={days}
              onChange={(e) => {
                setDays(e.target.value);
              }}
            />
          </div>
          <div>
            Rental mileage limits:
            <input
              type="number"
              value={mile}
              onChange={(e) => {
                setMile(e.target.value);
              }}
            />
          </div>
          <button
            onClick={() => {
              compareFunc();
            }}
          >
            Submit Edit
          </button>
          <button
            onClick={() => {
              setEdit(false);
            }}
          >
            Exit
          </button>
        </div>
      ) : (
        <div>
          <div>Phone of renter: {rental_by_phone}</div>
          <div>Rental days length: {rental_length_days}</div>
          <div>Rental mileage limits: {rental_mile_limits}</div>
          <div>Rental requested on: {req_date}</div>
          <button
            onClick={() => {
              setEdit(true);
            }}
          >
            Modify Rental
          </button>
          <button
            onClick={() => {
              endRental();
            }}
          >
            End Rental
          </button>
        </div>
      )}
    </div>
  );
};
