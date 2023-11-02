
export const getInfoCart = () => {
    return (dispatch) => {
      let k=0
      localStorage.getItem('cart')&&JSON.parse(localStorage.getItem('cart')).map(i=>k+=i.quantity)
          dispatch({ type: "DO_THIS", payload: k })
    };
  };