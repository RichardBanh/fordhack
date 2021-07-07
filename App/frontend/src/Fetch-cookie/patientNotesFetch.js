import Cookies from "js-cookie";
import axios from "axios";

export const patientNotesFetch = async (patient_uuid, dispatch) => {
  const url = "http://127.0.0.1:8000/patient-chart/";
  const jwt = Cookies.get("jwt");
  try {
    const response = await axios.put(
      url,
      {
        patient_uuid: patient_uuid,
      },
      {
        headers: {
          Authorization: `JWT ${jwt}`,
        },
      }
    );
    console.log(response.data);
    dispatch({
      type: "LOAD/NOTES/ALL",
      payload: { medicalChart: [...response.data] },
    });
  } catch (error) {
    console.error(error);
  }
};

export const sendNotes = async (data, dispatch) => {
  const url = "http://127.0.0.1:8000/patient-chart/";
  const jwt = Cookies.get("jwt");
  try {
    const response = await axios.post(url, data, {
      headers: {
        Authorization: `JWT ${jwt}`,
      },
    });
    console.log(response);
    dispatch({
      type: "ADD/UPDATE/CHART",
      payload: {
        date: response.data.date,
        patientNote: response.data.patientNote,
        doctor_id: response.data.doctor_id,
      },
    });
  } catch (error) {
    console.error(error);
  }
};
