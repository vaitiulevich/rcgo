// import Logo from './logo'
// import logoHeader from '../../assets/logo header.svg'
import './header.css'
// import card from '../../assets/card.svg'
import { Link } from "react-router-dom";
import logo from '../../assets/logo.svg'
import about from '../../assets/about.svg'
import search from '../../assets/search.svg'
// import cart from '../../assets/cart.svg'
import Category from '../Category/Category';
import viber from '../../assets/icons/viber.png'
import { useState } from 'react';
import Entry from '../Entry/Entry';
import cart from '../../assets/icon-cart-round.png'
import { useSelector } from 'react-redux';
import { useDispatch } from 'react-redux';
import { getInfoCart } from '../../store/Actions/Action';
import { useEffect } from 'react';


function Header() {
    let [isModalEntry,setModalEntry]=useState(false)
    // const infoCart=useSelector()
    const cartCount=useSelector((state)=>state.Test.cartInfo)

    const dispatch= useDispatch()
    let [searchText,setSearchText]=useState()
    useEffect(()=>{
    dispatch(getInfoCart())
    },[])
    return (
        <div className="header">
            <div className='contacts-header container'>
                <div className='contact-number'>
                <a className='phone-number' href='tel:8(029)577-46-70'>8(029)577-46-70 </a><br/> 
                <a className='phone-number' href='tel:8(044)511-45-13'>8(044)511-45-13</a><br/> 
                <a href='viber://chat?number=%2375295774670'></a>
                </div>
                <div><img className='viber' src={viber} alt='viber'/>
                +375295774670</div>
                <div className='schedule'>
                Магазин работает с 10.00 до 19.00 пн-пт<br/> 
заказы онлайн и по телефону без выходных
<div>
ТЦ Корона: Беларусь, Минск,<br/>
Кальварийская улица, 24  (второй этаж)
</div>
                </div>
            </div>
            <div className='header-all container'>
                <Link to={'/'}>
                <img src={logo} alt='logo'/>
                </Link>
                <div className='header-optional'>
                    <h2 className='header-handler'>Интернет-магазин радиоуправляемых моделей</h2>
                    <div className='header-search'>
                        <div className='search-block'>
                          <input
                        onKeyDown={(e)=>{
                            if(e.key==='Enter'){
                              console.log(e.target.value)
                              localStorage.setItem('s',e.target.value.trim())
                              window.location.assign('/search/'+searchText)
                            }
                          }}
                          onChange={(e)=>{
                            setSearchText(e.target.value)
                          }}
                         className='inp-search' placeholder='Введите артикул или часть названия для поиска'/>
                        <button
                        onClick={()=>{
                            window.location.assign('/search/'+searchText)
                        }}
                         className='header-btn'><img src={search} alt='search'/></button>
                        {/* <button onClick={()=>setModalEntry(!isModalEntry)} className='header-btn'><img src={about} alt='about'/></button> */}
                          
                        </div>
                        <div className='block-cart-header'>
                            <div className='count-cart'>{cartCount}</div>
                            <Link to={'/cart'}>
                               <img src={cart} alt='cart'/> 
                            </Link>
                            </div>
                    </div>
                </div>
            </div>
            <Category/>
        </div>
    );
}

export default Header;