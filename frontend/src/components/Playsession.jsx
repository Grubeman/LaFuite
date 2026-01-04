import React from "react";

function Playsession({playsession}) {
    return <div className="playsession-container" style={{border: "1px solid black"}}>
        <p className="playsession-id">{playsession.id}</p>
        <p className="playsession-id">{playsession.universe}</p>
    </div>

}

export default Playsession