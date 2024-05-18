import React from "react"
import '../style/File.css'
import iconFile from '../image/IconFile.png'


const File = () => {
    return (
        <div className="div-file-list">
            <div className="file-list">
                <div className="file-item">
                    <img src={iconFile} alt="File Icon" className="file-icon" />
                    <div className="div-file-name">
                        <span className="file-name">Fileas_234.pdf</span>
                    </div>
                    <button className="file-remove">&times;</button>
                </div>
            </div>
        </div>
    )
}

export default File