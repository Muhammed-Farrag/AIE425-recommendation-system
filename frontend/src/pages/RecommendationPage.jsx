import { useState } from 'react';
import RecommendationCard from '../components/RecommendationCard';
import { getRecommendations } from '../services/api';
import { Users, FileText, BrainCircuit, Rocket } from 'lucide-react';
import './RecommendationPage.css';

const USER_ID = 'user_demo_1';

const METHODS = [
  { key: 'collaborative', label: 'Collaborative Filtering', icon: <Users size={20} />, color: 'var(--accent-pink)' },
  { key: 'content-based', label: 'Content-Based', icon: <FileText size={20} />, color: 'var(--accent-green)' },
  { key: 'knowledge-based', label: 'Knowledge-Based', icon: <BrainCircuit size={20} />, color: 'var(--accent-cyan)' },
];

export default function RecommendationPage() {
  const [activeMethod, setActiveMethod] = useState('collaborative');
  const [results, setResults] = useState(null);
  const [loading, setLoading] = useState(false);
  const [category, setCategory] = useState('');

  const fetchRecommendations = async (method) => {
    setActiveMethod(method);
    setLoading(true);
    setResults(null);
    try {
      const data = await getRecommendations(method, {
        user_id: USER_ID,
        category: category || null,
      });
      setResults(data);
    } catch (err) {
      console.error(err);
    }
    setLoading(false);
  };

  return (
    <div className="rec-page">
      <div className="rec-page-header animate-in">
        <h1 className="rec-page-title">
          <span className="gradient-text">AI Recommendations</span>
        </h1>
        <p className="rec-page-subtitle">
          Choose a recommendation strategy and discover products curated for you.
        </p>
      </div>

      {/* Method Selector Tabs */}
      <div className="method-tabs">
        {METHODS.map(m => (
          <button
            key={m.key}
            className={`method-tab ${activeMethod === m.key ? 'active' : ''}`}
            style={{ '--tab-color': m.color }}
            onClick={() => fetchRecommendations(m.key)}
          >
            <span className="method-tab-icon">{m.icon}</span>
            <span className="method-tab-label">{m.label}</span>
          </button>
        ))}
      </div>

      {/* Optional Category Filter */}
      <div className="rec-filter-row">
        <input
          type="text"
          placeholder="Filter by category (optional)"
          value={category}
          onChange={(e) => setCategory(e.target.value)}
          className="rec-filter-input glass"
        />
      </div>

      {/* Results */}
      <div className="rec-results">
        {loading && (
          <div className="rec-loading">
            <div className="spinner" />
            <p>Generating recommendations...</p>
          </div>
        )}

        {results && !loading && (
          <>
            <div className="rec-results-header">
              <h2>{results.method}</h2>
              <span className="rec-results-count">{results.total_results} results</span>
            </div>
            <div className="rec-results-list">
              {results.recommendations.map((item, i) => (
                <RecommendationCard key={i} item={item} index={i} />
              ))}
            </div>
          </>
        )}

        {!results && !loading && (
          <div className="rec-empty-state">
            <span className="rec-empty-icon"><Rocket size={48} /></span>
            <h3>Select a method to begin</h3>
            <p>Click one of the recommendation strategies above</p>
          </div>
        )}
      </div>
    </div>
  );
}
