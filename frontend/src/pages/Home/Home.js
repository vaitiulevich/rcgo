// import { Routes, Route,BrowserRouter } from "react-router-dom";
// import axios from 'axios';
import { useEffect, useState } from 'react';
import '../../App.css'
import './home.css'
import axios from 'axios';
import { BASE_URL } from '../../url';
import CategoryAll from '../../components/CategoryAll/CategoryAll';
import Pagination from '../../components/Pagination/Pagination';
import hero from '../../assets/hero.png'
import hero2 from '../../assets/hero2.jpg'
import hero3 from '../../assets/hero3.jpg'
import hero4 from '../../assets/hero4.jpg'
import hero5 from '../../assets/hero5.jpg'
import hero6 from '../../assets/hero6.jpg'
import Carousel from "nuka-carousel"

const Home=()=> {
  let [products,setProducts]=useState()
  useEffect(()=>{
    axios.get(BASE_URL+'products',{params:{page:1}})
    .then(res=>{
      console.log(res)
      setProducts(res.data.results)
    })
    .catch(err=>console.log(err))
  },[])
    return (
        <div className='home-page'>
          {/* <CategoryAll/> */}
          <div className='carousel-home'>
          <Carousel
          speed={200}
          autoplay={true}
          autoplayInterval={7000}
          disableEdgeSwiping={true}
          wrapAround={true}
          renderCenterLeftControls={false}
          renderCenterRightControls={false}
          >
             <img src={hero2} alt='hero'/>
             <img src={hero} alt='hero'/>
             <img src={hero3} alt='hero'/>
             <img src={hero4} alt='hero'/>
             <img src={hero5} alt='hero'/>
             <img src={hero6} alt='hero'/>
          </Carousel>
          </div>
          <Pagination/>
        </div>
    );
}

export default Home;