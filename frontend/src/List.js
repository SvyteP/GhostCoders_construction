import React, { useContext } from "react"
import FileDownload from "./components/FileDownload"
import { AppContext } from "./store/AppContext"
import Header from "./components/Header"


const List = () => {
    const { theme, fileDownload } = useContext(AppContext)

    const handleDownload = (fileUrl) => {
        const newTab = window.open(fileUrl, '_blank');
        if (newTab) {
            newTab.onload = () => {
                newTab.close();
            };
        }
    };

    const allFile = fileDownload.find(file => file.file_name === 'all').file_url;

    return (
        <div className={`home ${theme? '': 'dark'}`}>
            <Header />
            <div className="container">
                <div className="div-header-upload">
                    <span className={`header ${theme? '': 'dark'}`}>Загрузить файлы</span>
                </div>
                <FileDownload />
                <div className="div-panel-container">
                    <button className={`panel-but2`} onClick={() => {handleDownload(allFile)}}>Загрузить все</button>
                </div>
            </div>
        </div>
    )
}

export default List