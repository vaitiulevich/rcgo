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
import Carousel from "nuka-carousel"
import arrleft from '../../assets/arrleft.svg'
import arrRight from '../../assets/arrRight.svg'
import sclad from '../../assets/sclad.png'
import pay from '../../assets/pay.png'
import noImg from '../../assets/noImg.png'
import { getInfoCart } from '../../store/Actions/Action';
import { useDispatch } from 'react-redux';

const ProductPage=()=> {
  let [product,setProduct]=useState()
  // let [description,se]=useState()
  let [quantity,setQuantity]=useState(1)
  let [isSuccessAdd,setSuccessAdd]=useState(false)
  const dispatch= useDispatch()

  const regular = new RegExp("[0-9]{1,}");
  console.log(window.location.pathname.split('/')[2])
  useEffect(()=>{
    window.scrollTo(0,370)
    axios.get(BASE_URL+'products/'+window.location.pathname.split('/')[2])
    .then(res=>{
      console.log(res)
      setProduct(res.data)
    })
    .catch(err=>console.log(err))
  },[])
  let description=product&&product.description?product.description.split('\n'):null
  const addCart=()=>{
    // localStorage.setItem()
    let prod=localStorage.getItem('cart')?JSON.parse(localStorage.getItem('cart')):[]
    if(prod.find(pr=>pr.id===product.id)){
        console.log('yes')
    }else{
    prod.push({
        id:product.id,
        name:product.name,
        price:product.margin_price,
        quantity:quantity,
        img:product.images[0]?product.images[0].img_low:'',
        article:product.article_sup,
        availableQuantity:product.quantity_composition
    })
    setSuccessAdd(true)
    setTimeout(()=>setSuccessAdd(false),2000)

    localStorage.setItem('cart',JSON.stringify(prod)) 
    }
    dispatch(getInfoCart())
  }
    return (
        <>
         {isSuccessAdd&&
            <div className='seccess-add'>
                {/* <img src={addcart} alt='добавлено в корзину'/> */}
                Товар добавлен в корзину</div>
            }
          {product&&
          <div className="product">
          <h2>{product.name}</h2>
          <div className='description-prod'>
            <div className='img-prod'>
              {product.images&&product.images.length<2?
              <>
              {product.images.length==1&&
            product.images.map((i,index)=>
              <img key={index} className='prod-img' src={i.img_medium} alt='img-book'/>
            )
            }
            {product.images.length<1&&
            <img src={noImg} alt='нет картинки'/>
            }
              </>
              :            
              <Carousel
              renderCenterLeftControls={({ previousSlide }) => (
                <div className='btn-arrow-left' onClick={previousSlide}>
                  <img src={arrleft} alt='left'/>
                </div>
              )}
              renderCenterRightControls={({ nextSlide }) => (
                <div className='btn-arrow' onClick={nextSlide}>
                  <img src={arrRight} alt='right'/>
                </div>
              )}
               adaptiveHeightAnimation='true'>
              {/* <img className='book-img' src={data.book.mainImageLink} alt={data.book.title}/> */}
              {product.images&&
              product.images.map((i,index)=>
                <img key={index} className='prod-img' src={i.img_medium} alt='img-book'/>
              )
              }
              </Carousel>}
            </div>
            <div className='desc-prod'>
              <p><span className='desc-text'>Производитель: </span> {product.brand}</p>
              <p><span className='desc-text'>Артикул: </span> {product.article_sup}</p>
              <div className='price-block'>

              <div className='prod-quantity'>
                <div onClick={()=>{quantity>1&&setQuantity(quantity-1)}}>-</div>
                <div>{quantity}</div>
                <div onClick={()=>{quantity<100&&setQuantity(quantity+1)}}>+</div>
              </div>
              <div>
              <span className='desc-text'>Цена: </span><span className='price'>{product.margin_price}</span><span className='byn'> BYN</span>
              </div>
              </div>
              {/* {product.quantity_composition==0&&<p>Нет на складе</p>} */}
              {/* {product.quantity_composition>0&&+product.quantity_composition<=10&&<p>Осталось немного</p>} */}
              {product.quantity_composition=="В наличии"&&<p className='status-qu'><img src={sclad} alt='есть'/>Есть на складе</p>}

              <button className='to-cart-btn' onClick={addCart}>В корзину</button>

              <p className='pay-metod'><span className='desc-text'>Способы оплаты: </span><img src={pay} alt='pay'/></p>

              <p className='desc-text'>
              Для резервирования товара оформите заказ на
сайте или позвоните по телефону<br/>
8(029)577-46-70<br/>
8(044)577-46-70
              </p>
              <p>
              <Link className='garant' to={'/delivery'}>Гарантии на возврат</Link>
              </p>
              {/* <p>{}]</p> */}

            </div>
          </div>
          <div className='all-description'>
            {description&&description.map((str, i) => <p key={`p_${i}`}>{str}</p>)}
          </div>
          <div className='all-description'>
            <p className='desc-text'>Внимание! Внешний вид товара, комплектация и характеристики могут изменяться производителем без предварительных уведомлений. Данный интернет-сайт носит исключительно информационный характер и ни при каких условиях не является публичной офертой, определяемой положениями Статьи 464 Гражданского кодекса Республики Беларусь.
            </p>
          </div>
          </div>
          }
        </>
    );
}

export default ProductPage;