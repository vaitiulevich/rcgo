// import Logo from './logo'
// import logoHeader from '../../assets/logo header.svg'
import './category.css'
import robot from '../../assets/icons/span.vertical-menu-ico.svg'
import tank from '../../assets/icons/span.vertical-menu-ico-1.svg'
import ship from '../../assets/icons/span.vertical-menu-ico-2.svg'
import plane from '../../assets/icons/span.vertical-menu-ico-3.svg'
import vert from '../../assets/icons/span.vertical-menu-ico-4.svg'
import copter from '../../assets/icons/span.vertical-menu-ico-5.svg'
import auto from '../../assets/icons/span.vertical-menu-ico-6.svg'
import detail from '../../assets/icons/span.vertical-menu-ico-10.svg'
import colobike from '../../assets/icons/span.vertical-menu-ico-8.svg'
import { Link } from 'react-router-dom'
import Accordion from '../Accordion/Accordion'

function Category() {
    return (
        <div className="category">
            <div className='header-desctop'>
            <div className='menu-information'>
                <nav>
                    <Link to={'/'}>Главная</Link>
                    <Link to={'/delivery'}>Доставка и оплата</Link>
                    <Link to={'/about'}>О нас</Link>
                    <Link to={'/contacts'}>Адрес и контакты</Link>
                    <Link to={'/service'}>Сервис</Link>
                    <Link to={'opt'}>Опт</Link>
                    <Link to={'/conditions'}>Условия покупки</Link>
                    <Link to={'/xiaomi'}>Xiaomi</Link>
                </nav>
            </div>
            <div className='menu'>
                <div className='item-menu'>
                    <Link onClick={()=>window.location.assign('/cat/mashiny')}>
                    <img src={auto} alt='Машина'/>
                    <p>Машины</p>
                    </Link>
                </div>
                <div className='item-menu'>
                    <Link onClick={()=>window.location.assign('/cat/kvadrokoptery')}>
                    <img src={copter} alt='Квадрокоптеры'/>
                    <p>Квадрокоптеры</p>
                    </Link>
                </div>
                <div className='item-menu'>
                    <Link onClick={()=>window.location.assign('/cat/vertolety')}>
                    <img src={vert} alt='Вертолеты'/>
                    <p>Вертолеты</p>
                    </Link>
                </div>
                <div className='item-menu'>
                    <Link onClick={()=>window.location.assign('/cat/samolety')}>
                    <img src={plane} alt='Самолеты'/>
                    <p>Самолеты</p>
                    </Link>
                </div>
                <div className='item-menu'>
                    <Link onClick={()=>window.location.assign('/cat/korabli')}>
                    <img src={ship} alt='Катера и яхты'/>
                    <p>Катера и яхты</p>
                    </Link>
                </div>
                <div className='item-menu'>
                    <Link onClick={()=>window.location.assign('/cat/tanki')}>
                    <img src={tank} alt='Танки'/>
                    <p>Танки</p>
                    </Link>
                </div>
                <div className='item-menu'>
                    <Link onClick={()=>window.location.assign('/cat/igrushki-i-hobbi')}>
                    <img src={robot} alt='Игрушки и хобби'/>
                    <p>Игрушки и хобби</p>
                    </Link>
                </div>
                <div className='item-menu'>
                    <Link onClick={()=>window.location.assign('/cat/zapchasti')}>
                    <img src={detail} alt='Запчасти для моделей'/>
                    <p>Запчасти для моделей</p>
                    </Link>
                </div>
                <div className='item-menu'>
                    <Link onClick={()=>window.location.assign('/cat/zapchasti-dji')}>
                    <img src={colobike} alt='Колесный транспорт'/>
                    <p>Колесный транспорт</p>
                    </Link>
                </div>
                {/* <div className='item-menu'>
                    <Link>
                    <img src={} alt=''/>
                    <p></p>
                    </Link>
                </div> */}
            </div>
            </div>
            <div className='header-mobile container'>
                <Accordion
                title={'Mеню'}
                content={
                    <>
                    <Link to={'/'}>Главная</Link>
                    <Link to={'/delivery'}>Доставка и оплата</Link>
                    <Link to={'/about'}>О нас</Link>
                    <Link to={'/contacts'}>Адрес и контакты</Link>
                    <Link to={'/service'}>Сервис</Link>
                    <Link to={'opt'}>Опт</Link>
                    <Link to={'/conditions'}>Условия покупки</Link>
                    <Link to={'/xiaomi'}>Xiaomi</Link>
                    <Link onClick={()=>window.location.assign('/cat/mashiny')}>Машины</Link>
                    <Link onClick={()=>window.location.assign('/cat/kvadrokoptery')}>Квадрокоптеры</Link>
                    <Link onClick={()=>window.location.assign('/cat/vertolety')}>Вертолеты</Link>
                    <Link onClick={()=>window.location.assign('/cat/samolety')}>Самолеты</Link>
                    <Link onClick={()=>window.location.assign('/cat/korabli')}>Катера и яхты</Link>
                    <Link onClick={()=>window.location.assign('/cat/tanki')}>Танки</Link>
                    <Link onClick={()=>window.location.assign('/cat/igrushki-i-hobbi')}>Игрушки и хобби</Link>
                    <Link onClick={()=>window.location.assign('/cat/zapchasti')}>Запчасти для моделей</Link>
                    <Link onClick={()=>window.location.assign('/cat/zapchasti-dji')}>Колесный транспорт</Link>
                    </>
                }
                />
            </div>
        </div>
    );
}

export default Category;