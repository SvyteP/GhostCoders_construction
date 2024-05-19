import React, { useContext } from "react"
import Header from "./components/Header"
import './style/Home.css'
import Upload from "./components/Upload"
import Input from "./components/Input"
import { AppContext } from "./store/AppContext"


const Home:React.FC = () => {
    const { theme } = useContext(AppContext);

    return (
        <div className={`home ${theme? '': 'dark'}`}>
            <Header />
            <Input />
            <Upload />
        </div>
    )
}

export default Home