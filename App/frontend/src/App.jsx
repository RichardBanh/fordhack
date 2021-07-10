import "./App.css";
import { createStore, combineReducers, applyMiddleware } from "redux";
import { Provider } from "react-redux";
import { Main } from "./Components/mainScreen";
import { Login } from "./Redux/loginReducer";
import { LoginProcess } from "../src/Redux/Middleware/loginFetch";
import { getVehicleList } from "../src/Redux/Middleware/getListFetch";
import { CarList } from "../src/Redux/carlistReducer";
function App() {
  return (
    <>
      <Provider store={store}>
        <Main />
      </Provider>
    </>
  );
}

const rootReducer = combineReducers({
  Login,
  CarList,
});

const middleware = [LoginProcess, getVehicleList];

const store = createStore(rootReducer, applyMiddleware(...middleware));
export default App;
