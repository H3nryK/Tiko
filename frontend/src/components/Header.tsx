// src/components/Header.tsx
import React from 'react';

const Header:React.FC = () => (
  <header className="bg-gray-800 text-white p-4 flex justify-between items-center">
    <h1 className="text-xl font-bold">Venue Booking</h1>
    <nav>
      <a href="/" className="mx-2">Home</a>
      <a href="/contact" className="mx-2">Contact</a>
      <a href="/login" className="mx-2">Login</a>
    </nav>
  </header>
);

export default Header;
