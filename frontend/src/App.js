import {Outlet} from "react-router-dom"
import './App.css'
import Header from "./components/Header/Header";
// import Hero from "./components/hero/Hero";
import Footer from "./components/Footer/Footer";
import UserQuestion from "./components/UserQuestion/UserQuestion";
import CategoryAll from "./components/CategoryAll/CategoryAll";
import car from '../src/assets/icons/span.vertical-menu-ico-6.svg'
import store from './store/store';
import { Provider } from "react-redux";

function App() {
  return (
  <Provider store={store}>
      <Header/>
      {/* <Hero/> */}
      {/* <UserQuestion/> */}
      {/* <img className="animate-background" src={car} alt="car"/> */}
      <div className="home container">
          <CategoryAll/>
      <Outlet/>
        </div>
      <Footer/>
      </Provider>
  );
}

export default App;