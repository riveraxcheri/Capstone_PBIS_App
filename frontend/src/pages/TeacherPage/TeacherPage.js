import React from "react";
import { useEffect, useState } from "react";
import useAuth from "../../hooks/useAuth";
import axios from "axios";
import Products from "../../components/Products/Products";

const TeacherPage = () => {
  const [user, token] = useAuth();
  const [products, setProducts] = useState([]);
  useEffect(() => {
    const fetchProducts = async () => {
      try {
        let response = await axios.get("http://127.0.0.1:8000/api/store/", {
          headers: {
            Authorization: "Bearer " + token,
          },
        });
        setProducts(response.data);
      } catch (error) {
        console.log(error.response.data);
      }
    };
    fetchProducts();
  }, [token]);
  return (
    <div className="container">
      <h1>Teacher Page for {user.username}!</h1>
      <p>{products.map((product) => (<Products product={product} key={product.id}/>))}</p>
    </div>
  );
};

export default TeacherPage;
