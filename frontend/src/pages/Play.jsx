import React, {useEffect, useState} from "react";
import api from "../api.js";
import PlaysessionCard from "../components/PlaysessionCard.jsx";
import StarsystemCard from "../components/StarsystemCard.jsx";
import {useParams} from "react-router-dom";

function Play() {
    const [starsystems, setStarSystems] = useState([])
    const {universe_id} = useParams()
    const getStarSystems = () => {
        api
            .get("/api/starsystems/"
            + universe_id + "/")
            .then((res) => res.data)
            .then((data) => {
                setStarSystems(data);
                console.log(data);
            })
            .catch((err) => alert(err))
    }

    useEffect(() => {
        getStarSystems()
    }, [])

    return <div>
        {
            starsystems.map(
                (ss) => <StarsystemCard starsystem={ss} key={ss.id}></StarsystemCard>
        )}
    </div>

}

export default Play