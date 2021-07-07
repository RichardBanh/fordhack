import Cookies from "js-cookie";
import axios from "axios";

const storeCookie = (resdata) => {
  Cookies.set("jwt", resdata.token, { expires: 1 / 48 });
  Cookies.set("username", resdata.user.username, { expires: 1 / 48 });
  Cookies.set(
    "dr_id",
    resdata.user.username.charAt(resdata.user.username.length - 1),
    { expires: 1 / 48 }
  );
};

export const loginFetch = async (datain, dispatch, type, payload) => {
  const url = "127.0.0.1:8000/token/";
  try {
    const response = await axios.post(url, datain);
    console.log(response);
    storeCookie(response.data);
    dispatch({
      type: type,
      payload: payload,
    });
  } catch (error) {
    console.error(error);
  }
};
