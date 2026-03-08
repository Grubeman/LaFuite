import { useState, useEffect } from 'react';
import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import Button from 'react-bootstrap/Button';
import api from '../api.js';
import { ACCESS_TOKEN } from '../constants.js';

function AppNavBar() {
    const [username, setUsername] = useState(null);
    const [isAuthenticated, setIsAuthenticated] = useState(false);

    useEffect(() => {
        api
            .get("/api/user/")
        const checkAuth = async () => {
            const token = localStorage.getItem(ACCESS_TOKEN);
            if (token) {
                setIsAuthenticated(true);
                try {
                    // Récupérer les informations de l'utilisateur connecté
                    const response = await api.get('/api/user/');
                    if (response.data && response.data.username) {
                        setUsername(response.data.username);
                        setIsAuthenticated(true);
                    }
                } catch (error) {
                    console.error("Erreur lors de la récupération de l'utilisateur:", error);
                    setIsAuthenticated(false);
                    setUsername(null);
                }
            } else {
                setIsAuthenticated(false);
                setUsername(null);
            }
        };

        checkAuth();
    }, []);

    return (
        <Navbar expand="lg" className="bg-body-tertiary">
            <Container>
                <Navbar.Brand href="/">La Fuite</Navbar.Brand>
                <Navbar.Toggle aria-controls="basic-navbar-nav" />
                <Navbar.Collapse id="basic-navbar-nav">
                    <Nav className="me-auto">
                        <Nav.Link href="/">Home</Nav.Link>
                    </Nav>
                    <Nav className="ms-auto">
                        {isAuthenticated && username ? (
                            <>
                                <Navbar.Text className="me-3">
                                    Connecté: <strong>{username}</strong>
                                </Navbar.Text>
                                <Button variant="outline-danger" href="/logout" size="sm">
                                    Déconnexion
                                </Button>
                            </>
                        ) : (
                            <Button variant="outline-primary" href="/login" size="sm">
                                Login
                            </Button>
                        )}
                    </Nav>
                </Navbar.Collapse>
            </Container>
        </Navbar>
    );
}

export default AppNavBar;