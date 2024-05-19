import React, { useContext, useState } from "react"
import '../style/Input.css'
import cover from '../image/cover.png'
import coverWhite from '../image/coverWhite.png'
import { AppContext } from "../store/AppContext"


const Input = () => {
    const { theme } = useContext(AppContext)
    const [input, setInput] = useState('')
    const [response, setResponse] = useState('')

    const onSubmit = async () => {
        if (input !== '') {
            const res = await fetch('http://127.0.0.1:8000/classify/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ input })
            });
            const data = await res.json()
            setResponse(data.result.title)
        }
    }

    return (
        <div className={`div-input-block ${theme? '': 'dark'}`}>
            <div className={`div-input-block-child div-input-block-child-img ${theme? '': 'dark'}`}>
                <img src={theme? cover: coverWhite} className={`input-block-img ${theme? '': 'dark'}`} />
            </div>
            <div className={`div-input-block-child div-input-block-child-input ${theme? '': 'dark'}`}>
                <div className={`div-input-block-child-input-child ${theme? '': 'dark'}`}>
                    <span className={`input-block-text ${theme? '': 'dark'}`}>Ведите наименование<br/>стройматериала</span>
                    <input type="text" name="input-title" className={`input-block-input ${theme? '': 'dark'}`} onChange={e => setInput(e.target.value)} />
                    <button className={`input-block-but ${theme? '': 'dark'}`} onClick={onSubmit}>Преобразовать</button>
                </div>
                <div className={`div-input-block-child-input-child ${theme? '': 'dark'}`}>
                    <span className={`input-block-text ${theme? '': 'dark'}`}>Наименование в КСР:</span>
                    <input type="text" className={`input-block-input ${theme? '': 'dark'}`} disabled value={response} />
                </div>
            </div>
        </div>
    )
}

export default Input