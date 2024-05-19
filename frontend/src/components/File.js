import React, { useContext } from "react";
import '../style/File.css';
import iconFile from '../image/IconFile.png';
import iconFileWhite from '../image/IconFileWhite.png';
import { AppContext } from "../store/AppContext";

const File = () => {
    const { theme, fileUpload, setFileUpload } = useContext(AppContext);

    const handleRemove = (index) => {
        setFileUpload(prevFiles => prevFiles.filter((_, i) => i !== index));
    };

    return (
        <div className="div-file-list">
            <div className="file-list">
                {fileUpload.map((file, index) => (
                    <div key={index} className={`file-item ${theme ? '' : 'dark'}`}>
                        <img src={theme ? iconFile : iconFileWhite} alt="File Icon" className="file-icon" />
                        <div className={`div-file-name ${theme ? '' : 'dark'}`}>
                            <span className={`file-name ${theme ? '' : 'dark'}`}>{file.name}</span>
                        </div>
                        <button className="file-remove" onClick={() => handleRemove(index)}>&times;</button>
                    </div>
                ))}
            </div>
        </div>
    );
};

export default File;