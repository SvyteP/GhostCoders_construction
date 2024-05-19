import React, { useCallback, useContext } from 'react';
import { useDropzone } from 'react-dropzone';
import '../style/FileUpload.css';
import iconUpload from '../image/IconUpload.png';
import iconUploadWhite from '../image/IconUploadWhite.png';
import { AppContext } from '../store/AppContext';

const FileUpload = () => {
  const { theme, setFileUpload } = useContext(AppContext);

  const onDrop = useCallback(acceptedFiles => {
    setFileUpload(prevFiles => [...prevFiles, ...acceptedFiles]);
  }, [setFileUpload]);

  const { getRootProps, getInputProps, isDragActive } = useDropzone({ onDrop });

  return (
    <div className="file-upload">
      <div {...getRootProps()} className={`dropzone ${isDragActive ? 'active' : ''} ${theme ? '' : 'dark'}`}>
        <input {...getInputProps()} />
        <div style={{ display: 'flex', alignItems: 'center' }}>
          <img src={theme ? iconUpload : iconUploadWhite} alt="Upload Icon" className="upload-icon" />
          <p>Перетащите файлы сюда или нажмите, чтобы выбрать</p>
        </div>
      </div>
      <div className='div-description'>
        <span className={`description ${theme ? '' : 'dark'}`}>Допустимые форматы: csv, xlsx</span>
      </div>
    </div>
  );
};

export default FileUpload;