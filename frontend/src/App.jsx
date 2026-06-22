import { useEffect, useState } from "react";

function App() {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/api/products")
      .then((response) => response.json())
      .then((data) => setProducts(data))
      .catch((error) => console.error("error fetching:", error));
  }, []);

  return (
    <div className="min-h-screen bg-gray-800 text-white p-8">
      <h1 className="text-3xl font-bold mb-8 text-center">Product List</h1>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6 max-w-6xl mx-auto">
        {products.map((product) => (
          <div key={product.id} className="bg-gray-700 p-6 rounded-lg shadow-lg">
            <h2 className="text-xl font-semibold mb-2">{product.name}</h2>
            <p className="text-gray-300 text-sm mb-4">{product.description}</p>
            <div className="flex justify-between items-center">
              <span className="text-green-400 font-bold">
                ${product.price}
              </span>
              <span className="text-xs bg-blue-600 px-2 py-1 rounded">
                {product.category?.name}
              </span>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;