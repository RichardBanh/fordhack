const initialState = { locations: [] };

export const CarLocation = (state = initialState, action) => {
  switch (action.type) {
    case "SET/CARLIST/LOCATION":
      return {
        locations: [...state.locations, action.payload.location],
      };
    default:
      return state;
  }
};
