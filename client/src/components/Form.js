import React, { useState } from 'react'

const Form = () => {

    const [url, setUrl] = useState("")

    const handleSubmit = async (e) => {
        e.preventDefault()

        await fetch('http://127.0.0.1:5000/home', {  
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(url) 
        })
        setUrl('')
    }

    const updateInput = e => {
        const input = e.target.value
        setUrl(input)
        // console.log(input)
    }

    return (
        <form onSubmit={handleSubmit}>
            <label htmlFor="input-name">Enter A Url</label>
            <input id="input-name" type="text" value={url} onChange={updateInput} />
            <input type="Submit" value="Search" />
        </form>
    )
}

export default Form