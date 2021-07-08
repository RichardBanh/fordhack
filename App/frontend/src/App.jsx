import "./App.css";
import { createStore, combineReducers, applyMiddleware } from "redux";
import { Provider } from "react-redux";
import { Main } from "./Components/mainScreen";
import { Login } from "./Redux/loginReducer";
import { LoginProcess } from "../src/Redux/Middleware/loginFetch";

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
});

const middleware = [LoginProcess];

const store = createStore(rootReducer, applyMiddleware(...middleware));
export default App;
