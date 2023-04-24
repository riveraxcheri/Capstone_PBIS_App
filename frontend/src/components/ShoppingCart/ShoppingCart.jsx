import React from "react";
import { useEffect, useState } from "react";
import useAuth from "../../hooks/useAuth";
import axios from "axios";

const ShoppingCart = () => {
    const [user, token] = useAuth();
    const [items, setItems] = useState([]);
  useEffect(() => {
    const fetchCart = async () => {
      try {
        let response = await axios.get("http://127.0.0.1:8000/api/cart/", {
          headers: {
            Authorization: "Bearer " + token,
          },
        });
        setItems(response.data);
      } catch (error) {
        console.log(error.response.data);
      }
    };
    fetchCart();
  }, [token]);
    return ( 
    <div>
        <h1>{user.username}'s Shopping Cart:</h1>
    </div> );
}
 
export default ShoppingCart;