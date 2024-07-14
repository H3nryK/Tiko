// src/App.tsx
import React from 'react';
import { BrowserRouter as Router, Route, Routes, Navigate } from 'react-router-dom';
import Header from './components/Header';
import CategoryList from './components/CategoryList';
import VenueList from './components/VenueList';
import VenueDetail from './components/VenueDetail';
import Dashboard from './components/Dashboard';
import Login from './components/Login';

interface PrivateRouteProps {
  component: React.ComponentType;
  path: string;
}

const PrivateRoute = ({ component: Component, ...rest }: PrivateRouteProps) => {
  const isAuthenticated = !!localStorage.getItem('token');
  return (
    <Route
      {...rest}
      element={isAuthenticated ? <Component /> : <Navigate to="/login" />}
    />
  );
};

const App = () => (
  <Router>
    <div>
      <Header />
      <Routes>
        <Route path="/login" element={<Login />} />
        <Route path="/" element={<CategoryList />} />
        <Route path="/categories/:id" element={<VenueList />} />
        <Route path="/venues/:id" element={<VenueDetail />} />
        <Route path="/dashboard" element={Dashboard} />
      </Routes>
    </div>
  </Router>
);

export default App;
