import React, { useState, useCallback } from "react";
import response from "../Assets/response.png";
import { GoogleMap, LoadScript, Marker } from "@react-google-maps/api";
//auto save function?
const containerStyle = {
  width: "40vw",
  height: "100vh",
};

const center = {
  lat: -3.745,
  lng: -38.523,
};
export const WorkingScreen = () => {
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
          <div className="rec_blk">
            <img className="image_sq" src={response} />
            <div className="info">
              <div>Car Id:</div>
              <div className="stats">9u9392091</div>
            </div>
            <div className="info">
              <div>Model:</div>
              <div className="stats">Edge</div>
            </div>
            <div className="info">
              <div>Model Year:</div>
              <div className="stats">2019</div>
            </div>
            <div className="info">
              <div>Color:</div>
              <div className="stats">Oxford White</div>
            </div>
            <div className="info">
              <div>Engine Type:</div>
              <div className="stats">ICE</div>
            </div>
            <div className="info">
              <div>Fuel Level:</div>
              <div className="stats">-5.0</div>
            </div>
            <div className="info">
              <div>Odometer:</div>
              <div className="stats">600</div>
            </div>
            <div className="info">
              <div>Location:</div>
              <div className="stats">Rental Lot</div>
            </div>
            <div className="info">
              <div>Rental Status:</div>
              <div className="stats">Home</div>
            </div>
            <div className="button_center">
              <button className="ren">Rental</button>
              <button className="req">Request</button>
              <button className="req">Notifications</button>
            </div>
          </div>
          <div className="rec_blk"></div>
          <div className="rec_blk"></div>
          <div className="rec_blk"></div>
          <div className="rec_blk"></div>
          <div className="rec_blk"></div>
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
