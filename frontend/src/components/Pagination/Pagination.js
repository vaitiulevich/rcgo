// import { Routes, Route,BrowserRouter } from "react-router-dom";
// import axios from 'axios';
import { useEffect, useState } from 'react';
import '../../App.css'
import './pagination.css'
import axios from 'axios';
import { BASE_URL } from '../../url';
import CategoryAll from '../CategoryAll/CategoryAll';
import Pagination from "react-js-pagination";
import ReactPaginate from 'react-paginate';
import { Link } from 'react-router-dom';
import noImg from '../../assets/noImg.png'
import { getInfoCart } from '../../store/Actions/Action';
import { useDispatch } from 'react-redux';

const PaginationCatalog=({cat,sub,search})=> {
  let [products,setProducts]=useState()
  let [isSuccessAdd,setSuccessAdd]=useState(false)
  let [pageCount,setPageCount]=useState(1)
  let [activePage,setActivePage]=useState(1)
  let [catt,setCat]=useState(cat?cat:null)
  let [subb,setSub]=useState(sub?sub:null)
  const dispatch= useDispatch()

  useEffect(()=>{
    getProduct()
  },[activePage,])
  useEffect(()=>{
  },[isSuccessAdd])
  const getProduct=()=>{
    axios.get(BASE_URL+'products/',{params:{page:activePage,category:catt,subcategory:subb,search:search?search:null}})
    .then(res=>{
      console.log(res)
      setProducts(res.data.results)
      setPageCount(Math.ceil(res.data.count/60))
    })
    .catch(err=>console.log(err))
  }
  const addCart=()=>{
    // localStorage.setItem()
    
  }
    return (
        <div className='pagination-panel'>
          {isSuccessAdd&&
            <div className='seccess-add'>
                {/* <img src={addcart} alt='добавлено в корзину'/> */}
                Товар добавлен в корзину</div>
            }
        <div className='catalog'>
            {products&&
            products.length>0?
            <>
            {products.map((i,ind)=>
            <div className='product' key={ind}>
                {i.images&&i.images[0]?
                <Link to={'/product/'+i.slug}>
                <img height='120px' width='180px' className='product-img' src={i.images[0].img_low} alt={i.name}/>
                  </Link>
                :
                <div className='product-img'>
                <Link to={'/product/'+i.slug}>
                  <img height='120px' width='180px' className='no-img' src={noImg} alt='нет картинки'/>
                </Link>
                </div>
                }
              <div 
              onClick={()=>{
                let prod=localStorage.getItem('cart')?JSON.parse(localStorage.getItem('cart')):[]
    if(prod.find(pr=>pr.id===i.id)){
        console.log('yes')
    }else{
    prod.push({
        id:i.id,
        name:i.name,
        price:i.margin_price,
        quantity:1,
        img:i.images[0]?i.images[0].img_low:'',
        article:i.article_sup,
        availableQuantity:i.quantity_composition
    })
    dispatch(getInfoCart())
    setSuccessAdd(true)
    setTimeout(()=>setSuccessAdd(false),2000)

    localStorage.setItem('cart',JSON.stringify(prod)) 
    }
    dispatch(getInfoCart())

              }}
              className='btn-add-cart'>Купить</div>
              <div className='prod-option'>
              <div className='product-title'>
              <Link to={'/product/'+i.slug}>
                {i.name}
                </Link>
                </div>
              <div className='product-price'>{i.margin_price} Br</div>
              </div>

              {/* {i.images.map((item,index)=>
                <img key={index} src={item.image_url} alt={i.name}/>
              )} */}
              
            </div>)}
            </>:
            <>Товаров не найдено</>
            }
          </div>
          {pageCount>1&&
            <div className='pagination'>
            <ReactPaginate
            previousLabel={'<'}
            nextLabel={'>'}
            pageCount={pageCount}
            onPageChange={res=>{
              setActivePage(res.selected+1)
              window.scrollTo(0,400)
            }}
            />
        </div>
          }
      
        </div>
    );
}

export default PaginationCatalog;