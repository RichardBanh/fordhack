const initialState = { username: "", signin: false };

export const Login = (state = initialState, action) => {
  switch (action.type) {
    case "SET/SIGNIN":
      return {
        username: action.payload.username,
        signin: action.payload.signin,
      };

    default:
      return state;
  }
};
