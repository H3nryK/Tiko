// src/components/Dashboard.tsx
import React, { useState } from 'react';
import axios from 'axios';

const Dashboard:React.FC = () => {
  const [venueName, setVenueName] = useState('');
  const [venueDescription, setVenueDescription] = useState('');
  const [categoryId, setCategoryId] = useState('');

  const handleCreateVenue = () => {
    axios.post('http://localhost:8000/api/venues/', {
      name: venueName,
      description: venueDescription,
      category: categoryId,
    })
      .then(response => {
        console.log('Venue created:', response.data);
        setVenueName('');
        setVenueDescription('');
        setCategoryId('');
      })
      .catch(error => console.error(error));
  };

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-2xl font-bold mb-4">Dashboard</h1>
      <div>
        <input
          type="text"
          placeholder="Venue Name"
          value={venueName}
          onChange={e => setVenueName(e.target.value)}
          className="block mb-2 p-2 border"
        />
        <textarea
          placeholder="Venue Description"
          value={venueDescription}
          onChange={e => setVenueDescription(e.target.value)}
          className="block mb-2 p-2 border"
        />
        <input
          type="text"
          placeholder="Category ID"
          value={categoryId}
          onChange={e => setCategoryId(e.target.value)}
          className="block mb-4 p-2 border"
        />
        <button onClick={handleCreateVenue} className="bg-blue-500 text-white px-4 py-2 rounded">Create Venue</button>
      </div>
    </div>
  );
};

export default Dashboard;
