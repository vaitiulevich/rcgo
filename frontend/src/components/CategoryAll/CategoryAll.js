import { useEffect, useState } from 'react'
import './category-all.css'
import axios from 'axios'
import { BASE_URL } from '../../url'
import Accordion from '../Accordion/Accordion'
import { Link } from 'react-router-dom'

const CategoryAll=()=> {
    let [categories,setCategories]=useState()
    useEffect(()=>{
        axios.get(BASE_URL+'categories')
        .then(res=>{
          console.log(res)
          setCategories(res.data)
        })
        .catch(err=>console.log(err))
      },[])
    return (
        <div className="category-all">
          <div className='menu-desctop'>
            {categories&&categories.map((i,ind)=>
            <Link onClick={()=>{window.location.assign('/cat/'+i.slug)}} key={ind} to={'/cat/'+i.slug}>{i.name}</Link>
            )}
          </div>
            
<div className='menu-mobile'>
<Accordion
                title={'Каталог'}
                content={
                  categories&&categories.map((item,index)=>
    <Link to={'/cat/'+item.slug} key={index}>
                        {item.name}
                    </Link>)
                }
                /> 
</div>
                
        </div>
    );
}

export default CategoryAll;