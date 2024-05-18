import React from "react"
import '../style/FileDownload.css'
import iconFile from '../image/IconFile.png'


const FileDownload = () => {
    return (
        <div className="file-download-list">
            <div className="file-download-item">
                <div className="file-div-name">
                    <img src={iconFile} alt="File Icon" className="file-icon" />
                    <div className="div-file-name">
                        <span className="file-name">Fileas_234.pdf</span>
                    </div>
                </div>
                <button className="file-remove">&times;</button>
            </div>
            <div className="file-download-item">
                <div className="file-div-name">
                    <img src={iconFile} alt="File Icon" className="file-icon" />
                    <div className="div-file-name">
                        <span className="file-name">Fileas_234.pdf</span>
                    </div>
                </div>
                <button className="file-remove">&times;</button>
            </div>
        </div>
    )
}

export default FileDownload