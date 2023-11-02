import { Routes, Route,BrowserRouter,Link } from "react-router-dom";
import { useEffect } from 'react';
import '../../App.css'
import './footer.css'
import logo from '../../assets/logo.svg'

const Footer=()=> {

    return (
        <div className="footer">
            <img src={logo} alt="logo"/>
            <div className="menu-foot">
                <h3>Меню</h3>
            <Link to={'/'}>Главная</Link>
                    <Link to={'/delivery'}>Доставка и оплата</Link>
                    <Link to={'/about'}>О нас</Link>
                    <Link to={'/contacts'}>Адрес и контакты</Link>
                    <Link to={'/service'}>Сервис</Link>
                    <Link to={'opt'}>Опт</Link>
                    <Link to={'/conditions'}>Условия покупки</Link>
                    <Link to={'/xiaomi'}>Xiaomi</Link>
            </div>
            <div className="menu-foot">
                <h3>Контакты</h3>
                <p>8(029)577-46-70</p>
                <p>8(044)511-45-13</p>
                <p>+375295774670</p>
                <p>Ежедневно 10:00-19:00</p>
                <p>ТЦ Корона: Беларусь, Минск, <br/>
                    Кальварийская улица, 24  (второй этаж)</p>
            </div>
        </div>
    );
}

export default Footer;