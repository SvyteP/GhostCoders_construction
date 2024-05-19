import React, { useContext } from "react"
import '../style/Panel.css'
import { AppContext } from "../store/AppContext"


const Panel = (props)  => {
    const { fileUpload } = useContext(AppContext)
    const isFileUploadEmpty = fileUpload.length === 0;

    return (
        <div className="div-panel-container">
            <button className={`panel-but1 ${isFileUploadEmpty? "disable": ""}`} disabled={isFileUploadEmpty}>Отмена</button>
            <button className={`panel-but2 ${isFileUploadEmpty? "disable": ""}`} disabled={isFileUploadEmpty}>Продолжить</button>
        </div>
    )
}

export default Panel