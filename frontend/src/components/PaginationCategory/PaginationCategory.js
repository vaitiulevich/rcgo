// import { Routes, Route,BrowserRouter } from "react-router-dom";
// import axios from 'axios';
import { useEffect, useState } from 'react';
import '../../App.css'
import './pagination-category.css'
import axios from 'axios';
import { BASE_URL } from '../../url';
import CategoryAll from '../CategoryAll/CategoryAll';
import Pagination from "react-js-pagination";
import ReactPaginate from 'react-paginate';
import { Link } from 'react-router-dom';
import noImg from '../../assets/noImg.png'
import delivery from '../../assets/delivery_small.gif'
import sclad from '../../assets/sclad.png'

const PaginationCategory=({cat,sub,search})=> {
  let [products,setProducts]=useState()
  let [isSuccessAdd,setSuccessAdd]=useState(false)
  let [pageCount,setPageCount]=useState(1)
  let [activePage,setActivePage]=useState(1)
  let [catt,setCat]=useState(cat?cat:null)
  let [subb,setSub]=useState(sub?sub:null)
  useEffect(()=>{
    getProduct()
  },[activePage])
  const getProduct=()=>{
    axios.get(BASE_URL+'products/',{params:{page:activePage,category:catt,subcategory:subb,search:search?search:null}})
    .then(res=>{
      console.log(res)
      setProducts(res.data.results)
      setPageCount(Math.ceil(res.data.count/60))

    })
    .catch(err=>console.log(err))
  }
  console.log(products)
  let description=products&&products.description?products.description.split('\n'):null

  const addCart=()=>{
    // localStorage.setItem()
    
  }
    return (
        <div className='category-pagination-panel'>
          {isSuccessAdd&&
            <div className='seccess-add'>
                {/* <img src={addcart} alt='добавлено в корзину'/> */}
                Товар добавлен в корзину</div>
            }
        <div className='category-catalog'>
            {products&&
            products.length>0?
            <>
            <h2 className='category-pagination-title'>Каталог</h2>
            {products.map((i,ind)=>
            <div className='block-category-item' key={ind}>
              <div className='category-product-title'>
              <Link to={'/product/'+i.slug}>
                {i.name}
                </Link>
                </div>
                <div className='category-product'>
                  {i.images&&i.images[0]?
                <div>
                  <Link to={'/product/'+i.slug}>
                <img height='120px' width='180px' className='category-product-img' src={i.images[0].img_low} alt={i.name}/>
                  </Link>
                </div>
                :
                <div className='product-img'>
                <Link to={'/product/'+i.slug}>
                  <img height='120px' width='180px's className='no-img' src={noImg} alt='нет картинки'/>
                </Link>
                </div>
                }
                <div className='category-prod-option'>
                  <div><span className='desc-text'>Производитель:</span> {i.brand}</div>
                  <div><span className='desc-text'>Артикул:</span> {i.article_sup}</div>
                  <div>
                    <p className='category-description-page'>
            {i.description&&i.description.split('\n')[1]}</p>
          </div>
          {i.quantity_composition=="В наличии"&&<p className='status-qu'><img src={sclad} alt='есть'/>Есть на складе</p>}

          <div className='category-product-price'><span className='desc-text'>Цена: </span>{i.margin_price} Br</div>
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
    setSuccessAdd(true)
    setTimeout(()=>setSuccessAdd(false),2000)
    localStorage.setItem('cart',JSON.stringify(prod)) 
    }
              }}
              className='btn-add-cart'>Купить</div>
                </div>
               <div className='delivery-cat'>
                  <Link to={'/delivery'}>
                  <img src={delivery} alt='delivery'/>
                  </Link>
                </div>
                
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

export default PaginationCategory;