import Products from "../Products/Products";
const Store = ({products}) => {
    return ( 
    <div>
        <h3>Store Page</h3>
        <button>Get Products</button>
    </div>
    
 );
}
{/* <p>{products.map((product) => (<Products product={product} key={product.id}/>))}</p> */}
export default Store;