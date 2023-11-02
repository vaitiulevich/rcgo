const initialState = {
    cartInfo: 0,
  };
  
  export default function TestReducer(state = initialState, action) {
    switch (action.type) {
      case "DO_THIS":
        return {
          ...state,
          cartInfo: action.payload,
        };
      default:
        return state;
    }
  }