const initialState = { message: "", notification: false };

export const NotificationReducer = (state = initialState, action) => {
  switch (action.type) {
    case "NOTIFICATION/ON":
      return {
        message: action.payload.message,
        notification: !state.notification,
      };
    case "NOTIFICATION/OFF":
      return {
        message: "",
        notification: !state.notification,
      };
    default:
      return state;
  }
};
