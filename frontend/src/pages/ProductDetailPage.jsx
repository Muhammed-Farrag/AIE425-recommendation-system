import { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { Star, ArrowLeft, BrainCircuit, Sparkles } from 'lucide-react';
import { getProductById, rateProduct } from '../services/api';
import './ProductDetailPage.css';

const USER_ID = 'user_demo_1'; // Simulated user

export default function ProductDetailPage() {
  const { id } = useParams();
  const navigate = useNavigate();
  const [product, setProduct] = useState(null);
  const [loading, setLoading] = useState(true);
  const [userRating, setUserRating] = useState(0);
  const [hoverRating, setHoverRating] = useState(0);
  const [ratingMessage, setRatingMessage] = useState('');

  useEffect(() => {
    setLoading(true);
    getProductById(parseInt(id))
      .then(setProduct)
      .catch(() => navigate('/'))
      .finally(() => setLoading(false));
  }, [id, navigate]);

  const handleRate = async (rating) => {
    setUserRating(rating);
    try {
      const res = await rateProduct(USER_ID, product.id, rating);
      setRatingMessage(res.message);
      setTimeout(() => setRatingMessage(''), 3000);
    } catch {
      setRatingMessage('Failed to submit rating');
    }
  };

  if (loading) {
    return (
      <div className="detail-page">
        <div className="detail-skeleton glass" />
      </div>
    );
  }

  if (!product) return null;

  return (
    <div className="detail-page">
      <button className="back-btn" onClick={() => navigate(-1)}>
        <ArrowLeft size={16} /> Back
      </button>

      <div className="detail-container animate-in">
        <div className="detail-image-section">
          <div className="detail-image-wrapper glass">
            <img
              src={product.image}
              alt={product.name}
              className="detail-image"
              onError={(e) => {
                e.target.src = `https://placehold.co/600x400/1a1a2e/00f2fe?text=${encodeURIComponent(product.name.split(' ')[0])}`;
              }}
            />
          </div>
        </div>

        <div className="detail-info-section">
          <div className="detail-badge">{product.category}</div>
          <p className="detail-brand">{product.brand}</p>
          <h1 className="detail-name">{product.name}</h1>

          <div className="detail-price-rating">
            <span className="detail-price gradient-text">${product.price.toFixed(2)}</span>
            <span className="detail-rating">
              <Star size={16} className="star-icon" fill="currentColor" /> {product.rating} / 5.0
            </span>
          </div>

          <p className="detail-description">{product.description}</p>

          {/* Features */}
          <div className="detail-features">
            <h3>Features</h3>
            <div className="features-grid">
              {product.features.map(f => (
                <span key={f} className="feature-tag">{f.replace(/_/g, ' ')}</span>
              ))}
            </div>
          </div>

          {/* Rating Section */}
          <div className="rating-section glass">
            <h3>Rate this Product</h3>
            <div className="star-rating">
              {[1, 2, 3, 4, 5].map(star => (
                <button
                  key={star}
                  className={`star-btn ${star <= (hoverRating || userRating) ? 'active' : ''}`}
                  onClick={() => handleRate(star)}
                  onMouseEnter={() => setHoverRating(star)}
                  onMouseLeave={() => setHoverRating(0)}
                >
                  <Star size={24} fill={star <= (hoverRating || userRating) ? "currentColor" : "none"} />
                </button>
              ))}
            </div>
            {ratingMessage && <p className="rating-msg">{ratingMessage}</p>}
          </div>

          {/* Quick Actions */}
          <div className="detail-actions">
            <button
              className="action-btn primary"
              onClick={() => navigate('/knowledge-based')}
            >
              <BrainCircuit size={18} /> Find Similar (Knowledge AI)
            </button>
            <button
              className="action-btn secondary"
              onClick={() => navigate('/recommendations')}
            >
              <Sparkles size={18} /> Get Recommendations
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}
