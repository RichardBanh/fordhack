import { storeCookieJWT } from "../../CookieFunctions/Cookie";
import { fetchfun } from "../../FetchFunction";

const getVehicleList = (storeAPI) => (next) => (action) => {
  if (action.type === "GET/LIST/MIDDLEWARE") {
    const raw = JSON.stringify({ type: "ALL" });
    fetchfun(action.payload.url, action.payload.method, true, raw, true)
      .then((response) => response.json())
      .then((response) => {
        storeAPI.dispatch({
          type: "SET/ALL/CARLIST",
          payload: { car: response },
        });
      });
  }
  return next(action);
};

export { getVehicleList };
