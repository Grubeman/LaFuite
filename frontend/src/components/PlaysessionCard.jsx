import React, {useEffect, useState} from "react";

import Button from 'react-bootstrap/Button';
import Card from 'react-bootstrap/Card';
import api from "../api.js";

import { useNavigate } from "react-router-dom";

function PlaysessionCard({playsession, onDelete}) {

    let navigate = useNavigate();
    const routeChange = (universe_id) =>{
        console.log(universe_id)
        let path = `play/`+ universe_id + "/";
        navigate(path);
    }

    const formattedDate = new Date(playsession.created_at).toLocaleDateString("fr-FR")

    return (
        <Card style={{ width: '18rem' }}>
            <Card.Body>
                <Card.Title>ID: {playsession.id}</Card.Title>
                <Card.Body>
                    <p className="playsession-universe">Universe {playsession.universe?.id ?? "—"}</p>
                    <p className="playsession-createat">Creation date: {formattedDate}</p>
                    <p className="playsession-stage">Current Stage {playsession.stage}</p>
                    <p className="playsession-starship">Starship {playsession.starship?.name ?? "—"}</p>

                </Card.Body>
                <Button variant="primary" className="playsession-play" onClick={() =>routeChange(playsession.universe.id)}>Play</Button>
                <Button variant="danger" className="playsession-delete" onClick={() => onDelete(playsession.id)}>Delete</Button>
            </Card.Body>
        </Card>
    );
}

export default PlaysessionCard