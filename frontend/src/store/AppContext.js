import React, { createContext, useState } from 'react';

export const AppContext = createContext();

export const AppProvider = ({ children }) => {
  const [disable, setDisable] = useState(true);
  const [theme, setTheme] = useState(true);
  return (
    <AppContext.Provider value={{ disable, setDisable, theme, setTheme }}>
      {children}
    </AppContext.Provider>
  );
};