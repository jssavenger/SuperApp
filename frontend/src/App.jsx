import { BrowserRouter, Routes, Route } from "react-router-dom";
// pages
import MainPage from "./pages/MainPage";
import DashBoard from "./pages/Dashboard";

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<MainPage />} />
        <Route path="/dashboard" element={<DashBoard />} />
      </Routes>
    </BrowserRouter>
  );
}
