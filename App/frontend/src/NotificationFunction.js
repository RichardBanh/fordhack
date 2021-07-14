import { fetchfun } from "./FetchFunction";

export const notification = (
  url,
  method,
  rawch,
  raw,
  auth,
  dispatch,
  actionReq
) => {
  dispatch({
    type: "NOTIFICATION/ON",
    payload: { message: "Request sent, Please wait" },
  });
  fetchfun(url, method, rawch, raw, auth)
    .then((res) => {
      return res.json();
    })
    .then((response) => {
      if (response.request.commandStatus === "COMPLETED") {
        dispatch({
          type: "NOTIFICATION/ON",
          payload: { message: actionReq },
        });
      } else {
        dispatch({
          type: "NOTIFICATION/ON",
          payload: { message: "Ford Request Failed, Please resubmit!" },
        });
      }
    });
};

export const engineTurnNotifiction = (
  url,
  method,
  rawch,
  raw,
  auth,
  dispatch,
  action
) => {
  dispatch({
    type: "NOTIFICATION/ON",
    payload: { message: "Request sent, Please wait" },
  });
  fetchfun(url, method, rawch, raw, auth)
    .then((res) => {
      return res.json();
    })
    .then((response) => {
      console.log(response);
      dispatch({
        type: "NOTIFICATION/ON",
        payload: { message: response },
      });
    });
};
