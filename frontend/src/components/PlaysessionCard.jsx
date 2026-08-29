import React, {useEffect, useState} from "react";

import Button from 'react-bootstrap/Button';
import Card from 'react-bootstrap/Card';
import api from "../api.js";

import { useNavigate } from "react-router-dom";

function PlaysessionCard({playsession, onDelete}) {

    let navigate = useNavigate();
    const routeChange = (location_type, location_id) =>{
        console.log(location_type, location_id)
        let path = 0
        if (location_type === 1) {
            path = `play/planet/`+ location_id + "/";
        } else {
            path = `play/`+ location_id + "/";
        }
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
                    <p className="playsession-location">Location {playsession.location ?? "—"}</p>
                    <p className="playsession-location_id">Location ID {playsession.location_id ?? "—"}</p>

                </Card.Body>
                <Button variant="primary" className="playsession-play" onClick={() =>routeChange(playsession.location, playsession.location_id)}>Play</Button>
                <Button variant="danger" className="playsession-delete" onClick={() => onDelete(playsession.id)}>Delete</Button>
            </Card.Body>
        </Card>
    );
}

export default PlaysessionCard