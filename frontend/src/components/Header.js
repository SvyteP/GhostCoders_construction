import React, { useContext } from "react";
import '../style/Header.css';
import sun from '../image/sun.png';
import moon from '../image/moon.png';
import { AppContext } from "../store/AppContext";

const Header = () => {
    const { theme, setTheme } = useContext(AppContext);

    return (
        <div className={`div-header ${theme? '': 'dark'}`}>
            <div className={`div-header-logo ${theme? '': 'dark'}`}>
                <span className={`header-logo ${theme? '': 'dark'}`}>GhostCoders</span>
            </div>
            <span className={`header-name ${theme? '': 'dark'}`}>Класификатор строительных ресурсов</span>
            <div className={`header-div-switch ${theme? '': 'dark'}`}>
                <img 
                    src={sun}
                    className={`header-switch ${theme ? '' : 'none'}`} 
                    onClick={() => setTheme(false)}
                />
                <img 
                    src={moon} 
                    className={`header-switch ${theme ? 'none' : ''}`} 
                    onClick={() => setTheme(true)} 
                />
            </div>
        </div>
    );
}

export default Header;