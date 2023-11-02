// import Logo from './logo'
// import logoHeader from '../../assets/logo header.svg'
import { useState } from 'react';
import './user-question.css'
// import card from '../../assets/card.svg'
// import { Link } from "react-router-dom";
// import logo from '../../assets/logo.svg'
// import about from '../../assets/about.svg'
// import search from '../../assets/search.svg'
// import cart from '../../assets/cart.svg'
// import Category from '../Category/Category';
// import viber from '../../assets/icons/viber.png'


const UserQuestion=()=> {
    let [isModalQuestion,setModalQuestion]=useState()
    return (
        <div>
            <div onClick={()=>setModalQuestion(!isModalQuestion)} className="user-question">
                ОСТАВИТЬ СВОЙ ВОПРОС
            </div>
            {isModalQuestion&&
            <div>
            llevkenfkjeb
            </div>
            }           
        </div>
    );
}

export default UserQuestion;