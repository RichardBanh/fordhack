const initialState = { locations: [] };

export const CarLocation = (state = initialState, action) => {
  switch (action.type) {
    case "SET/CARLIST/LOCATION":
      return {
        locations: [...state.locations, action.payload.location],
      };
    case "ADD/STREET/INFO":
      return {
        locations: state.locations.map((item, index) => {
          if (item.id !== action.payload.id) {
            return item;
          }
          return {
            ...item,
            googleLocation: action.payload.googleLocation,
          };
        }),
      };
    default:
      return state;
  }
};
