// import { Routes, Route,BrowserRouter } from "react-router-dom";
// import axios from 'axios';
import { useEffect, useState } from 'react';
import '../../App.css'
// import './ProductPage.css'
import axios from 'axios';
import { BASE_URL } from '../../url';
import CategoryAll from '../../components/CategoryAll/CategoryAll';
import Pagination from '../../components/Pagination/Pagination';
import { Link } from 'react-router-dom';

const Search=()=> {
  // console.log(window.location.pathname)
  let search=decodeURIComponent(window.location.pathname.split('/')[window.location.pathname.split('/').length-1])
    return (
        <>
          {/* <CategoryAll/> */}
          <Pagination search={search}/>
        </>
    );
}

export default Search;