import Cookies from "js-cookie";

export const fetchfun = (url, method, rawch, raw, auth) => {
  const heading = {
    Accept: "application/json",
    "Content-Type": "application/json",
  };
  if (auth) {
    heading.Authorization = "Bearer " + Cookies.get("jwt");
  }
  const sendBod = {
    method: method,
    headers: heading,
  };
  if (rawch) {
    sendBod.body = raw;
  }

  console.log(sendBod);

  return fetch(url, sendBod);
};
