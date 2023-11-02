// import Logo from './logo'
// import logoHeader from '../../assets/logo header.svg'
import './entry.css'
// import card from '../../assets/card.svg'
// import { Link } from "react-router-dom";
// import logo from '../../assets/logo.svg'
// import about from '../../assets/about.svg'
// import search from '../../assets/search.svg'
// import cart from '../../assets/cart.svg'
// import Category from '../Category/Category';
// import viber from '../../assets/icons/viber.png'


const Entry=({setClose})=> {
    return (
        <div className="entry">
            <div>
                <input type='text' placeholder='login'/>
                <input type='password' placeholder='password'/>
                <button>{'>'}</button> 
            </div>
            
            <div>
                <a>registr</a>
                <a>forgot pass</a>
            </div>
        </div>
    );
}

export default Entry;