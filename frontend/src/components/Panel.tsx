import React from "react"
import '../style/Panel.css'


const Panel:React.FC<{disable: boolean}> = (props)  => {
    return (
        <div className="div-panel-container">
            <button className={`panel-but1 ${props.disable? "disable": ""}`}>Отмена</button>
            <button className={`panel-but2 ${props.disable? "disable": ""}`}>Продолжить</button>
        </div>
    )
}

export default Panel