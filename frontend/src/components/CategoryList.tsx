// src/components/CategoryList.tsx
import React, { useEffect, useState } from 'react';
import axios from 'axios';

const CategoryList = () => {
  const [categories, setCategories] = useState([]);

  useEffect(() => {
    const token = localStorage.getItem('token');
    axios.get('http://localhost:8000/api/categories/', {
      headers: {
        'Authorization': `Token ${token}`
      }
    })
      .then(response => setCategories(response.data))
      .catch(error => console.error(error));
  }, []);

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-2xl font-bold mb-4">Venue Categories</h1>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        {categories.map((category: any) => (
          <div key={category.id} className="bg-white p-4 shadow rounded">
            <h2 className="text-xl font-semibold">{category.name}</h2>
          </div>
        ))}
      </div>
    </div>
  );
};

export default CategoryList;
