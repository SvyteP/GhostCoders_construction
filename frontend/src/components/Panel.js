import React, { useContext } from "react";
import '../style/Panel.css';
import { AppContext } from "../store/AppContext";
import { useNavigate } from "react-router-dom";

const Panel = () => {
    const navigate = useNavigate()

    const { fileUpload, setFileUpload, setFileDownload } = useContext(AppContext);
    const isFileUploadEmpty = fileUpload.length === 0;

    const handleUpload = async () => {
        if (isFileUploadEmpty) return;

        const formData = new FormData();
        fileUpload.forEach((file) => {
            formData.append('file', file);
        });

        try {
            const response = await fetch('http://127.0.0.1:8000/upload/', {
                method: 'POST',
                body: formData,
            });

            if (response.ok) {
                const data = await response.json();
                console.log('Успех:', data);
                setFileDownload(data.files)
                navigate('/list')
                // Обрабатываем полученные данные JSON
            } else {
                console.error('Ошибка:', response.statusText);
            }
        } catch (error) {
            console.error('Ошибка:', error);
        }
    };

    const handleClose = () => {
        setFileUpload([])
    }

    return (
        <div className="div-panel-container">
            <button className={`panel-but1 ${isFileUploadEmpty ? "disable" : ""}`} disabled={isFileUploadEmpty} onClick={handleClose}>Отмена</button>
            <button className={`panel-but2 ${isFileUploadEmpty ? "disable" : ""}`} disabled={isFileUploadEmpty} onClick={handleUpload}>Продолжить</button>
        </div>
    );
};

export default Panel;
