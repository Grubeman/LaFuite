import { useParams } from "react-router-dom";
import React, { useEffect, useRef, useState } from "react";
import * as d3 from "d3";


function Planet() {
    const { id } = useParams();
    const svgRef = useRef(null);
    const [angle, setAngle] = useState(0);
    const [pos, setPos] = useState({ x: 100, y: 125 });

    // Crée le rectangle une seule fois avec D3
    useEffect(() => {
        const svg = d3.select(svgRef.current);
        svg.selectAll("*").remove(); // nettoie avant de (re)créer
        svg.append("rect")
            .attr("x", 100)
            .attr("y", 125)
            .attr("width", 100)
            .attr("height", 50)
            .attr("fill", "red");
    }, []);

    // Met à jour position et rotation via D3
    useEffect(() => {
        d3.select(svgRef.current)
            .select("rect")
            .attr("x", pos.x)
            .attr("y", pos.y)
            .attr("transform", `rotate(${angle}, ${pos.x + 50}, ${pos.y + 25})`);
    }, [angle, pos]);

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
            <h2>Planet {id} page</h2>
            <p>A / E : rotation &nbsp;|&nbsp; ← → ↑ ↓ : translation (50px)</p>
            <svg ref={svgRef} width={300} height={300} style={{ border: "1px solid #ccc" }} />
        </div>
    );
}

export default Planet;
