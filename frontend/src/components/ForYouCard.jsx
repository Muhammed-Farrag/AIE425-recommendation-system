import { Star, Lightbulb } from 'lucide-react';
import { useState } from 'react';
import './ForYouCard.css';

const METHOD_COLORS = {
  'CF: User-Based Cosine': '#f472b6',
  'CF: User-Based Pearson k-NN': '#ff6b9d',
  'CF: Item-Based Cosine': '#f59e0b',
  'CF: Item-Based Jaccard': '#a78bfa',
  'Content-Based': '#34d399',
  'Content-Based (TFIDF)': '#34d399',
  'Content-Based (LSA)': '#6ee7b7',
  'Content-Based (WORD2VEC)': '#10b981',
  'Content-Based (FEATURE)': '#2dd4bf',
};

export default function ForYouCard({ item, index }) {
  const [showExplanation, setShowExplanation] = useState(false);
  const { product, score, explanation, method } = item;
  const color = METHOD_COLORS[method] || 'var(--accent-cyan)';

  return (
    <div
      className="fyu-card glass"
      style={{ animationDelay: `${index * 0.07}s` }}
      onMouseEnter={() => setShowExplanation(true)}
      onMouseLeave={() => setShowExplanation(false)}
    >
      {/* Image */}
      <div className="fyu-image-wrapper">
        <img
          src={product.image}
          alt={product.name}
          className="fyu-image"
          loading="lazy"
          onError={(e) => {
            e.target.src = `https://placehold.co/400x300/1a1a2e/00f2fe?text=${encodeURIComponent(product.name.split(' ')[0])}`;
          }}
        />
        {/* Score overlay */}
        <div className="fyu-score-badge">
          <span className="fyu-score-value">{score.toFixed(1)}</span>
          <span className="fyu-score-label">score</span>
        </div>
        {/* Rank */}
        <div className="fyu-rank">#{index + 1}</div>
        {/* Method tag */}
        <div className="fyu-method-pill" style={{ borderColor: color, color }}>
          {method}
        </div>
      </div>

      {/* Info */}
      <div className="fyu-info">
        <p className="fyu-brand">{product.brand}</p>
        <h3 className="fyu-name">{product.name}</h3>
        <div className="fyu-meta">
          <span className="fyu-price">${product.price.toFixed(2)}</span>
          <span className="fyu-rating">
            <Star size={13} fill="currentColor" style={{ color: 'var(--accent-orange)' }} />
            {product.rating}
          </span>
        </div>
      </div>

      {/* Explanation overlay on hover */}
      <div className={`fyu-explanation-overlay ${showExplanation ? 'visible' : ''}`}>
        <div className="fyu-explanation-content">
          <Lightbulb size={16} className="fyu-explanation-icon" />
          <p>{explanation}</p>
        </div>
      </div>
    </div>
  );
}
