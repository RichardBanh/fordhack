const initialState = { carlist: [] };

export const CarList = (state = initialState, action) => {
  switch (action.type) {
    case "SET/ALL/CARLIST":
      return {
        carlist: [...action.payload.car],
      };
    default:
      return state;
  }
};
