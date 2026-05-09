import { Lightbulb, Star } from 'lucide-react';
import './RecommendationCard.css';

export default function RecommendationCard({ item, index }) {
  const { product, score, explanation, method } = item;

  // Determine method color
  const methodColors = {
    'Rule-Based': 'var(--accent-cyan)',
    'Constraint-Based': 'var(--accent-purple)',
    'Utility-Based': 'var(--accent-orange)',
    'Collaborative Filtering': 'var(--accent-pink)',
    'CF: User-Based Cosine': 'var(--accent-pink)',
    'CF: User-Based Pearson k-NN': '#ff6b9d',
    'CF: Item-Based Cosine': '#f59e0b',
    'CF: Item-Based Jaccard': '#a78bfa',
    'Content-Based': 'var(--accent-green)',
    'Content-Based (TFIDF)': 'var(--accent-green)',
    'Content-Based (LSA)': '#34d399',
    'Content-Based (WORD2VEC)': '#6ee7b7',
    'Content-Based (FEATURE)': '#10b981',
  };
  const color = methodColors[method] || 'var(--accent-blue)';

  return (
    <div
      className="rec-card glass"
      style={{ animationDelay: `${index * 0.1}s`, '--method-color': color }}
    >
      <div className="rec-card-header">
        <div className="rec-rank">#{index + 1}</div>
        <div className="rec-score-badge">
          <span className="rec-score-value">{score.toFixed(1)}</span>
          <span className="rec-score-label">score</span>
        </div>
      </div>

      <div className="rec-card-body">
        <img
          src={product.image}
          alt={product.name}
          className="rec-image"
          loading="lazy"
          onError={(e) => {
            e.target.src = `https://placehold.co/120x120/1a1a2e/00f2fe?text=${encodeURIComponent(product.name.split(' ')[0])}`;
          }}
        />
        <div className="rec-details">
          <p className="rec-brand">{product.brand}</p>
          <h4 className="rec-name">{product.name}</h4>
          <div className="rec-meta">
            <span className="rec-price">${product.price.toFixed(2)}</span>
            <span className="rec-rating"><Star size={12} fill="currentColor" style={{color: 'var(--accent-orange)'}}/> {product.rating}</span>
          </div>
        </div>
      </div>

      <div className="rec-method-tag" style={{ borderColor: color, color }}>
        {method}
      </div>

      <div className="rec-explanation">
        <span className="rec-explanation-icon"><Lightbulb size={16} /></span>
        <p>{explanation}</p>
      </div>
    </div>
  );
}
