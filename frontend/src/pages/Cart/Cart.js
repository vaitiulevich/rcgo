// import { Routes, Route,BrowserRouter } from "react-router-dom";
// import axios from 'axios';
import { useEffect, useState } from 'react';
import '../../App.css'
import './Cart.css'
import axios from 'axios';
import { BASE_URL } from '../../url';
import CategoryAll from '../../components/CategoryAll/CategoryAll';
import Pagination from '../../components/Pagination/Pagination';
import { Link } from 'react-router-dom';
import ReactInputMask from "react-input-mask";
import noImg from '../../assets/noImg.png'
import { getInfoCart } from '../../store/Actions/Action';
import { useDispatch } from 'react-redux';

const Cart=()=> {
  let [cart,setCart]=useState()
  let [status,setStatus]=useState()
  let [dataUser,setDataUser]=useState()
  const dispatch= useDispatch()
  let [errorData,setErrorData]=useState({
    address: '',
    email: '',
    fio: '',
    index:'',
    phone: '',
    delivery:'',
    payment:''
  })

  useEffect(()=>{
    getCart()
  },[status])
  useEffect(()=>{
    dataUser&&setErrorData(validate(dataUser))
  },[dataUser])

  const createOrder=()=>{
    let basc=[]
    JSON.parse(localStorage.getItem('cart')).map(i=>basc.push({products:i.id,quantity:i.quantity}))
    console.log({
      baskets:basc,
      fio:dataUser.fio,
      address:dataUser.address,
      index:dataUser.index,
      phone:dataUser.phone,
      delivery:dataUser.delivery,
      email:dataUser.email,
      comment:dataUser.comment,
      payment:dataUser.payment
    })
    axios.post(BASE_URL+'order/',{
      baskets:basc,
      fio:dataUser.fio,
      address:dataUser.address,
      index:dataUser.index,
      phone:dataUser.phone,
      delivery:dataUser.delivery,
      email:dataUser.email,
      comment:dataUser.comment,
      payment:dataUser.payment
    })
    .then(res=>{
      console.log(res)
      localStorage.removeItem('cart')
      setStatus('Успешно оформлено')
      window.location.reload()
      getCart()
    })
    .catch(err=>console.log(err))
  }
  const getCart=()=>{
    localStorage.getItem('cart')&&setCart(JSON.parse(localStorage.getItem('cart')))
  }
  console.log(cart)
  const changeInputUser = (event) => {
    event.persist();
    // setStatusDataUpdate('')
    // localStorage.setItem('user',JSON.stringify(data))
    setDataUser((prev) => {
      return {
        ...prev,
        [event.target.name]: event.target.value,
      };
    });
    // console.log(data)
  };
  const validate = (values) => {
    console.log(values)
    let errors = {};
    if (!values.fio) {
      errors.fio = "Поле ФИО обязательно для ввода";
    }else
    if(values.fio<2){
      errors.fio = "Поле ФИО должно быть длиннее двух символов";
    }

    if (!values.email) {
      errors.email = "Поле email обязательно для ввода";
    }else
    if (!values.email) {
      errors.email = "Поле email обязательно для ввода";
    }else
    if(/^[\w-\.]+@([\w-]+\.)+[\w-]{1,4}$/.test(values.email)===false){
      errors.email = "Поле email может содержать только буквы латинского алфавита";
    }

    if (!values.address) {
      errors.address = "Поле адресс обязательно для ввода";
    }

    if (!values.payment) {
      errors.payment = "Выберите способ оплаты";
    }

    if (!values.delivery) {
      errors.delivery = "выберите способ доставки";
    }

    if (!values.phone) {
      errors.phone = "Поле номер телефона обязательно для ввода";
    }

    // if (!values.index) {
    //   errors.index = "Поле почтового индекса обязательно для ввода";
    // }
    
    return errors
  }
    return (
        <div className='cart'>
        <h2>Корзина</h2>
        {cart&&cart.length>0?
        <div>
        <table>
          <tr className='handler-table'>
            <th>Фото:</th>
            <th>Наименование:</th>
            <th>Кол-во:</th>
            <th>Стоимость:</th>
            <th></th>
          </tr>
{
  cart.map((i,ind)=>
  <tr key={ind}>
    <td>
      {i.img==''?
      <img src={noImg} alt='нет картинки'/>
      :
    <img src={i.img} alt='i.name'/>
      }
    </td>
    <td>
      {i.name}
    </td>
    <td className='quantity-td'>
    <div className='prod-quantity'>
                <div className='pointer' onClick={()=>{
                    if(i.quantity>1){
                    localStorage.removeItem('cart')
                    cart[ind].quantity=cart[ind].quantity-1
                    localStorage.setItem('cart',JSON.stringify(cart))
                    getCart()
    dispatch(getInfoCart())

                    }
                  }}>-</div>
                <div>{i.quantity}</div>
                <div className='pointer' onClick={()=>{
                if(i.quantity<100){
                  console.log('jjj')
                  localStorage.removeItem('cart')
                    cart[ind].quantity=cart[ind].quantity+1
                    console.log(cart)
                    localStorage.setItem('cart',JSON.stringify(cart))
                    getCart()
    dispatch(getInfoCart())
                  }
                }}>+</div>
              </div>
    </td>
    <td className='price-td'>
      {i.price} Br
    </td>
    <td
    className='delete'
    onClick={()=>{
      localStorage.removeItem('cart')
      cart.splice(ind,1)
      console.log(cart)
      localStorage.setItem('cart',JSON.stringify(cart))
      getCart()
    dispatch(getInfoCart())
    }}
    >x</td>
    </tr>)
}
        </table>

        <h2>Оформление заказа</h2>
        <div className='all-data'>
        {/* <fieldset> */}
  <div>
  <div>Способ доставки:</div>

      {errorData.delivery&&<div className='err'>{errorData.delivery}</div>}

  <div>
    <input onChange={changeInputUser} type="radio" id="huey" name="delivery" value="samovevoz"/>
    <label for="huey">Самовывоз из офиса(0 р.)</label>
  </div>

  <div>
    <input onChange={changeInputUser} type="radio" id="dewey" name="delivery" value="dekiveryMKAD" />
    <label for="dewey">Доставка курьером в пределах МКАД (10 р.)</label>
  </div>

  <div>
    <input onChange={changeInputUser} type="radio" id="louie" name="delivery" value="deliveryRB" />
    <label for="louie">Доставка курьером по РБ (17 р.)</label>
  </div>

  <div>
    <input onChange={changeInputUser} type="radio" id="louie123" name="delivery" value="post" />
    <label for="louie123">Почтой (9 р.)</label>
  </div>
  </div>

{/* </fieldset> */}

<div className='data'>
  <div>Мои данные:</div>
  {/* <label>Имя</label> */}
          <input
          name='fio'
          type='text'
          placeholder='ФИО'
      className='inp'
          onChange={changeInputUser}
          />
          {errorData.fio&&<div className='err'>{errorData.fio}</div>}

          <input
          name='email'
          type='email'
          placeholder='Email'
      className='inp'
          onChange={changeInputUser}
          />
          {errorData.email&&<div className='err'>{errorData.email}</div>}

          <input
          name='address'
          type='text'
          placeholder='Адрес'
      className='inp'
          onChange={changeInputUser}
          />
          {errorData.address&&<div className='err'>{errorData.address}</div>}

          {/* <input
          type='text'
          placeholder='Номер телефона'
          onChange={changeInputUser}
          /> */}
          <ReactInputMask
       mask="+375(99) 999-99-99"
       type="tel"
      name='phone'
      // value={ProfData.phone}
      onChange={changeInputUser}
      className="inp" 
      placeholder="Телефон" 
      required
       />
          {errorData.phone&&<div className='err'>{errorData.phone}</div>}

          {/* <input
          onChange={changeInputUser}
          /> */}
          <input
          name='index'
          className='inp'
          type='text'
          placeholder='Почтовый индекс'
          onChange={changeInputUser}
          />
          {errorData.index&&<div className='err'>{errorData.index}</div>}
         
</div>
<div>

<div>Способ оплаты:</div>
{errorData.payment&&<div className='err'>{errorData.payment}</div>}

<div>
  <input onChange={changeInputUser} type="radio" id="huey1" name="payment" value="nal"/>
  <label for="huey1">наличными в магазине</label>
</div>

<div>
  <input onChange={changeInputUser} type="radio" id="dewey1" name="payment" value="beznal" />
  <label for="dewey1">Безналичный расчет</label>
</div>

<div>
  <input onChange={changeInputUser} type="radio" id="louie1" name="payment" value="bank" />
  <label for="louie1">По платежному поручению в любом банке</label>
</div>
{/* <div>
  <input onChange={changeInputUser} type="radio" id="louie12" name="payment" value="deliveryRB" />
  <label for="louie12">По платежному поручению в любом банке</label>
</div> */}
</div>

          {/* <input/> */}
        </div>
        <div>Комментарий</div>
        <textarea
          name='comment'
          // className='inp'
          type='text'
          // placeholder='Комментарий'
          onChange={changeInputUser}
          />
        <button onClick={createOrder}>Оформить</button>

        </div>
      
        :<div>
          Тут пусто
          </div>}
        
          {/* <CategoryAll/> */}
          {/* <Pagination cat={cat} sub={sub}/> */}
        </div>
    );
}

export default Cart;