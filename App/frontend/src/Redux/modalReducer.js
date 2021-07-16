const initialState = {
  modalRental: null,
  modalDetail: null,
  modalRequest: null,
  modalNotification: null,
  modalVehicleId: null,
  show: "",
};

export const ModalData = (state = initialState, action) => {
  switch (action.type) {
    case "SET/MODAL/DATA/DETAIL":
      return {
        ...state,
        modalDetail: { ...action.payload.modalDetail },
      };
    case "SET/MODAL/SHOW":
      return {
        ...state,
        show: action.payload.showWhat,
      };
    default:
      return state;
  }
};
