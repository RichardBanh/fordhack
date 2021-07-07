import "./App.css";
import { createStore, combineReducers, applyMiddleware } from "redux";
import { Provider } from "react-redux";
import { Main } from "./Components/mainScreen";
import { login } from "./Redux/loginReducer";


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
  login,
});

const store = createStore(rootReducer);
export default App;
