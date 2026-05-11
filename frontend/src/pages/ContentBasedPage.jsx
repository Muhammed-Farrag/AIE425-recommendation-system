import { useState } from 'react';
import ForYouCard from '../components/ForYouCard';
import {
  getContentBasedRecommendations,
  compareContentBased,
} from '../services/api';
import {
  FileText, GitCompare, Zap, ChevronDown, Layers, UserCheck,
} from 'lucide-react';
import { BarChart, Bar, XAxis, YAxis, Tooltip, Legend, ResponsiveContainer, CartesianGrid } from 'recharts';
import './RecommendPage.css';

const USERS = [
  { id: 'U001', label: 'Marcus — Audiophile' },
  { id: 'U006', label: 'Aaliyah — Mobile Power User' },
  { id: 'U011', label: 'Cormac — Photographer' },
  { id: 'U016', label: 'Tyler — Home Gamer' },
  { id: 'U021', label: 'Claire — Smart Home' },
  { id: 'U026', label: 'Sandra — Budget Shopper' },
  { id: 'U031', label: 'Yusuf — Tech Professional' },
  { id: 'U036', label: 'Brooke — Casual Consumer' },
];

const CB_METHODS = [
  { key: 'tfidf',   label: 'TF-IDF',        color: '#10b981', desc: 'Term frequency–inverse document frequency on product text.' },
  { key: 'lsa',     label: 'LSA',            color: '#34d399', desc: 'Latent Semantic Analysis for dimensionality-reduced topic similarity.' },
  { key: 'word2vec',label: 'Word2Vec',       color: '#6ee7b7', desc: 'Dense word embeddings capturing semantic meaning of product descriptions.' },
  { key: 'feature', label: 'Feature-Based',  color: '#a7f3d0', desc: 'Structured attribute matching (brand, category, specifications).' },
];

const CB_COMPARE_KEYS = {
  tfidf:    'TF-IDF',
  lsa:      'LSA',
  word2vec: 'Word2Vec',
  feature:  'Feature-Based',
};

export default function ContentBasedPage() {
  const [userId, setUserId] = useState('U001');
  const [method, setMethod] = useState('tfidf');
  const [results, setResults] = useState(null);
  const [compareResults, setCompareResults] = useState(null);
  const [loading, setLoading] = useState(false);
  const [showCompare, setShowCompare] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setResults(null);
    setCompareResults(null);
    setShowCompare(false);
    try {
      const data = await getContentBasedRecommendations(method, { user_id: userId });
      setResults(data);
    } catch (err) {
      console.error(err);
    }
    setLoading(false);
  };

  const handleCompare = async () => {
    setLoading(true);
    setResults(null);
    setCompareResults(null);
    try {
      const data = await compareContentBased({ user_id: userId });
      setCompareResults(data);
      setShowCompare(true);
    } catch (err) {
      console.error(err);
    }
    setLoading(false);
  };

  const getChartData = () => {
    if (!compareResults) return [];
    return Object.entries(CB_COMPARE_KEYS).map(([key, label]) => {
      const recs = compareResults[key]?.recommendations ?? [];
      const avgScore = recs.length
        ? +(recs.reduce((s, r) => s + r.score, 0) / recs.length * 100).toFixed(1)
        : 0;
      return { method: label, avgScore };
    });
  };

  const currentMethod = CB_METHODS.find((m) => m.key === method);

  return (
    <div className="rp-page">
      <div className="rp-header animate-in">
        <h1 className="rp-title">
          <FileText className="inline-icon" size={32} />
          <span className="gradient-text-green">Content-Based</span>
        </h1>
        <p className="rp-subtitle">
          Find products similar to what you've loved before. Powered by text similarity, semantic embeddings, and feature matching.
        </p>
      </div>

      <div className="rp-layout">
        {/* ── Sidebar ─────────────────────────────────── */}
        <aside className="rp-sidebar">
          {/* User selector */}
          <div className="rp-section glass">
            <h2 className="rp-section-title"><UserCheck size={14} className="inline-icon" /> User Persona</h2>
            <div className="rp-select-wrap">
              <select value={userId} onChange={(e) => setUserId(e.target.value)} className="rp-select">
                {USERS.map((u) => (
                  <option key={u.id} value={u.id}>{u.id} — {u.label.split('—')[1].trim()}</option>
                ))}
              </select>
              <ChevronDown size={14} className="rp-select-chevron" />
            </div>
          </div>

          {/* Method selector */}
          <div className="rp-section glass">
            <h2 className="rp-section-title"><Layers size={14} className="inline-icon" /> Algorithm</h2>
            <div className="rp-method-list">
              {CB_METHODS.map((m) => (
                <button
                  key={m.key}
                  className={`rp-method-btn ${method === m.key ? 'active' : ''}`}
                  style={{ '--m-color': m.color }}
                  onClick={() => setMethod(m.key)}
                >
                  <span className="rp-method-dot" style={{ background: m.color }} />
                  <div className="rp-method-info">
                    <span className="rp-method-label">{m.label}</span>
                    <span className="rp-method-desc">{m.desc}</span>
                  </div>
                </button>
              ))}
            </div>
          </div>

          {/* Actions */}
          <form onSubmit={handleSubmit} className="rp-actions">
            <button type="submit" className="rp-submit-btn rp-submit-green" disabled={loading}>
              <Zap size={16} />
              {loading && !showCompare ? 'Loading...' : 'Get Recommendations'}
            </button>
            <button type="button" className="rp-compare-btn" onClick={handleCompare} disabled={loading}>
              <GitCompare size={16} />
              Compare All 4 Methods
            </button>
          </form>
        </aside>

        {/* ── Results ─────────────────────────────────── */}
        <main className="rp-results">
          {loading && (
            <div className="rp-loading">
              <div className="rp-spinner rp-spinner-green" />
              <p>{showCompare ? 'Running all 4 CB methods...' : `Running ${currentMethod?.label}...`}</p>
            </div>
          )}

          {/* Single method */}
          {results && !showCompare && !loading && (
            <div className="animate-in">
              <div className="rp-results-header">
                <h2>{results.method}</h2>
                <span className="rp-count-pill">{results.total_results} results</span>
              </div>
              <div className="rp-card-grid">
                {results.recommendations.map((item, i) => (
                  <ForYouCard key={i} item={item} index={i} />
                ))}
              </div>
            </div>
          )}

          {/* Compare mode */}
          {compareResults && showCompare && !loading && (
            <div className="animate-in">
              <h2 className="rp-compare-title"><GitCompare size={20} /> Comparing All 4 CB Methods</h2>
              <div className="rp-compare-scroll">
              <div className="rp-compare-grid" style={{ gridTemplateColumns: 'repeat(4, 220px)' }}>
                {Object.entries(CB_COMPARE_KEYS).map(([key, label], ci) => {
                  const data = compareResults[key];
                  if (!data) return null;
                  return (
                    <div key={key} className="rp-compare-col glass">
                      <div className="rp-compare-col-header" style={{ borderColor: CB_METHODS[ci]?.color }}>
                        <span className="rp-col-dot" style={{ background: CB_METHODS[ci]?.color }} />
                        <span className="rp-col-label">{label}</span>
                        <span className="rp-col-count">{data.total_results} results</span>
                      </div>
                      {data.recommendations.slice(0, 5).map((item, i) => (
                        <div key={i} className="rp-compare-item">
                          <span className="rp-compare-rank">#{i + 1}</span>
                          <div className="rp-compare-info">
                            <p className="rp-compare-name">{item.product.name}</p>
                            <div className="rp-compare-meta">
                              <span>${item.product.price?.toFixed(0)}</span>
                              <span>★ {item.product.rating}</span>
                              <span style={{ color: CB_METHODS[ci]?.color }}>
                                {(item.score * 100).toFixed(0)}%
                              </span>
                            </div>
                          </div>
                        </div>
                      ))}
                    </div>
                  );
                })}
              </div>
              </div>

              {/* Chart */}
              <div className="rp-chart glass">
                <h3 className="rp-chart-title"><GitCompare size={18} /> Average Similarity Score per Method</h3>
                <ResponsiveContainer width="100%" height={240}>
                  <BarChart data={getChartData()} margin={{ top: 10, right: 20, left: 0, bottom: 5 }}>
                    <CartesianGrid strokeDasharray="3 3" stroke="rgba(255,255,255,0.06)" />
                    <XAxis dataKey="method" tick={{ fill: 'rgba(255,255,255,0.5)', fontSize: 11 }} />
                    <YAxis tick={{ fill: 'rgba(255,255,255,0.5)', fontSize: 11 }} />
                    <Tooltip contentStyle={{ background: 'rgba(10,10,15,0.95)', border: '1px solid rgba(255,255,255,0.1)', borderRadius: 8 }} />
                    <Legend />
                    <Bar dataKey="avgScore" name="Avg Score (0-100)" fill="#10b981" radius={[4, 4, 0, 0]} />
                  </BarChart>
                </ResponsiveContainer>
              </div>
            </div>
          )}

          {/* Empty state */}
          {!results && !compareResults && !loading && (
            <div className="rp-empty">
              <FileText size={52} className="rp-empty-icon" />
              <h3>Select a method and load your feed</h3>
              <p>Pick a user persona and algorithm on the left, then click "Get Recommendations".</p>
            </div>
          )}
        </main>
      </div>
    </div>
  );
}
