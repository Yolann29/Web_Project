import React, { useState } from 'react';

function ModAnn(props) {

    const [title, setTitle] = useState(null);
    const [description, setDescription] = useState(null);

    const handleSubmit = async (sub) => {
        sub.preventDefault();

        const data = {
            'id': props.id,
            'title': title,
            'description': description,
        };
        console.log(data);

        try {
            const response = await fetch('http://127.0.0.1:8000/view', {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json'
            },
                body: JSON.stringify(data)
            });

            if (!response.ok) {
                throw new Error('Network response was not ok');
            }

            console.log(response);
        } catch (error) {
            console.error('Error fetching data:', error);
        }
    };

    const handledelete = async (sub) => {
        sub.preventDefault();
    }

    return (
        <div>
            <label id="title">Title</label>
            <input type="text" id="title" name="title" value={title} onChange={(ev) => setTitle(ev.target.value)} />
            <label id="description">Description</label>
            <input type="text" id="description" name="description" value={description} onChange={(ev) => setDescription(ev.target.value)} />
            <input type="submit" onClick={handleSubmit} />
            <button onClick={handledelete}>Delete</button>
        </div>
    );
}

export default ModAnn;