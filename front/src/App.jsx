import { BrowserRouter, Routes, Route } from "react-router-dom";
import "./App.css";
import { Navbar } from "./components/Navbar";

import { Home } from "./views/Home";
import { DetailsView } from "./views/DetailsView";
import { PlanetsView } from "./views/PlanetsView";
import { NotFound } from "./views/NotFound";
import { Register } from "./views/Register";
import { Login } from "./views/Login";
import { UserSpace } from "./views/UserSpace";

function App() {
  return (
    <BrowserRouter basename="/">
      <Navbar />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/characters/:id" element={<DetailsView />} />
        <Route path="/planets/:id" element={<PlanetsView />} />
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />
        <Route path="/private" element={<UserSpace />} />
        <Route path="*" element={<NotFound />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
