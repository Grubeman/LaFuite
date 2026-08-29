import { useParams } from "react-router-dom";
import React, { useEffect, useMemo, useRef, useState } from "react";
import * as d3 from "d3";
import api from "../api.js";


function Outpost() {
    const { id } = useParams();
    const svgRef = useRef(null);
    const data = useMemo(
        () => [
            {
                x: 100,
                y: 125,
                width: 100,
                height: 50,
                fill: "blue"
            },
            {
                x: 150,
                y: 200,
                width: 100,
                height: 50,
                fill: "red"
            }
        ],
        []
    );
    const controlledRect = data[data.length - 1];
    const [outpost, setOutpost] = useState({});
    const [buildings, setBuildings] = useState([]);
    const [angle, setAngle] = useState(0);
    const [pos, setPos] = useState({ x: controlledRect.x, y: controlledRect.y });
    const [controlledSize, setControlledSize] = useState({
        width: controlledRect.width,
        height: controlledRect.height
    });
    const getOutpost = () => {
        console.log("get outpost", id)
        api
            .get("/api/outpost/" + id +     "/" )
            .then((res) => res.data)
            .then((data) => {
                console.log(data)
                setOutpost(data)
                setControlledSize({ width: data.width * 50, height: data.height * 50 });
            })
            .catch((err) => alert(err))
    }

    const getBuildings = () => {
        console.log("get buildings for outposts", id)
        api
            .get("/api/buildings/" + id +     "/" )
            .then((res) => res.data)
            .then((data) => {
                data = data[0]
                console.log("data", data)
                setBuildings(data);
                data = [{
                    x: 100,
                    y: 125,
                    width: 100,
                    height: 50,
                    fill: "blue"
                }]
                const svg = d3.select(svgRef.current);
                svg.selectAll("*").remove(); // nettoie avant de (re)créer
                svg
                    .selectAll("rect")
                    .data(data)
                    .enter()
                    .append("rect")
                    .attr("x", (d) => d.x)
                    .attr("y", (d) => d.y)
                    .attr("width", (d) => d.width)
                    .attr("height", (d) => d.height)
                    .attr("fill", (d) => d.fill)
                    .attr("class", (_, i) => (i === data.length - 1 ? "controlled-rect" : "static-rect"))
                    .on("click", function (event, d) {
                        svg.selectAll("rect")
                            .classed("controlled-rect", false)
                            .classed("static-rect", true);

                        d3.select(event.currentTarget)
                            .classed("controlled-rect", true)
                            .classed("static-rect", false);

                        setPos({ x: d.x, y: d.y });
                        setControlledSize({ width: d.width, height: d.height });
                    });
            })
            .catch((err) => alert(err))
    }

    // Crée le rectangle une seule fois avec D3
    useEffect(() => {
        getOutpost()
        //getBuildings()
    }, []);

    useEffect(() => {
        d3.select(svgRef.current)
            .attr("width", controlledSize.width)
            .attr("height", controlledSize.height)
    }, [controlledSize.height, controlledSize.width]);

    // Met à jour position et rotation via D3
    useEffect(() => {
        d3.select(svgRef.current)
            .select(".controlled-rect")
            .attr("x", pos.x)
            .attr("y", pos.y)
            .attr(
                "transform",
                `rotate(${angle}, ${pos.x + controlledSize.width / 2}, ${pos.y + controlledSize.height / 2})`
            );
    }, [angle, pos, controlledSize.height, controlledSize.width]);

    // Touches : A/E pour rotation, flèches pour translation
    useEffect(() => {
        const handleKeyDown = (e) => {
            if (e.key === "a" || e.key === "A") {
                setAngle((prev) => prev - 90);
            } else if (e.key === "e" || e.key === "E") {
                setAngle((prev) => prev + 90);
            } else if (e.key === "ArrowLeft") {
                setPos((prev) => ({ ...prev, x: prev.x - 50 }));
            } else if (e.key === "ArrowRight") {
                setPos((prev) => ({ ...prev, x: prev.x + 50 }));
            } else if (e.key === "ArrowUp") {
                setPos((prev) => ({ ...prev, y: prev.y - 50 }));
            } else if (e.key === "ArrowDown") {
                setPos((prev) => ({ ...prev, y: prev.y + 50 }));
            }
        };
        window.addEventListener("keydown", handleKeyDown);
        return () => window.removeEventListener("keydown", handleKeyDown);
    }, []);

    return (
        <div>
            <h2>Outpost {id} page</h2>
            <p>Latitude {outpost?.latitude}, longitude {outpost?.longitude}</p>
            <p>A / E : rotation &nbsp;|&nbsp; ← → ↑ ↓ : translation (50px)</p>
            <svg ref={svgRef} width={300} height={300} style={{ border: "1px solid #ccc" }} />
        </div>
    );
}

export default Outpost;
