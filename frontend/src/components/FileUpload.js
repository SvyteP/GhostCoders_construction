import React, { useCallback } from 'react';
import { useDropzone } from 'react-dropzone';
import '../style/FileUpload.css';
import iconUpload from '../image/IconUpload.png'

const FileUpload = () => {
  const onDrop = useCallback(acceptedFiles => {
    // Обработка загруженных файлов
    console.log(acceptedFiles);
  }, []);

  const { getRootProps, getInputProps, isDragActive } = useDropzone({ onDrop });

  return (
    <div className="file-upload">
      <div {...getRootProps()} className={`dropzone ${isDragActive ? 'active' : ''}`}>
        <input {...getInputProps()} />
        {
            <div style={{display: 'flex', alignItems: 'center'}}>
            <img src={iconUpload} alt="Upload Icon" className="upload-icon" />
            <p>Перетащите файлы сюда или нажмите, чтобы выбрать</p>
            </div>
        }
      </div>
      <div className='div-description'>
        <span className='description'>Допустимые форматы: pdf, xls</span>
      </div>
    </div>
  );
};

export default FileUpload;