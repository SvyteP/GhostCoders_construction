import React, { useContext, useEffect } from "react";
import { AppContext } from "../store/AppContext";
import '../style/FileDownload.css';
import iconFile from '../image/IconFile.png';
import iconFileWhite from '../image/IconFileWhite.png';
import download from '../image/download.png';
import downloadWhite from '../image/downloadWhite.png';
import { useNavigate } from "react-router-dom";

const FileDownload = () => {
    const { theme, fileDownload } = useContext(AppContext);
    const navigate = useNavigate();

    useEffect(() => {
        if (fileDownload.length === 0) {
            navigate('/');
        }
    }, [fileDownload, navigate]);

    const handleDownload = (fileUrl) => {
        const newTab = window.open(fileUrl, '_blank');
        if (newTab) {
            newTab.onload = () => {
                newTab.close();
            };
        }
    };

    const filteredFiles = fileDownload.filter(file => file.file_name !== 'all');

    return (
        <div className="file-download-list">
            {filteredFiles.map((file, index) => (
                <div key={index} className={`file-download-item ${theme ? '' : 'dark'}`}>
                    <div className="file-div-name">
                        <img src={theme ? iconFile : iconFileWhite} alt="File Icon" className="file-icon" />
                        <div className="div-file-name">
                            <span className={`file-name ${theme ? '' : 'dark'}`}>{file.file_name}</span>
                        </div>
                    </div>
                    <img className="file-download" src={theme ? download : downloadWhite} onClick={() => handleDownload(file.file_url)} />
                </div>
            ))}
        </div>
    );
};

export default FileDownload;