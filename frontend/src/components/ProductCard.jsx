import { Star } from 'lucide-react';
import './ProductCard.css';

export default function ProductCard({ product, onClick }) {
  return (
    <div className="product-card glass" onClick={() => onClick?.(product)}>
      <div className="product-image-wrapper">
        <img
          src={product.image}
          alt={product.name}
          className="product-image"
          loading="lazy"
          onError={(e) => {
            e.target.src = `https://placehold.co/400x300/1a1a2e/00f2fe?text=${encodeURIComponent(product.name.split(' ')[0])}`;
          }}
        />
        <div className="product-badge">{product.category}</div>
      </div>
      <div className="product-info">
        <p className="product-brand">{product.brand}</p>
        <h3 className="product-name">{product.name}</h3>
        <div className="product-meta">
          <span className="product-price">${product.price.toFixed(2)}</span>
          <span className="product-rating">
            <span className="star"><Star size={14} fill="currentColor" /></span> {product.rating}
          </span>
        </div>
      </div>
    </div>
  );
}
