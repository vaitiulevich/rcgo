import React from 'react';
import ReactDOM from 'react-dom/client';
import { BrowserRouter, Routes, Route} from "react-router-dom";
import './index.css';
import App from './App';
// import { Provider } from 'react-redux';
import Home from './pages/Home/Home';
import Delivery from './pages/static/Delivery/Delivery';
import ProductPage from './pages/ProductPage/ProductPage';
import About from './pages/static/About/About';
import Contacts from './pages/static/Contacts/Contacts';
import Service from './pages/static/Service/Service';
import Opt from './pages/static/Opt/Opt';
import Conditions from './pages/static/Conditions/Conditions';
import Xiaomi from './pages/static/Xiaomi/Xiaomi';
import CategoryPage from './pages/CategoryPage/CategoryPage';
import SubcategoryPage from './pages/SubcategoryPage/SubcategoryPage';
import Cart from './pages/Cart/Cart';
import Search from './pages/Search/Search';

export default function Routing() {
    return (
      <BrowserRouter>
        <Routes>
          <Route path='/' element={<App/>}>
            <Route path='/' element={<Home/>} />
            <Route path='/delivery' element={<Delivery/>} />
            <Route path='/about' element={<About/>} />
            <Route path='/contacts' element={<Contacts/>} />
            <Route path='/service' element={<Service/>} />
            <Route path='/opt' element={<Opt/>} />
            <Route path='/conditions' element={<Conditions/>} />
            <Route path='/xiaomi' element={<Xiaomi/>} />
            <Route path='/cart' element={<Cart/>} />
            <Route path='/product/:Prodid' element={<ProductPage/>} />
            <Route path='/search/:SearchText' element={<Search/>} />
            <Route path='/cat/:catname' element={<CategoryPage/>} />
            <Route path='/subcat/:catname/:subcatname' element={<SubcategoryPage/>} />
            {/* <Route path='/enter' element={<Enter/>} /> */}
            {/* <Route path='/calendly/:id' element={<CalendlyPage/>} /> */}
          </Route>
        </Routes>
      </BrowserRouter>
    );
  }

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  // <Provider>
    <Routing />
  // </Provider>
);
