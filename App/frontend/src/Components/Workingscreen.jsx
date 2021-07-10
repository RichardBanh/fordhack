import React, { useEffect } from "react";
import { GoogleMap, LoadScript, Marker } from "@react-google-maps/api";
import { ListBlk } from "./ListBlk";
import { useDispatch, useSelector } from "react-redux";

const containerStyle = {
  width: "40vw",
  height: "100vh",
};

const center = {
  lat: -3.745,
  lng: -38.523,
};
export const WorkingScreen = () => {
  const dispatch = useDispatch();
  const carlist = useSelector((state) => state.CarList.carlist);
  useEffect(() => {
    dispatch({
      type: "GET/LIST/MIDDLEWARE",
      payload: { url: "http://127.0.0.1:8000/carlist/", method: "POST" },
    });
  }, []);
  //add load

  const listCars = carlist.map((x) => <ListBlk data={x} />);
  return (
    <>
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
              zoom={10}
            >
              <Marker position={{ lat: -3.745, lng: -38.523 }}></Marker>
              <></>
            </GoogleMap>
          </LoadScript>
        </div>
      </div>
    </>
  );
};
