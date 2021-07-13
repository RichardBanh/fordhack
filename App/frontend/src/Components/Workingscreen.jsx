import React, { useEffect, useState } from "react";
import { GoogleMap, LoadScript, Marker } from "@react-google-maps/api";
import { ListBlk } from "./ListBlk";
import { useDispatch, useSelector } from "react-redux";
import { Modal } from "./Modal";
const containerStyle = {
  width: "40vw",
  height: "100vh",
};

//user settings home profile
const center = {
  lat: 42.3,
  lng: -83.205,
};

export const WorkingScreen = () => {
  const dispatch = useDispatch();
  const carlist = useSelector((state) => state.CarList.carlist);
  const locations = useSelector((state) => state.CarLocation.locations);
  const [openModal, setModal] = useState(false);
  const [id, setModalId] = useState({});
  useEffect(() => {
    dispatch({
      type: "GET/LIST/MIDDLEWARE",
      payload: { url: "http://127.0.0.1:8000/carlist/", method: "POST" },
    });
  }, []);

  const listCars = carlist.map((x, index) => (
    <ListBlk
      data={x}
      index={index}
      dispatch={dispatch}
      key={index}
      setModal={setModal}
      setModalId={setModalId}
    />
  ));

  const markers = locations.map((x, index) => (
    <Marker
      index={index}
      key={index}
      position={{ lat: parseFloat(x.latitude), lng: parseFloat(x.longitude) }}
    ></Marker>
  ));

  return (
    <>
      {openModal ? <Modal id={id} dispatch={dispatch} /> : <div></div>}
      <div className="content">
        <div className="side_left">
          <div className="menubar">
            <div>Logo</div>
            <div className="accountType">Account Class: Admin</div>
            <div>Settings</div>
            <div>Security Console</div>
            <div>Log Out</div>
          </div>
          {carlist.length > 0 ? listCars : <div>Loading</div>}
        </div>
        <div className="side_right">
          <LoadScript googleMapsApiKey="AIzaSyDjmq8FIkvICMQwQIVlx2pzZ_IbY-tBeG0">
            <GoogleMap
              mapContainerStyle={containerStyle}
              center={center}
              zoom={17}
            >
              {markers}
            </GoogleMap>
          </LoadScript>
        </div>
      </div>
    </>
  );
};
