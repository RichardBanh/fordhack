import Cookies from "js-cookie";

const storeCookieJWT = (type, type1, resdata) => {
  Cookies.set(type, resdata.refresh, { expires: 1 / 48 });
  Cookies.set(type1, resdata.access, { expires: 1 / 48 });
};

export { storeCookieJWT };
