// src/components/VenueDetail.tsx
import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { useParams } from 'react-router-dom';

const VenueDetail = () => {
  const { id } = useParams();
  const [venue, setVenue] = useState(null);

  useEffect(() => {
    axios.get(`http://localhost:8000/api/venues/${id}/`)
      .then(response => setVenue(response.data))
      .catch(error => console.error(error));
  }, [id]);

  if (!venue) return <div>Loading...</div>;

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-2xl font-bold mb-4">{venue.name}</h1>
      <p>{venue.description}</p>
      <button className="mt-4 bg-blue-500 text-white px-4 py-2 rounded">Book Now</button>
    </div>
  );
};

export default VenueDetail;
