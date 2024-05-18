import React from "react"
import Header from "./components/Header"
import './style/Home.css'
import Upload from "./components/Upload"
import Input from "./components/Input"


const Home:React.FC = () => {
    return (
        <div className="home">
            <Header />
            <Input />
            <Upload />
        </div>
    )
}

export default Home