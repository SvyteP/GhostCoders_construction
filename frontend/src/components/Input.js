import React, { useContext } from "react"
import '../style/Input.css'
import cover from '../image/cover.png'
import { AppContext } from "../store/AppContext"


const Input = () => {
    const { theme } = useContext(AppContext);

    return (
        <div className={`div-input-block `}>
            <div className={`div-input-block-child div-input-block-child-img `}>
                <img src={cover} className={`input-block-img `} />
            </div>
            <div className={`div-input-block-child div-input-block-child-input `}>
                <div className={`div-input-block-child-input-child `}>
                    <span className={`input-block-text `}>Ведите наименование<br/>стройматериала</span>
                    <input type="text" className={`input-block-input `}/>
                    <button className={`input-block-but `}>Преобразовать</button>
                </div>
                <div className={`div-input-block-child-input-child `}>
                    <span className={`input-block-text `}>Наименование в КСР:</span>
                    <input type="text" className={`input-block-input `} disabled/>
                </div>
            </div>
        </div>
    )
}

export default Input