// import { Routes, Route,BrowserRouter } from "react-router-dom";
// import axios from 'axios';
import { useEffect, useState } from 'react';
import '../../App.css'
import './ProductPage.css'
import axios from 'axios';
import { BASE_URL } from '../../url';
import CategoryAll from '../../components/CategoryAll/CategoryAll';
import Pagination from '../../components/Pagination/Pagination';
import { Link } from 'react-router-dom';
import PaginationCategory from '../../components/PaginationCategory/PaginationCategory';

const SubcategoryPage=()=> {
  let [product,setProduct]=useState()
  let [quantity,setQuantity]=useState(1)
  // const regular = new RegExp("[0-9]{1,}");
  let sub=window.location.pathname.split('/')[window.location.pathname.split('/').length-1]
  let cat=window.location.pathname.split('/')[window.location.pathname.split('/').length-2]
  let [products,setProducts]=useState()
  useEffect(()=>{
  },[])
  console.log(sub)
    return (
        <>
          {/* <CategoryAll/> */}
          {/* <Pagination cat={cat} sub={sub}/> */}
          <PaginationCategory cat={cat} sub={sub}/>
        </>
    );
}

export default SubcategoryPage;