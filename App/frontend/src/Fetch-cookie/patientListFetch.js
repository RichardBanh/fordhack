import Cookies from "js-cookie";
import axios from "axios";

export const patientFetch = async (dispatch, type) => {
  const url = "http://127.0.0.1:8000/patients/";
  const jwt = Cookies.get("jwt");
  try {
    const response = await axios.get(url, {
      headers: {
        Authorization: `JWT ${jwt}`,
      },
    });
    console.log(response);
    dispatch({ type: type, payload: { all: [...response.data] } });
  } catch (error) {
    console.error(error);
  }
};

export const patientAdd = async (data, dispatch) => {
  const url = "http://127.0.0.1:8000/patients/";
  const jwt = Cookies.get("jwt");
  let lat;
  let long;
  navigator.geolocation.getCurrentPosition(function (position) {
    lat = position.coords.latitude;
    long = position.coords.longitude;
  });
  try {
    const response = await axios.post(
      url,
      {
        ...data,
        latitude: lat,
        longtitude: long,
      },
      {
        headers: {
          Authorization: `JWT ${jwt}`,
        },
      }
    );
    console.log(response);
    dispatch({
      type: "PATIENT/LIST/ADD",
      payload: {
        first_name: response.data.first_name,
        last_name: response.data.last_name,
        uuid: response.data.uuid,
        height: response.data.height,
        weight: response.data.weight,
        doctor_id: response.data.doctor_id,
        phone_number: response.data.phone_number,
        age: response.data.age,
        blood_type: response.data.blood_type,
        lat: response.data.latitude,
        lon: response.data.longitude,
        phone_number: response.data.phone_number,
        registration_date: response.data.registration_date,
      },
    });
  } catch (error) {
    console.error(error);
  }
};
