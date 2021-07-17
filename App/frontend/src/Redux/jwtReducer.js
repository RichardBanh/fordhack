const initialState = { jwt: "" };

export const jwtReducer = (state = initialState, action) => {
  switch (action.type) {
    case "ADD/JWT":
      return {
        jwt: action.payload.jwt,
      };
    case "REMOVE/JWT":
      return {
        jwt: "",
      };
    default:
      return state;
  }
};
