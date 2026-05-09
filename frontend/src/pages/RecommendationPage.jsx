import { useState } from 'react';
import RecommendationCard from '../components/RecommendationCard';
import { getRecommendations, getCollaborativeRecommendations, compareCollaborative } from '../services/api';
import { Users, FileText, BrainCircuit, Rocket, ChevronDown, GitCompare } from 'lucide-react';
import './RecommendationPage.css';

const USERS = [
  { id: 'U001', label: 'U001 — Marcus (Audiophile)' },
  { id: 'U006', label: 'U006 — Aaliyah (Mobile Power User)' },
  { id: 'U011', label: 'U011 — Cormac (Photographer)' },
  { id: 'U016', label: 'U016 — Tyler (Home Gamer)' },
  { id: 'U021', label: 'U021 — Claire (Smart Home)' },
  { id: 'U026', label: 'U026 — Sandra (Budget Shopper)' },
  { id: 'U031', label: 'U031 — Yusuf (Tech Professional)' },
  { id: 'U036', label: 'U036 — Brooke (Casual Consumer)' },
];

const METHODS = [
  { key: 'collaborative', label: 'Collaborative Filtering', icon: <Users size={20} />, color: 'var(--accent-pink)' },
  { key: 'content-based', label: 'Content-Based', icon: <FileText size={20} />, color: 'var(--accent-green)' },
  { key: 'knowledge-based', label: 'Knowledge-Based', icon: <BrainCircuit size={20} />, color: 'var(--accent-cyan)' },
];

const CF_METHODS = [
  { key: 'user_cosine', label: 'User-Based Cosine' },
  { key: 'user_pearson', label: 'User-Based Pearson k-NN' },
  { key: 'item_cosine', label: 'Item-Based Cosine' },
  { key: 'item_jaccard', label: 'Item-Based Jaccard' },
];

export default function RecommendationPage() {
  const [activeMethod, setActiveMethod] = useState('collaborative');
  const [activeCfMethod, setActiveCfMethod] = useState('user_cosine');
  const [userId, setUserId] = useState('U001');
  const [results, setResults] = useState(null);
  const [compareResults, setCompareResults] = useState(null);
  const [loading, setLoading] = useState(false);
  const [category, setCategory] = useState('');

  const fetchRecommendations = async (method, cfMethod) => {
    setActiveMethod(method);
    setLoading(true);
    setResults(null);
    setCompareResults(null);
    try {
      if (method === 'collaborative') {
        const cf = cfMethod || activeCfMethod;
        setActiveCfMethod(cf);
        const data = await getCollaborativeRecommendations(cf, {
          user_id: userId,
          category: category || null,
        });
        setResults(data);
      } else {
        const data = await getRecommendations(method, {
          user_id: userId,
          category: category || null,
        });
        setResults(data);
      }
    } catch (err) {
      console.error(err);
    }
    setLoading(false);
  };

  const handleCompareAll = async () => {
    setLoading(true);
    setResults(null);
    setCompareResults(null);
    try {
      const data = await compareCollaborative({ user_id: userId });
      setCompareResults(data);
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

      {/* User Selector */}
      <div className="rec-user-selector">
        <label className="rec-user-label">
          <Users size={16} /> Active User
        </label>
        <div className="rec-select-wrapper">
          <select
            value={userId}
            onChange={(e) => setUserId(e.target.value)}
            className="rec-select glass"
            id="user-selector"
          >
            {USERS.map(u => (
              <option key={u.id} value={u.id}>{u.label}</option>
            ))}
          </select>
          <ChevronDown size={16} className="rec-select-icon" />
        </div>
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

      {/* CF Sub-Method Selector — visible only when CF is active */}
      {activeMethod === 'collaborative' && (
        <div className="cf-method-selector animate-in">
          <div className="cf-method-buttons">
            {CF_METHODS.map(cf => (
              <button
                key={cf.key}
                className={`cf-method-btn ${activeCfMethod === cf.key ? 'active' : ''}`}
                onClick={() => fetchRecommendations('collaborative', cf.key)}
              >
                {cf.label}
              </button>
            ))}
          </div>
          <button className="cf-compare-btn glass" onClick={handleCompareAll}>
            <GitCompare size={16} />
            Compare All CF Methods
          </button>
        </div>
      )}

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

        {/* Single method results */}
        {results && !loading && !compareResults && (
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

        {/* CF Comparison results */}
        {compareResults && !loading && (
          <div className="cf-compare-grid">
            {Object.entries(compareResults)
              .filter(([key]) => key !== 'user_id')
              .map(([methodKey, methodResults]) => (
                <div key={methodKey} className="cf-compare-column glass">
                  <h3 className="cf-compare-title">{methodResults.method}</h3>
                  <span className="cf-compare-count">{methodResults.total_results} results</span>
                  <div className="cf-compare-items">
                    {methodResults.recommendations.map((item, i) => (
                      <RecommendationCard key={i} item={item} index={i} />
                    ))}
                  </div>
                </div>
              ))}
          </div>
        )}

        {!results && !loading && !compareResults && (
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
