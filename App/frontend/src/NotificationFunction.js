import { fetchfun } from "./FetchFunction";

export const notification = (
  url,
  method,
  rawch,
  raw,
  auth,
  dispatch,
  requestType
) => {
  dispatch({
    type: "NOTIFICATION/ON",
    payload: { message: "REQUEST SENT, Please wait" },
  });
  fetchfun(url, method, rawch, raw, auth)
    .then((res) => {
      return res.json();
    })
    .then((response) => {
      if (response.request.commandStatus === "COMPLETED") {
        dispatch({
          type: "NOTIFICATION/ON",
          payload: { message: requestType },
        });
      } else {
        dispatch({
          type: "NOTIFICATION/ON",
          payload: { message: "Ford Request Failed, Please resubmit!" },
        });
      }
    });
};
