import React from 'react';
// 1. Import useCart instead of CartContext
import { useCart } from '../context/CartContext';

const CartPage = () => {
    // 2. Consume cart data and actions directly from useCart()
    const { cartItems, total, updateQuantity, removeFromCart } = useCart();
    
    // NOTE: If you need VITE_DJANGO_BASE_URL for images, grab it from import.meta.env
    const baseUrl = import.meta.env.VITE_DJANGO_BASE_URL || "";

    // Render an empty state view if there are no items in the cart
    if (!cartItems || cartItems.length === 0) {
        return (
            <div className="flex flex-col items-center justify-center p-12 text-center min-h-[50vh]">
                <h2 className="text-2xl font-bold text-gray-800 mb-2">Your Cart is Empty</h2>
                <p className="text-gray-500">Add some products to your cart to see them here!</p>
            </div>
        );
    }

    return (
        <div className="max-w-4xl mx-auto p-6 bg-white rounded-lg shadow-sm my-8">
            <h2 className="text-3xl font-extrabold text-gray-900 mb-6">Your Cart</h2>
            <div className="border-b border-gray-200 mb-4"></div>
            
            {/* Cart Items List */}
            <div className="divide-y divide-gray-200">
                {cartItems.map((item) => (
                    <div 
                        key={item.id} 
                        className="flex flex-col sm:flex-row items-center justify-between py-6 gap-4"
                    >
                        {/* Product Image */}
                        <div className="w-24 h-24 shrink-0 bg-gray-100 rounded-md overflow-hidden">
                            <img 
                                src={`${baseUrl}${item.product_image}`} 
                                alt={item.product_name} 
                                className="w-full h-full object-cover"
                            />
                        </div>

                        {/* Product Info Description */}
                        <div className="flex-1 text-center sm:text-left">
                            <h4 className="text-lg font-semibold text-gray-800">{item.product_name}</h4>
                            <p className="text-gray-600 mt-1">Price: ${item.product_price}</p>
                        </div>

                        {/* Quantity Adjustment Controls */}
                        <div className="flex items-center bg-gray-50 border border-gray-200 rounded-lg p-1">
                            <button 
                                onClick={() => updateQuantity(item.id, item.quantity - 1)}
                                className="px-3 py-1 text-gray-600 hover:bg-gray-200 rounded-md transition font-semibold"
                            >
                                -
                            </button>
                            <span className="px-4 font-bold text-gray-800 text-sm">{item.quantity}</span>
                            <button 
                                onClick={() => updateQuantity(item.id, item.quantity + 1)}
                                className="px-3 py-1 text-gray-600 hover:bg-gray-200 rounded-md transition font-semibold"
                            >
                                +
                            </button>
                        </div>

                        {/* Complete Item Removal Action Trigger */}
                        <div>
                            <button 
                                onClick={() => removeFromCart(item.id)} 
                                className="text-sm font-medium text-red-600 hover:text-red-800 transition"
                            >
                                Remove
                            </button>
                        </div>
                    </div>
                ))}
            </div>

            {/* Total Order Cost Summary Footer */}
            <div className="mt-8 pt-6 border-t border-gray-200 flex flex-col items-end">
                <div className="text-right">
                    <h3 className="text-xl font-medium text-gray-700">
                        Total Balance: <span className="text-2xl font-bold text-green-600 ml-2">${total}</span>
                    </h3>
                </div>
                <button 
                    className="mt-4 px-6 py-3 bg-blue-600 text-white font-semibold rounded-lg shadow-md hover:bg-blue-700 hover:shadow-lg transition focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2 w-full sm:w-auto"
                >
                    Proceed to Checkout
                </button>
            </div>
        </div>
    );
};

export default CartPage;