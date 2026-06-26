import React from "react";
import { Link } from "react-router-dom";

// Fetching backend base URL from environment variables
const BASE_URL = import.meta.env.VITE_DJANGO_BASE_URL;

function ProductCard({ product }) {
  return (
    <Link to={`/product/${product.id}`} className="cursor-pointer">
      <div className="bg-white rounded-xl shadow-md hover:shadow-lg hover:scale-105 transition-all p-4 duration-300">
        <div className="w-full h-48 overflow-hidden rounded-t-xl">
          <img
            src={`${BASE_URL}${product.image}`}
            alt={product.name}
            className="w-full h-full object-cover"
          />
        </div>
        <div className="mt-4">
          <h2 className="text-lg font-semibold text-gray-800 truncate">
            {product.name}
          </h2>
          <p className="font-medium text-gray-600 mt-1">${product.price}</p>
        </div>
      </div>
    </Link>
  );
}

export default ProductCard;
