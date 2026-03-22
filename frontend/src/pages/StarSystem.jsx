import { useParams } from "react-router-dom";
import React, {useEffect, useState} from "react";
import api from "../api.js";
import PlanetCard from "../components/PlanetCard.jsx";


function StarSystem() {
    const { id} = useParams();
    const [planets, setPlanets] = useState([])

    const getPlanets = () => {
        api
            .get("/api/planets/" + id +     "/" )
            .then((res) => res.data)
            .then((data) => {
                setPlanets(data);
                console.log(data);
            })
            .catch((err) => alert(err))
    }

    useEffect(() => {
        getPlanets()
    }, [])

    return <div>
        StarSystem {id} page
        {
            planets.map(
                (p) => <PlanetCard planet={p} key={p.id}></PlanetCard>
            )}
    </div>


}

export default StarSystem