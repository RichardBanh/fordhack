import React, { useEffect } from "react";
import { useSelector } from "react-redux";

export const ModalDetail = (props) => {
  const {
    color,
    engineType,
    lastUpdated,
    modelName,
    modelYear,
    modemEnabled,
    nickName,
    vehicleId,
  } = props.modalDetail;
  return (
    <>
      <div>Car Id: {vehicleId}</div>
      <div>Nickname: {nickName}</div>
      <div>Model Year: {modelYear}</div>
      <div>Model Name: {modelName}</div>
      <div>Engine Type: {engineType}</div>
      <div>Last Updated: {lastUpdated}</div>
      <div>Connection on: {"" + modemEnabled} </div>
      <div>Color: {color}</div>
    </>
  );
};
