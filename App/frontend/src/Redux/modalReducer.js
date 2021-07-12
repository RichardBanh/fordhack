const initialState = {
  modalRental: null,
  modalDetail: null,
  modalRequest: null,
  modalNotification: null,
  modalVehicleId: null,
};

export const ModalData = (state = initialState, action) => {
  switch (action.type) {
    case "SET/MODAL/DATA/DETAIL":
      return {
        ...state,
        modalDetail: { ...action.payload.modalDetail },
      };
    default:
      return state;
  }
};
