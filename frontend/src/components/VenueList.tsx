// src/components/VenueList.tsx
import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { useParams } from 'react-router-dom';

interface Venue {
  id: number;
  name: string;
  description: string;
  categoryId: number;
}

const VenueList = () => {
  const { id } = useParams<{ id: string }>();
  const [venues, setVenues] = useState<Venue[]>([]);

  useEffect(() => {
    const token = localStorage.getItem('token');
    axios.get(`http://localhost:8000/api/categories/${id}/venues/`, {
      headers: {
        'Authorization': `Token ${token}`
      }
    })
      .then(response => setVenues(response.data))
      .catch(error => console.error(error));
  }, [id]);

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-2xl font-bold mb-4">Venues in Category {id}</h1>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        {venues.map((venue: Venue) => (
          <div key={venue.id} className="bg-white p-4 shadow rounded">
            <h2 className="text-xl font-semibold">{venue.name}</h2>
            <p>{venue.description}</p>
          </div>
        ))}
      </div>
    </div>
  );
};

export default VenueList;
