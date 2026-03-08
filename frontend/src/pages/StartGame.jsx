import React, { useEffect, useState } from "react";
import api from "../api";
import Playsession from "../components/Playsession";
import Button from 'react-bootstrap/Button';
import Card from 'react-bootstrap/Card';
import { Outlet } from "react-router-dom";

function StartGame() {
    const [playsessions, setPlaysessions] = useState([])


    const getPlaysessions = () => {
        api
           .get("/api/playsessions/") 
           .then((res) => res.data)
           .then((data) => {
                setPlaysessions(data);
                console.log(data);
           })
           .catch((err) => alert(err))
    }

    useEffect(() => {
        getPlaysessions()
    }, [])

    const deletePlaysession = (id) => {
        api
            .delete(`api/playsessions/delete/${id}/`)
            .then((res) => {
                if (res.status === 204) console.log(`Playsession {id} deleted`)
                else console.log("Error when deleting play session")
                getPlaysessions()
            })
           .catch((err) => alert(err))
    }

    const createPlaysession = () => {
        api
            .post("api/playsessions/create/")
            .then((res) => {
                if (res.status === 201) console.log("New play session created")
                else console.log("Error when creating play session")
                getPlaysessions()
            })
           .catch((err) => alert(err))
    }

    if (playsessions.length > 0) {
        return <div>
            Play sessions list
            {
            playsessions.map(
                (ps) => <Playsession playsession={ps} onDelete={deletePlaysession} key={ps.id}></Playsession>
            )}
            <Card style={{ width: '18rem' }}>
                <Card.Body>
                    <Card.Title>New Session</Card.Title>
                    <Button variant="primary" className="playsession-create" onClick={() => createPlaysession()}>Create</Button>
                </Card.Body>
            </Card>
            <Outlet/>
            </div>
    } else {
        return <div>
            <Card style={{ width: '18rem' }}>
                <Card.Body>
                    <Card.Title>New Session</Card.Title>
                    <Button variant="primary" className="playsession-create" onClick={() => createPlaysession()}>Create</Button>
                </Card.Body>
            </Card>
        </div>
    }

}

export default StartGame