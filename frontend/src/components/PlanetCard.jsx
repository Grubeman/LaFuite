import Button from 'react-bootstrap/Button';
import Card from 'react-bootstrap/Card';
import React from "react";
import {useNavigate} from "react-router-dom";

function PlanetCard({planet}) {
    const formattedDate = new Date(planet.created_at).toLocaleDateString("fr-FR")

    let navigate = useNavigate();
    const routeChange = () =>{
        let path = `/play/planet/${planet.id}`;
        navigate(path);
    }

    return (
        <Card style={{ width: '18rem' }}>
            <Card.Body>
                <Card.Title>ID: {planet.id}</Card.Title>
                <Card.Body>
                    <p className="planet-starsystem">StarSystem {planet?.star_system ?? "—"}</p>
                    <p className="planet-name">Planet {planet.name}</p>
                    <p className="planet-createat">Creation date: {formattedDate}</p>

                </Card.Body>

                <Button variant="primary" className="planet-go" onClick={routeChange}>Land</Button>
            </Card.Body>
        </Card>
    );
}

export default PlanetCard