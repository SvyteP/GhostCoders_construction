import React, { useCallback, useContext } from "react"
import '../style/Upload.css'
import FileUpload from "./FileUpload"
import File from "./File"
import Panel from "./Panel"
import { AppContext } from "../store/AppContext"


const Upload:React.FC = () => {
    const { disable } = useContext(AppContext)

    return(
        <div>
            <div className="container">
                <div className="div-header-upload">
                    <span className="header">Загрузить файлы</span>
                </div>
                <FileUpload />
                <File />
                <Panel disable={disable}/>
            </div>
        </div>
    )
}

export default Upload