import { useEffect, useState } from "react";
import api from "../api";
import Playsession from "../components/Playsession";

function Home() {
    const [playsessions, setPlaysessions] = useState([])

    useEffect(() => {
        getPlaysessions()
    }, [])

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

    const createPlaysession = (e) => {
        e.preventDefault();
        api
            .post("api/playsessions/create")
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
                (ps) => <Playsession playsession={ps} key={ps.id}></Playsession>
            )}
            </div>
    } else {
        return <div>
            No play sessions detected
            <form onSubmit={createPlaysession}>
                <input type="submit" value="Submit"></input>
            </form>
        </div>
    }

}

export default Home