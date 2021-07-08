import { storeCookie } from "../../CookieFunctions/Cookie";

const LoginProcess = (storeAPI) => (next) => (action) => {
  //error point
  const bearer = `Bearer ${action.payload.jwt}`;
  const processedB = bearer.replace(/\"/g, "");
  //error point
  if (action.type === "LOGIN/MIDDLEWARE") {
    const fetchfun = async () => {
      const url = action.payload.url;
      const resp = await fetch(url, {
        method: action.payload.method,
        headers: {
          Accept: "application/json",
          "Content-Type": "application/json",
          Authorization: processedB,
        },
      });
      const data = await resp.json();
      //error point
      console.log(data);
      //error point
    };
    fetchfun();
  }
  return next(action);
};

export { LoginProcess };

//need to call dispatch
