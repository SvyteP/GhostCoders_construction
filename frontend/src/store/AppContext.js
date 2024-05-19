import React, { createContext, useState } from 'react';

export const AppContext = createContext();

export const AppProvider = ({ children }) => {
  const [theme, setTheme] = useState(true);
  const [fileUpload, setFileUpload] = useState([]);
  const [fileDownload, setFileDownload] = useState([])
  return (
    <AppContext.Provider value={{theme, setTheme, fileUpload, setFileUpload, fileDownload, setFileDownload }}>
      {children}
    </AppContext.Provider>
  );
};