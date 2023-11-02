// import { Routes, Route,BrowserRouter } from "react-router-dom";
// import axios from 'axios';
import { useEffect, useState } from 'react';
import './delivery.css'
import chek from '../../../assets/chek.jpg.crdownload'

const Contacts=()=> {

    return (
        <div className="static container">
          <h2>Адрес и контакты</h2>
          <p><b>
          г. Минск, ул.Чернышевского д.10 офис 11
          <br/><br/>+375(29)577-46-70 mts
<br/>+375(44)577-46-70 vel
<br/>+375(25)777-46-70 life
<br/>Почта для безналичных заказов и юр. лиц info@rc-go.by 
            </b></p>

            <p>
                <span>Время работы:</span>
                <br/>Пн-Пт с 10.00 до 19.00 (без перерыва) 
                <br/>Вы можете позвонить нашим менеджерам и получить ответы на все интересующие Вас вопросы или оформить заказ, если уже сделали свой выбор.
                <br/>В любое время Вы можете задать свои вопросы и оформить заказ по почте  info@rc-go.by  или воспользоваться системой заказа на сайте.
                <br/>Также к Вашим услугам удобный ЧАТ, который появляется сбоку: менеджеры обязательно ответят на все вопросы (просим проявить терпение, ответ может быть не всегда моментальный из-за большой загруженности) 

                <br/>Координаты для навигатора 53.927762, 27.599798
            </p>

          <p>
            <span>ООО "Радиоуправляемые  модели"</span>
            <br/><span>Зарегистрирован </span>Минским горисполкомом 25 октября 2013 года.
            <br/> <span>Юридический адрес: </span>220012, г.Минск,  ул.Чернышевского 10 офис 11
            <br/> <span>Физический адрес: </span>220012, г.Минск, ул.Чернышевского 10 офис 11
            <br/> <span>УНП: </span>192149079
          </p>
          <p>
            <span>Рс BYN: </span>BY23ALFA30122558490010270000 в ЗАО «Альфа-Банк», 220012 г. Минск, г. Минск, ул. Сурганова, 43-47
            <br/><span>БИК </span>ALFABY2X
          </p>
          <p>
          Зарегистрирован в торговом  реестре Республики Беларусь 20.11.2013 
          <br/><span>Директор: </span>Нарутович Андрей Николаевич
          </p>
        </div>
    );
}

export default Contacts;