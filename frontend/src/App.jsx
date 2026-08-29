import react from 'react'
import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom"
import Login from "./pages/Login"
import Register from "./pages/Register"
import Home from "./pages/Home"
import Play from "./pages/Play"
import NotFound from "./pages/NotFound"
import ProtectedRoute from "./components/ProtectedRoute"
import AppNavBar from "./components/NavBar.jsx";
import StartGame from "./pages/StartGame.jsx";
import StarSystem from "./pages/StarSystem.jsx";
import Planet from "./pages/Planet.jsx";
import Outpost from "./pages/Outpost.jsx";

function Logout() {
  localStorage.clear()
  return <Navigate to="/login" />
}

function RegisterAndLogout() {
  localStorage.clear()
  return <Register />
}

function App() {
  return (
      <div>
      <AppNavBar></AppNavBar>
    <BrowserRouter>
      <Routes>
        <Route
          path="/"
          element={
            <ProtectedRoute>
              <Home />
            </ProtectedRoute>
          }
        >
          <Route index element={<StartGame />} />
          <Route
              path="play/:universe_id"
              element={
                <ProtectedRoute>
                  <Play />
                </ProtectedRoute>
              }
          />
          <Route
                path="play/starsystem/:id"
                element={
                    <ProtectedRoute>
                        <StarSystem />
                    </ProtectedRoute>
                }
            />
            <Route
                path="play/planet/:id"
                element={
                    <ProtectedRoute>
                        <Planet />
                    </ProtectedRoute>
                }
            />
            <Route
                path="play/outpost/:id"
                element={
                    <ProtectedRoute>
                        <Outpost />
                    </ProtectedRoute>
                }
            />
        </Route>
        <Route path="/login" element={<Login />} />
        <Route path="/logout" element={<Logout />} />
        <Route path="/register" element={<RegisterAndLogout />} />
        <Route path="*" element={<NotFound />}></Route>
      </Routes>
    </BrowserRouter>
      </div>
  )
}
export default App
