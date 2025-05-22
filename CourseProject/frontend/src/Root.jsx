import App from './App';
import React from 'react';
import Login from './pages/Login.jsx';
import Basket from './pages/Basket.jsx'
import ProductPage from './pages/ProductPage';
import Registration from './pages/Registration.jsx';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';

function Root() {
  const [userName, setUserName] = React.useState('');

  return (
    <Router>
      <Routes>
        <Route path="/" element={<App userName={userName} />} />
        <Route path="/products/:pk/" element={<ProductPage />} />
        <Route path='/register/' element={<Registration />} />
        <Route path="/login" element={<Login setUserName={setUserName} />} />
        <Route path="/basket/" element={<Basket />} />
      </Routes>
    </Router>
  );
}

export default Root;