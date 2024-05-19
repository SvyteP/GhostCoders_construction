import React, { createContext, useState } from 'react';

export const AppContext = createContext();

export const AppProvider = ({ children }) => {
  const [theme, setTheme] = useState(true);
  const [fileUpload, setFileUpload] = useState([]);
  return (
    <AppContext.Provider value={{theme, setTheme, fileUpload, setFileUpload }}>
      {children}
    </AppContext.Provider>
  );
};