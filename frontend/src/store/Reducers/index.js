import { combineReducers } from "redux";
import TestReducer from "./Reducer";

const reducers = combineReducers({
  Test: TestReducer,
});

export default reducers;

