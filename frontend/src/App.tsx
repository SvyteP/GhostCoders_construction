import React from 'react';
import { Routes, Route, BrowserRouter } from 'react-router-dom';
import List from './List';
import Home from './Home';

function App() {
    return (
        <BrowserRouter>
            <Routes>
                <Route path='/' element={<Home />} />
                <Route path='list' element={<List />} />
                <Route path='*' element={<Home />} />
            </Routes>
        </BrowserRouter>
    );
}

export default App;
