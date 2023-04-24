// General Imports
import { Routes, Route } from "react-router-dom";
import "./App.css";

// Pages Imports
import HomePage from "./pages/HomePage/HomePage";
import LoginPage from "./pages/LoginPage/LoginPage";
import RegisterPage from "./pages/RegisterPage/RegisterPage";
import TeacherPage from "./pages/TeacherPage/TeacherPage";
import StudentPage from "./pages/StudentPage/StudentPage";

// Component Imports
import Navbar from "./components/NavBar/NavBar";
import Footer from "./components/Footer/Footer";
import Store from "./components/Store/Store";
import ShoppingCart from "./components/ShoppingCart/ShoppingCart";
import Transactions from "./components/Transactions/Transactions";

// Util Imports
import PrivateRoute from "./utils/PrivateRoute";

function App() {
  return (
    <div>
      <Navbar />
      <Routes>
        <Route
          path="/"
          element={
            <PrivateRoute>
              <HomePage />
            </PrivateRoute>
          }
        />
        <Route path="/teacher" element={<TeacherPage/>}/>
        <Route path="/student" element={<StudentPage/>}/>
        <Route path="/store" element={<Store/>}/>
        <Route path="/cart" element={<ShoppingCart/>}/>
        <Route path="/transactions" element={<Transactions/>}/>
        <Route path="/register" element={<RegisterPage />} />
        <Route path="/login" element={<LoginPage />} />
      </Routes>
      <Footer />
    </div>
  );
}

export default App;
