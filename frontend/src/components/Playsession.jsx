import React from "react";

import Button from 'react-bootstrap/Button';
import Card from 'react-bootstrap/Card';

function Playsession({playsession, onDelete}) {
    const formattedDate = new Date(playsession.created_at).toLocaleDateString("fr-FR")


    return (
        <Card style={{ width: '18rem' }}>
            <Card.Body>
                <Card.Title>ID: {playsession.id}</Card.Title>
                <Card.Text>
                    <p className="playsession-universe">Universe {playsession.universe}</p>
                    <p className="playsession-createat">Creation date: {formattedDate}</p>
                    <p className="playsession-stage">Current Stage {playsession.stage}</p>
                </Card.Text>
                <Button variant="primary" className="playsession-delete" onClick={() => onDelete(playsession.id)}>Delete</Button>
            </Card.Body>
        </Card>
    );
}

export default Playsession