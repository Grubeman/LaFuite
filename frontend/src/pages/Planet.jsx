import { useParams } from "react-router-dom";
import React, {useEffect, useState} from "react";
import api from "../api.js";
import PlanetCard from "../components/PlanetCard.jsx";


function Planet() {
    const { id} = useParams();

    return <div>
        Planet {id} page
    </div>


}

export default Planet