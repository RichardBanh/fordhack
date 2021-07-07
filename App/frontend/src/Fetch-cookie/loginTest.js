const axios = require("axios");

const loginFetch = async () => {
  const url = "http://127.0.0.1:8000/doctors/current_user/";

  axios
    .get(url, {
      headers: {
        Authorization: `JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjo1LCJ1c2VybmFtZSI6ImdpbGVhZCIsImV4cCI6MTYyMTk4NzgwOSwiZW1haWwiOiJnaWxlYWRAYWRtaW4uY29tIn0.9XUy7o15dDK83szEyYwSwVezomfZCCJe_E9IJ5yZou0`,
      },
    })
    .then((res) => console.log(res.data))
    .catch((err) => {
      console.log(err);
    });
};

loginFetch();
