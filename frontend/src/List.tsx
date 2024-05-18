import React from "react"
import FileDownload from "./components/FileDownload"


const List:React.FC = () => {
    return (
        <div className="container">
            <div className="div-header">
                <span className="header">Отредактированные файлы</span>
            </div>
            <FileDownload />
            <div className="div-panel-container">
                <button className={`panel-but2`}>Загрузить все</button>
            </div>
        </div>
    )
}

export default List