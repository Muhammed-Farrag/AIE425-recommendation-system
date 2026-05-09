import { useState, useEffect, useCallback } from 'react';
import ForYouCard from '../components/ForYouCard';
import {
  getCollaborativeRecommendations,
  getRecommendations,
  compareCollaborative,
} from '../services/api';
import {
  SlidersHorizontal,
  X,
  Users,
  BrainCircuit,
  Sparkles,
  ChevronDown,
  GitCompare,
  Zap,
  FileText,
} from 'lucide-react';
import './ForYouPage.css';

const USERS = [
  { id: 'U001', label: 'Marcus (Audiophile)' },
  { id: 'U006', label: 'Aaliyah (Mobile Power User)' },
  { id: 'U011', label: 'Cormac (Photographer)' },
  { id: 'U016', label: 'Tyler (Home Gamer)' },
  { id: 'U021', label: 'Claire (Smart Home)' },
  { id: 'U026', label: 'Sandra (Budget Shopper)' },
  { id: 'U031', label: 'Yusuf (Tech Professional)' },
  { id: 'U036', label: 'Brooke (Casual Consumer)' },
];

const ENGINES = [
  { key: 'collaborative', label: 'Collaborative Filtering', icon: <Users size={18} /> },
  { key: 'content-based', label: 'Content-Based', icon: <FileText size={18} /> },
];

const CF_METHODS = [
  { key: 'user_cosine', label: 'User-Based Cosine', desc: 'Rates based on similar users\' preferences' },
  { key: 'user_pearson', label: 'User-Based Pearson k-NN', desc: 'Mean-centred correlation with nearest neighbours' },
  { key: 'item_cosine', label: 'Item-Based Cosine', desc: 'Finds items rated similarly by the same users' },
  { key: 'item_jaccard', label: 'Item-Based Jaccard', desc: 'Co-occurrence overlap on implicit feedback' },
];

const CF_METHOD_DISPLAY = {
  user_cosine: 'User-Based Cosine',
  user_pearson: 'User-Based Pearson k-NN',
  item_cosine: 'Item-Based Cosine',
  item_jaccard: 'Item-Based Jaccard',
};

export default function ForYouPage() {
  // State
  const [userId, setUserId] = useState('U001');
  const [engine, setEngine] = useState('collaborative');
  const [cfMethod, setCfMethod] = useState('user_cosine');
  const [drawerOpen, setDrawerOpen] = useState(false);
  const [results, setResults] = useState(null);
  const [compareResults, setCompareResults] = useState(null);
  const [loading, setLoading] = useState(false);
  const [compareMode, setCompareMode] = useState(false);

  // Fetch recommendations
  const fetchFeed = useCallback(async (uid, eng, cf) => {
    setLoading(true);
    setResults(null);
    setCompareResults(null);
    setCompareMode(false);
    try {
      if (eng === 'collaborative') {
        const data = await getCollaborativeRecommendations(cf, { user_id: uid });
        setResults(data);
      } else {
        const data = await getRecommendations(eng, { user_id: uid });
        setResults(data);
      }
    } catch (err) {
      console.error('Failed to fetch:', err);
    }
    setLoading(false);
  }, []);

  // Auto-fetch on mount
  useEffect(() => {
    fetchFeed(userId, engine, cfMethod);
  }, []); // eslint-disable-line react-hooks/exhaustive-deps

  // Drawer handlers
  const applyAndClose = () => {
    setDrawerOpen(false);
    fetchFeed(userId, engine, cfMethod);
  };

  const handleCompare = async () => {
    setDrawerOpen(false);
    setLoading(true);
    setResults(null);
    setCompareResults(null);
    try {
      const data = await compareCollaborative({ user_id: userId });
      setCompareResults(data);
      setCompareMode(true);
    } catch (err) {
      console.error(err);
    }
    setLoading(false);
  };

  // Current display label
  const currentLabel =
    engine === 'collaborative'
      ? CF_METHOD_DISPLAY[cfMethod] || cfMethod
      : 'Content-Based (TF-IDF)';

  const currentUser = USERS.find((u) => u.id === userId);

  return (
    <div className="fyu-page">
      {/* ── Header ────────────────────────────────────────────── */}
      <header className="fyu-header animate-in">
        <div className="fyu-header-left">
          <h1 className="fyu-title">
            <Sparkles size={28} className="fyu-title-icon" />
            <span className="gradient-text">For You</span>
          </h1>
          <div className="fyu-powered-row">
            <span className="fyu-powered-pill">
              <Zap size={12} />
              <span>{currentLabel}</span>
            </span>
            <span className="fyu-user-pill">
              <Users size={12} />
              <span>{currentUser?.label}</span>
            </span>
          </div>
        </div>

        <button
          className="fyu-settings-btn glass"
          onClick={() => setDrawerOpen(true)}
          aria-label="Open algorithm settings"
        >
          <SlidersHorizontal size={20} />
          <span className="fyu-settings-label">Algorithm</span>
        </button>
      </header>

      {/* ── Feed Grid ─────────────────────────────────────────── */}
      <main className="fyu-feed">
        {loading && (
          <div className="fyu-loading">
            <div className="fyu-loading-spinner" />
            <p>Curating your recommendations...</p>
          </div>
        )}

        {/* Normal feed */}
        {results && !loading && !compareMode && (
          <div className="fyu-grid" key={results.method + userId}>
            {results.recommendations.map((item, i) => (
              <ForYouCard key={`${item.product.name}-${i}`} item={item} index={i} />
            ))}
          </div>
        )}

        {/* Compare mode */}
        {compareResults && compareMode && !loading && (
          <div className="fyu-compare-container">
            <h2 className="fyu-compare-heading animate-in">
              <GitCompare size={22} />
              Comparing All 4 CF Methods
            </h2>
            <div className="fyu-compare-grid">
              {Object.entries(compareResults)
                .filter(([key]) => key !== 'user_id')
                .map(([methodKey, methodData]) => (
                  <div key={methodKey} className="fyu-compare-col glass animate-in">
                    <h3 className="fyu-compare-col-title">{methodData.method}</h3>
                    <span className="fyu-compare-col-count">
                      {methodData.total_results} results
                    </span>
                    <div className="fyu-compare-col-items">
                      {methodData.recommendations.map((item, i) => (
                        <ForYouCard key={i} item={item} index={i} />
                      ))}
                    </div>
                  </div>
                ))}
            </div>
          </div>
        )}

        {/* Empty state */}
        {!results && !compareResults && !loading && (
          <div className="fyu-empty">
            <Sparkles size={48} />
            <h3>No recommendations yet</h3>
            <p>Click the Algorithm button to configure and load your feed.</p>
          </div>
        )}
      </main>

      {/* ── Backdrop ──────────────────────────────────────────── */}
      <div
        className={`fyu-backdrop ${drawerOpen ? 'visible' : ''}`}
        onClick={() => setDrawerOpen(false)}
      />

      {/* ── Algorithm Drawer ──────────────────────────────────── */}
      <aside className={`fyu-drawer glass ${drawerOpen ? 'open' : ''}`}>
        <div className="fyu-drawer-header">
          <h2>
            <BrainCircuit size={20} className="inline-icon" /> Algorithm Settings
          </h2>
          <button className="fyu-drawer-close" onClick={() => setDrawerOpen(false)}>
            <X size={20} />
          </button>
        </div>

        <div className="fyu-drawer-body">
          {/* User Persona */}
          <div className="fyu-drawer-section">
            <label className="fyu-drawer-label">
              <Users size={14} /> User Persona
            </label>
            <div className="fyu-drawer-select-wrapper">
              <select
                value={userId}
                onChange={(e) => setUserId(e.target.value)}
                className="fyu-drawer-select"
              >
                {USERS.map((u) => (
                  <option key={u.id} value={u.id}>
                    {u.id} — {u.label}
                  </option>
                ))}
              </select>
              <ChevronDown size={14} className="fyu-drawer-select-chevron" />
            </div>
          </div>

          {/* Engine */}
          <div className="fyu-drawer-section">
            <label className="fyu-drawer-label">
              <BrainCircuit size={14} /> Recommendation Engine
            </label>
            <div className="fyu-drawer-engine-list">
              {ENGINES.map((e) => (
                <button
                  key={e.key}
                  className={`fyu-engine-btn ${engine === e.key ? 'active' : ''}`}
                  onClick={() => setEngine(e.key)}
                >
                  {e.icon}
                  <span>{e.label}</span>
                </button>
              ))}
            </div>
          </div>

          {/* CF Algorithm — only shown when engine = collaborative */}
          {engine === 'collaborative' && (
            <div className="fyu-drawer-section">
              <label className="fyu-drawer-label">
                <Sparkles size={14} /> Similarity Algorithm
              </label>
              <div className="fyu-drawer-cf-grid">
                {CF_METHODS.map((m) => (
                  <button
                    key={m.key}
                    className={`fyu-cf-btn ${cfMethod === m.key ? 'active' : ''}`}
                    onClick={() => setCfMethod(m.key)}
                  >
                    <span className="fyu-cf-btn-label">{m.label}</span>
                    <span className="fyu-cf-btn-desc">{m.desc}</span>
                  </button>
                ))}
              </div>
            </div>
          )}
        </div>

        {/* Drawer Footer */}
        <div className="fyu-drawer-footer">
          {engine === 'collaborative' && (
            <button className="fyu-drawer-compare-btn" onClick={handleCompare}>
              <GitCompare size={16} />
              Compare All Methods
            </button>
          )}
          <button className="fyu-drawer-apply-btn" onClick={applyAndClose}>
            <Zap size={16} />
            Apply & Load Feed
          </button>
        </div>
      </aside>
    </div>
  );
}
