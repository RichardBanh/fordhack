import Cookies from "js-cookie";

const storeCookie = (resdata) => {
  Cookies.set("jwt", resdata.token, { expires: 1 / 48 });
  Cookies.set("username", resdata.user.username, { expires: 1 / 48 });
};

export { storeCookie };
