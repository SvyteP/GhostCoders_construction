import React, { useCallback, useContext } from "react"
import '../style/Upload.css'
import FileUpload from "./FileUpload"
import File from "./File"
import Panel from "./Panel"
import { AppContext } from "../store/AppContext"


const Upload:React.FC = () => {
    const { theme } = useContext(AppContext)

    return(
        <div>
            <div className="container">
                <div className="div-header-upload">
                    <span className={`header ${theme? '': 'dark'}`}>Загрузить файлы</span>
                </div>
                <FileUpload />
                <File />
                <Panel/>
            </div>
        </div>
    )
}

export default Upload