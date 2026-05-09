import { useState, useEffect } from 'react';
import RecommendationCard from '../components/RecommendationCard';
import { getKnowledgeBasedRecommendations, compareKnowledgeBased, getCategories, getBrands } from '../services/api';
import { Ruler, Scale, BarChart2, BrainCircuit, Frown, DollarSign, Folder, Tag, Star, Search, Zap } from 'lucide-react';
import { BarChart, Bar, XAxis, YAxis, Tooltip, Legend, ResponsiveContainer, CartesianGrid } from 'recharts';
import './KnowledgeBasedPage.css';

const USER_ID = 'user_demo_1';

const KB_METHODS = [
  {
    key: 'rule',
    label: 'Rule-Based',
    icon: <Ruler size={24} />,
    color: 'var(--accent-cyan)',
    description: 'Strict filtering: products must match ALL your constraints.',
  },
  {
    key: 'constraint',
    label: 'Constraint-Based',
    icon: <Scale size={24} />,
    color: 'var(--accent-purple)',
    description: 'Hard + soft constraints: required filters with preference based ranking.',
  },
  {
    key: 'utility',
    label: 'Utility-Based',
    icon: <BarChart2 size={24} />,
    color: 'var(--accent-orange)',
    description: 'Weighted scoring: assigns importance to price, rating, brand, and features.',
  },
];

export default function KnowledgeBasedPage() {
  const [selectedMethod, setSelectedMethod] = useState('rule');
  const [categories, setCategories] = useState([]);
  const [brands, setBrands] = useState([]);
  const [form, setForm] = useState({
    budget: '',
    category: '',
    brand: '',
    min_rating: '',
  });
  const [results, setResults] = useState(null);
  const [compareResults, setCompareResults] = useState(null);
  const [loading, setLoading] = useState(false);
  const [showCompare, setShowCompare] = useState(false);

  useEffect(() => {
    Promise.all([getCategories(), getBrands()]).then(([cats, brds]) => {
      setCategories(cats);
      setBrands(brds);
    });
  }, []);

  const buildInput = () => ({
    user_id: USER_ID,
    budget: form.budget ? parseFloat(form.budget) : null,
    category: form.category || null,
    brand: form.brand || null,
    min_rating: form.min_rating ? parseFloat(form.min_rating) : null,
    preferences: {},
  });

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setResults(null);
    setCompareResults(null);
    setShowCompare(false);

    try {
      const data = await getKnowledgeBasedRecommendations(selectedMethod, buildInput());
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
      const data = await compareKnowledgeBased(buildInput());
      setCompareResults(data);
      setShowCompare(true);
    } catch (error) {
      console.error('Failed to compare:', error);
    } finally {
      setLoading(false);
    }
  };

  const getChartData = () => {
    if (!compareResults) return [];
    const maxItems = 5;
    const data = [];
    
    for (let i = 0; i < maxItems; i++) {
      const ruleItem = compareResults.rule_based.recommendations[i];
      const constraintItem = compareResults.constraint_based.recommendations[i];
      const utilityItem = compareResults.utility_based.recommendations[i];
      
      if (!ruleItem && !constraintItem && !utilityItem) break;
      
      // Normalize rule-based (0-5) to 0-100 scale for visual comparison alongside the others
      data.push({
        name: `Rank #${i + 1}`,
        'Rule-Based': ruleItem ? parseFloat((ruleItem.score * 20).toFixed(1)) : 0,
        'Constraint-Based': constraintItem ? parseFloat(constraintItem.score.toFixed(1)) : 0,
        'Utility-Based': utilityItem ? parseFloat(utilityItem.score.toFixed(1)) : 0,
      });
    }
    return data;
  };

  const updateForm = (key, value) => setForm(prev => ({ ...prev, [key]: value }));

  return (
    <div className="kb-page">
      {/* Header */}
      <div className="kb-header animate-in">
        <h1 className="kb-title">
          <BrainCircuit className="inline-icon" size={32} /> <span className="gradient-text">Knowledge-Based AI</span>
        </h1>
        <p className="kb-subtitle">
          Define your constraints and preferences and our AI agents will find the perfect products for you.
        </p>
      </div>

      <div className="kb-layout">
        {/* Left Panel — Controls */}
        <aside className="kb-sidebar">
          {/* Method Selector */}
          <div className="kb-section glass">
            <h2 className="kb-section-title">Method</h2>
            <div className="kb-method-list">
              {KB_METHODS.map(m => (
                <button
                  key={m.key}
                  className={`kb-method-btn ${selectedMethod === m.key ? 'active' : ''}`}
                  style={{ '--m-color': m.color }}
                  onClick={() => setSelectedMethod(m.key)}
                >
                  <span className="kb-method-icon">{m.icon}</span>
                  <div className="kb-method-info">
                    <span className="kb-method-label">{m.label}</span>
                    <span className="kb-method-desc">{m.description}</span>
                  </div>
                </button>
              ))}
            </div>
          </div>

          {/* Input Form */}
          <form className="kb-form glass" onSubmit={handleSubmit}>
            <h2 className="kb-section-title">Your Preferences</h2>

            <div className="form-field">
              <label htmlFor="kb-budget"><DollarSign size={14} className="inline-icon" /> Budget (max price)</label>
              <input
                id="kb-budget"
                type="number"
                placeholder="e.g. 500"
                value={form.budget}
                onChange={(e) => updateForm('budget', e.target.value)}
                min="0"
              />
            </div>

            <div className="form-field">
              <label htmlFor="kb-category"><Folder size={14} className="inline-icon" /> Category</label>
              <select
                id="kb-category"
                value={form.category}
                onChange={(e) => updateForm('category', e.target.value)}
              >
                <option value="">Any Category</option>
                {categories.map(c => <option key={c} value={c}>{c}</option>)}
              </select>
            </div>

            <div className="form-field">
              <label htmlFor="kb-brand"><Tag size={14} className="inline-icon" /> Brand</label>
              <select
                id="kb-brand"
                value={form.brand}
                onChange={(e) => updateForm('brand', e.target.value)}
              >
                <option value="">Any Brand</option>
                {brands.map(b => <option key={b} value={b}>{b}</option>)}
              </select>
            </div>

            <div className="form-field">
              <label htmlFor="kb-rating"><Star size={14} className="inline-icon" /> Minimum Rating</label>
              <input
                id="kb-rating"
                type="number"
                placeholder="e.g. 4.0"
                value={form.min_rating}
                onChange={(e) => updateForm('min_rating', e.target.value)}
                min="1"
                max="5"
                step="0.1"
              />
            </div>

            <button type="submit" className="kb-submit-btn flex-center" disabled={loading}>
              {loading ? 'Analyzing...' : <><Search size={18} className="mr-2" /> Get Recommendations</>}
            </button>

            <button
              type="button"
              className="kb-compare-btn flex-center"
              onClick={handleCompare}
              disabled={loading}
            >
              <Zap size={18} className="mr-2" /> Compare All 3 Methods
            </button>
          </form>
        </aside>

        {/* Right Panel — Results */}
        <main className="kb-results-panel">
          {loading && (
            <div className="kb-loading">
              <div className="spinner" />
              <p>Running {showCompare ? 'comparison' : selectedMethod} analysis...</p>
            </div>
          )}

          {/* Single Method Results */}
          {results && !showCompare && !loading && (
            <div className="kb-results-section animate-in">
              <div className="kb-results-header">
                <h2>{results.method}</h2>
                <span className="kb-results-count">{results.total_results} products found</span>
              </div>
              {results.recommendations.length === 0 ? (
                <div className="kb-no-results">
                  <span><Frown size={48} className="mx-auto text-muted" /></span>
                  <p>No products match your constraints. Try relaxing your filters.</p>
                </div>
              ) : (
                <div className="kb-results-list">
                  {results.recommendations.map((item, i) => (
                    <RecommendationCard key={i} item={item} index={i} />
                  ))}
                </div>
              )}
            </div>
          )}

          {/* Comparison View */}
          {compareResults && showCompare && !loading && (
            <div className="kb-compare-grid animate-in">
              {['rule_based', 'constraint_based', 'utility_based'].map((key) => {
                const data = compareResults[key];
                const matchMap = { rule_based: 0, constraint_based: 1, utility_based: 2 };
                const info = KB_METHODS[matchMap[key]];
                
                return (
                  <div key={key} className="kb-compare-column glass">
                    <div className="kb-compare-header" style={{ borderColor: info.color }}>
                      <span className="kb-compare-icon">{info.icon}</span>
                      <h3>{info.label}</h3>
                      <span className="kb-compare-count">{data.total_results} results</span>
                    </div>
                    <div className="kb-compare-list">
                      {data.recommendations.slice(0, 5).map((item, i) => {
                        return (
                          <div key={i} className="kb-compare-item">
                            <div className="kb-compare-rank">#{i + 1}</div>
                            <div className="kb-compare-info">
                              <p className="kb-compare-name">{item.product.name}</p>
                              <div className="kb-compare-meta">
                                <span>${item.product.price.toFixed(0)}</span>
                                <span>★ {item.product.rating}</span>
                                <span className="kb-compare-score">Score: {item.score.toFixed(1)}</span>
                              </div>
                            </div>
                          </div>
                        );
                      })}
                      {data.recommendations.length === 0 && (
                        <p className="kb-compare-empty">No matches</p>
                      )}
                    </div>
                  </div>
                );
              })}

            <div className="kb-compare-chart glass">
              <h3 className="kb-chart-title"><BarChart2 className="inline-icon" size={20} /> Method Score Comparison</h3>
              <p className="kb-chart-subtitle">Normalized scores (0-100) across all methods for the top 5 products.</p>
              <div style={{ width: '100%', height: 350, marginTop: '20px' }}>
                <ResponsiveContainer>
                  <BarChart data={getChartData()} margin={{ top: 20, right: 30, left: 0, bottom: 5 }}>
                    <CartesianGrid strokeDasharray="3 3" stroke="rgba(255,255,255,0.05)" vertical={false} />
                    <XAxis dataKey="name" stroke="rgba(255,255,255,0.5)" tick={{fill: 'rgba(255,255,255,0.5)'}} />
                    <YAxis stroke="rgba(255,255,255,0.5)" tick={{fill: 'rgba(255,255,255,0.5)'}} />
                    <Tooltip 
                      contentStyle={{ backgroundColor: 'rgba(10, 10, 15, 0.95)', border: '1px solid rgba(255,255,255,0.1)', borderRadius: '8px', boxShadow: '0 10px 30px rgba(0,0,0,0.5)' }}
                      itemStyle={{ color: '#fff', fontWeight: 600 }}
                      cursor={{ fill: 'rgba(255,255,255,0.05)' }}
                    />
                    <Legend wrapperStyle={{ paddingTop: '20px' }} />
                    <Bar dataKey="Rule-Based" fill="var(--accent-cyan)" radius={[4, 4, 0, 0]} />
                    <Bar dataKey="Constraint-Based" fill="var(--accent-purple)" radius={[4, 4, 0, 0]} />
                    <Bar dataKey="Utility-Based" fill="var(--accent-orange)" radius={[4, 4, 0, 0]} />
                  </BarChart>
                </ResponsiveContainer>
              </div>
            </div>
            </div>
          )}

          {/* Initial Empty State */}
          {!results && !compareResults && !loading && (
            <div className="kb-empty-state">
              <div className="kb-empty-visual">
                <span className="kb-empty-icon"><BrainCircuit size={48} /></span>
                <div className="kb-empty-orbits">
                  <div className="orbit orbit-1" />
                  <div className="orbit orbit-2" />
                  <div className="orbit orbit-3" />
                </div>
              </div>
              <h3>Configure & Discover</h3>
              <p>Set your preferences on the left and let our AI find the best products for you.</p>
            </div>
          )}
        </main>
      </div>
    </div>
  );
}
