import { storeCookieJWT } from "../../CookieFunctions/Cookie";

const LoginProcess = (storeAPI) => (next) => (action) => {
  if (action.type === "LOGIN/MIDDLEWARE") {
    const raw = JSON.stringify({
      username: action.payload.username,
      password: action.payload.password,
    });
    const fetchfun = async () => {
      const url = action.payload.url;
      await fetch(url, {
        method: action.payload.method,
        headers: {
          Accept: "application/json",
          "Content-Type": "application/json",
          // Authorization: processedB,
          // redirect: "follow",
        },
        body: raw,
      })
        .then((response) => response.json())
        .then((result) => {
          storeCookieJWT("refresh", "jwt", result);
          storeAPI.dispatch({
            type: "SET/SIGNIN",
            payload: { username: action.payload.username, signin: true },
          });
        });
    };
    fetchfun();
  }
  return next(action);
};

export { LoginProcess };

//need to call dispatch
