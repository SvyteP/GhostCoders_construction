import React, { useContext } from "react"
import '../style/Input.css'
import cover from '../image/cover.png'
import { AppContext } from "../store/AppContext"


const Input = () => {
    const { theme } = useContext(AppContext);

    return (
        <div className={`div-input-block ${theme? '': 'dark'}`}>
            <div className={`div-input-block-child div-input-block-child-img ${theme? '': 'dark'}`}>
                <img src={cover} className={`input-block-img ${theme? '': 'dark'}`} />
            </div>
            <div className={`div-input-block-child div-input-block-child-input ${theme? '': 'dark'}`}>
                <div className={`div-input-block-child-input-child ${theme? '': 'dark'}`}>
                    <span className={`input-block-text ${theme? '': 'dark'}`}>Ведите наименование<br/>стройматериала</span>
                    <input type="text" className={`input-block-input ${theme? '': 'dark'}`}/>
                    <button className={`input-block-but ${theme? '': 'dark'}`}>Преобразовать</button>
                </div>
                <div className={`div-input-block-child-input-child ${theme? '': 'dark'}`}>
                    <span className={`input-block-text ${theme? '': 'dark'}`}>Наименование в КСР:</span>
                    <input type="text" className={`input-block-input ${theme? '': 'dark'}`} disabled/>
                </div>
            </div>
        </div>
    )
}

export default Input