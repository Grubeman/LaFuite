import Button from 'react-bootstrap/Button';
import Card from 'react-bootstrap/Card';
import React from "react";
import {useNavigate} from "react-router-dom";

function StarsystemCard({starsystem}) {
    const formattedDate = new Date(starsystem.created_at).toLocaleDateString("fr-FR")

    let navigate = useNavigate();
    const routeChange = () =>{
        let path = `/play/starsystem/${starsystem.id}`;
        navigate(path);
    }

    return (
        <Card style={{ width: '18rem' }}>
            <Card.Body>
                <Card.Title>ID: {starsystem.id}</Card.Title>
                <Card.Body>
                    <p className="starsystem-universe">Universe {starsystem?.universe ?? "—"}</p>
                    <p className="starsystem-createat">Creation date: {formattedDate}</p>

                </Card.Body>

                <Button variant="primary" className="starsystem-go" onClick={routeChange}>Go</Button>
            </Card.Body>
        </Card>
    );
}

export default StarsystemCard