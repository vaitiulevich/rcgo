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
import noImg from '../../assets/noImg.png'
import robot from '../../assets/icons/span.vertical-menu-ico.svg'
import tank from '../../assets/icons/span.vertical-menu-ico-1.svg'
import ship from '../../assets/icons/span.vertical-menu-ico-2.svg'
import plane from '../../assets/icons/span.vertical-menu-ico-3.svg'
import vert from '../../assets/icons/span.vertical-menu-ico-4.svg'
import copter from '../../assets/icons/span.vertical-menu-ico-5.svg'
import auto from '../../assets/icons/span.vertical-menu-ico-6.svg'
import detail from '../../assets/icons/span.vertical-menu-ico-10.svg'
import colobike from '../../assets/icons/span.vertical-menu-ico-8.svg'

const CategoryPage=()=> {
  let [product,setProduct]=useState()
  let [quantity,setQuantity]=useState(1)
  // const regular = new RegExp("[0-9]{1,}");
  let cat=window.location.pathname.split('/')[window.location.pathname.split('/').length-1]
  let [products,setProducts]=useState()

  console.log(cat)
  useEffect(()=>{
    axios.get(BASE_URL+'subcategories',{params:{category:cat}})
    .then(res=>{
      console.log(res)
      setProducts(res.data)})
    .catch(err=>console.log(err))
  },[cat])
    return (
        <div className='category-block'>
          <div>
            {cat=='mashiny'&&<img className='auto-animate' src={auto} alt='auto'/>}
            {cat=='kvadrokoptery'&&<img className='auto-animate' src={copter} alt='auto'/>}
            {cat=='vertolety'&&<img className='auto-animate' src={vert} alt='auto'/>}
            {cat=='samolety'&&<img className='auto-animate' src={plane} alt='auto'/>}
            {cat=='korabli'&&<img className='auto-animate' src={ship} alt='auto'/>}
            {cat=='tanki'&&<img className='auto-animate' src={tank} alt='auto'/>}
            {cat=='igrushki-i-hobbi'&&<img className='auto-animate' src={robot} alt='auto'/>}
            {cat=='zapchasti'&&<img className='zap-animate' src={detail} alt='auto'/>}
            {cat=='kolesnyj-transport'&&<img className='auto-animate' src={colobike} alt='auto'/>}
            {/* {cat=='mashiny'&&<img className='auto-animate' src={auto} alt='auto'/>} */}

            </div>
          {products&&
          <>
          {products.length<1?
          <>
            Пока ничего нет
          </>:
        <div className='category-page'>
          {products.map((i,ind)=>
          <div className='subcategory' key={ind}>
            <Link onClick={()=>{cat === 'zapchasti' ?  window.location.assign('/cat/'+i.slug) : window.location.assign('/subcat/'+cat+'/'+i.slug)}} to={'/subcat/'+cat+'/'+i.slug}>
              {i.image!==null?
              <img height='100px' width='160px' src={i.image} alt={i.name}/>
              :
              <img height='80px' width='120px' src={noImg} alt='noImg'/>
              }
              {i.name}
              </Link>
          </div>)}
          </div> 
          } 
          </>
        }
          {/* <CategoryAll/> */}
          {/* <Pagination cat={cat}/> */}
        </div>
    );
}

export default CategoryPage;