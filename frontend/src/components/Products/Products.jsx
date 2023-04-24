const Products = ({product}) => {
    return ( 
        <ul>
            <li className="product_info">
                <h3>{product.name}</h3>
                <p>{product.cost}</p>
                <p>{product.category}</p>
                <p>{product.is_available}</p>
            </li>
        </ul>
     );
}
 
export default Products;