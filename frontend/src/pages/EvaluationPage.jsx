import { useState, useEffect } from 'react';
import {
  BarChart, Bar, XAxis, YAxis, Tooltip, Legend,
  ResponsiveContainer, CartesianGrid, RadarChart,
  Radar, PolarGrid, PolarAngleAxis, PolarRadiusAxis,
} from 'recharts';
import { getEvaluationMetrics } from '../services/api';
import {
  BarChart2, Users, FileText, BrainCircuit,
  TrendingUp, Target, Layers, Award,
} from 'lucide-react';
import './EvaluationPage.css';

/* ── Label maps ────────────────────────────────────────────────── */
const CF_LABELS = {
  user_cosine: 'User Cosine',
  user_pearson: 'User Pearson',
  item_cosine: 'Item Cosine',
  item_jaccard: 'Item Jaccard',
};

const CB_LABELS = {
  tfidf: 'TF-IDF',
  lsa: 'LSA',
  word2vec: 'Word2Vec',
  feature: 'Feature-Based',
};

const KB_LABELS = {
  rule: 'Rule-Based',
  constraint: 'Constraint-Based',
  utility: 'Utility-Based',
};

/* ── Colour palettes ───────────────────────────────────────────── */
const CF_COLORS = ['#6366f1', '#8b5cf6', '#a78bfa', '#c4b5fd'];
const CB_COLORS = ['#10b981', '#34d399', '#6ee7b7', '#a7f3d0'];
const KB_COLORS = ['#f59e0b', '#fbbf24', '#fcd34d'];

/* ── Metric display config ─────────────────────────────────────── */
const CF_METRICS = [
  { key: 'precision', label: 'Precision@10', unit: '%' },
  { key: 'recall', label: 'Recall@10', unit: '%' },
  { key: 'ndcg', label: 'NDCG@10', unit: '%' },
  { key: 'hit_rate', label: 'Hit Rate@10', unit: '%' },
  { key: 'f1', label: 'F1@10', unit: '%' },
  { key: 'mrr', label: 'MRR@10', unit: '%' },
  { key: 'coverage', label: 'Coverage', unit: '%' },
];

/* ── Tooltip ───────────────────────────────────────────────────── */
const CustomTooltip = ({ active, payload, label }) => {
  if (!active || !payload?.length) return null;
  return (
    <div className="ev-tooltip glass">
      <p className="ev-tooltip-label">{label}</p>
      {payload.map((p) => (
        <p key={p.name} style={{ color: p.color }}>
          {p.name}: <strong>{p.value}%</strong>
        </p>
      ))}
    </div>
  );
};

/* ── Summary card ──────────────────────────────────────────────── */
const SummaryCard = ({ icon, label, value, unit, note, color }) => (
  <div className="ev-summary-card glass animate-in">
    <div className="ev-summary-icon" style={{ color }}>
      {icon}
    </div>
    <div className="ev-summary-body">
      <span className="ev-summary-label">{label}</span>
      <span className="ev-summary-value">
        {value}<span className="ev-summary-unit">{unit}</span>
      </span>
      {note && <span className="ev-summary-note">{note}</span>}
    </div>
  </div>
);

/* ── Metric table ──────────────────────────────────────────────── */
const MetricTable = ({ rows, cols, colors, highlight }) => (
  <div className="ev-table-wrap">
    <table className="ev-table">
      <thead>
        <tr>
          <th>Method</th>
          {cols.map((c) => <th key={c.key}>{c.label}</th>)}
        </tr>
      </thead>
      <tbody>
        {rows.map(({ key, label, data }, i) => (
          <tr key={key} className={highlight === key ? 'ev-row-best' : ''}>
            <td>
              <span className="ev-method-pill" style={{ background: colors[i] + '22', color: colors[i] }}>
                {label}
              </span>
              {highlight === key && <span className="ev-badge-best">Best</span>}
            </td>
            {cols.map((c) => (
              <td key={c.key}>
                {data[c.key] != null ? `${data[c.key]}${c.unit}` : '—'}
              </td>
            ))}
          </tr>
        ))}
      </tbody>
    </table>
  </div>
);

/* ── Main page ─────────────────────────────────────────────────── */
export default function EvaluationPage() {
  const [metrics, setMetrics] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    getEvaluationMetrics()
      .then(setMetrics)
      .catch(() => setError('Failed to load metrics. Make sure the backend is running.'))
      .finally(() => setLoading(false));
  }, []);

  /* ── Loading ───────────────────────────────────────────────── */
  if (loading) {
    return (
      <div className="ev-page">
        <div className="ev-loading">
          <div className="ev-loading-spinner" />
          <p>Computing metrics across all methods...</p>
          <p className="ev-loading-sub">First run may take up to 30 s (CB model loading)</p>
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="ev-page">
        <div className="ev-error glass">{error}</div>
      </div>
    );
  }

  const { cf, cb, kb, best_cf, best_cb, k } = metrics;

  /* ── Build CF chart data ──────────────────────────────────── */
  const cfChartData = CF_METRICS.slice(0, 4).map((m) => ({
    metric: m.label,
    ...Object.fromEntries(
      Object.entries(cf).map(([key, vals]) => [CF_LABELS[key], vals[m.key]])
    ),
  }));

  /* ── Build CB chart data ──────────────────────────────────── */
  const cbChartData = [
    { metric: 'Category Precision@10 (%)' },
    { metric: 'Coverage (%)' },
  ].map((row) => {
    const key = row.metric.startsWith('Category') ? 'precision' : 'coverage';
    return {
      ...row,
      ...Object.fromEntries(
        Object.entries(cb).map(([m, vals]) => [CB_LABELS[m], vals[key]])
      ),
    };
  });

  /* ── Build KB chart data ──────────────────────────────────── */
  const kbChartData = Object.entries(kb).map(([key, vals]) => ({
    method: KB_LABELS[key],
    Coverage: vals.coverage,
    'Avg Score': +(vals.avg_score * 20).toFixed(1),
    Results: +((vals.result_count / 80) * 100).toFixed(1),
  }));

  /* ── Build radar / cross-approach data ───────────────────── */
  const radarData = [
    { metric: 'Precision', CF: cf[best_cf]?.precision ?? 0, CB: cb[best_cb]?.precision ?? 0, KB: 0 },
    { metric: 'Hit Rate', CF: cf[best_cf]?.hit_rate ?? 0, CB: cb[best_cb]?.precision ?? 0, KB: 0 },
    { metric: 'NDCG', CF: cf[best_cf]?.ndcg ?? 0, CB: 0, KB: 0 },
    { metric: 'Coverage', CF: cf[best_cf]?.coverage ?? 0, CB: cb[best_cb]?.coverage ?? 0, KB: Math.max(...Object.values(kb).map((v) => v.coverage)) },
    { metric: 'MRR', CF: cf[best_cf]?.mrr ?? 0, CB: 0, KB: 0 },
  ];

  /* ── CF table rows ────────────────────────────────────────── */
  const cfRows = Object.entries(cf).map(([key, data]) => ({
    key, label: CF_LABELS[key], data,
  }));

  /* ── CB table rows ────────────────────────────────────────── */
  const cbRows = Object.entries(cb).map(([key, data]) => ({
    key, label: CB_LABELS[key], data,
  }));

  const bestCfData = cf[best_cf] || {};
  const bestCbData = cb[best_cb] || {};
  const maxKbCoverage = Math.max(...Object.values(kb).map((v) => v.coverage));

  return (
    <div className="ev-page">
      {/* ── Header ─────────────────────────────────────────── */}
      <header className="ev-header animate-in">
        <div className="ev-header-icon"><BarChart2 size={32} /></div>
        <div>
          <h1 className="ev-title gradient-text">Evaluation & Comparison</h1>
          <p className="ev-subtitle">
            Offline metrics for all {Object.keys(cf).length} CF methods,{' '}
            {Object.keys(cb).length} CB methods, and{' '}
            {Object.keys(kb).length} KB methods — evaluated on {k} recommendations per user.
          </p>
        </div>
      </header>

      {/* ── Summary cards ──────────────────────────────────── */}
      <section className="ev-summary-row animate-in">
        <SummaryCard
          icon={<Target size={28} />}
          label={`Best CF Precision@${k}`}
          value={bestCfData.precision ?? '—'}
          unit="%"
          note={`${CF_LABELS[best_cf]} · Leave-one-out`}
          color="#6366f1"
        />
        <SummaryCard
          icon={<TrendingUp size={28} />}
          label={`Best CF NDCG@${k}`}
          value={bestCfData.ndcg ?? '—'}
          unit="%"
          note={`${CF_LABELS[best_cf]}`}
          color="#8b5cf6"
        />
        <SummaryCard
          icon={<Layers size={28} />}
          label={`Best CB Cat. Precision@${k}`}
          value={bestCbData.precision ?? '—'}
          unit="%"
          note={`${CB_LABELS[best_cb]} · Category overlap`}
          color="#10b981"
        />
        <SummaryCard
          icon={<Award size={28} />}
          label="Max KB Coverage"
          value={maxKbCoverage}
          unit="%"
          note="Catalog coverage (no constraints)"
          color="#f59e0b"
        />
      </section>

      {/* ── CF Methods ─────────────────────────────────────── */}
      <section className="ev-section glass animate-in">
        <h2 className="ev-section-title">
          <Users size={20} className="ev-section-icon" style={{ color: '#6366f1' }} />
          Collaborative Filtering — Method Comparison
        </h2>
        <p className="ev-section-desc">
          Leave-one-out evaluation: for each of 8 test users, one known-relevant item is
          held out and we check whether each CF method ranks it in the top {k}.
        </p>

        <div className="ev-chart-wrap">
          <ResponsiveContainer width="100%" height={280}>
            <BarChart data={cfChartData} margin={{ top: 10, right: 20, left: 0, bottom: 5 }}>
              <CartesianGrid strokeDasharray="3 3" stroke="rgba(255,255,255,0.08)" />
              <XAxis dataKey="metric" tick={{ fill: 'var(--text-secondary)', fontSize: 12 }} />
              <YAxis unit="%" domain={[0, 100]} tick={{ fill: 'var(--text-secondary)', fontSize: 12 }} />
              <Tooltip content={<CustomTooltip />} />
              <Legend />
              {Object.keys(cf).map((key, i) => (
                <Bar key={key} dataKey={CF_LABELS[key]} fill={CF_COLORS[i]} radius={[4, 4, 0, 0]} />
              ))}
            </BarChart>
          </ResponsiveContainer>
        </div>

        <MetricTable
          rows={cfRows}
          cols={CF_METRICS}
          colors={CF_COLORS}
          highlight={best_cf}
        />
      </section>

      {/* ── CB Methods ─────────────────────────────────────── */}
      <section className="ev-section glass animate-in">
        <h2 className="ev-section-title">
          <FileText size={20} className="ev-section-icon" style={{ color: '#10b981' }} />
          Content-Based Filtering — Method Comparison
        </h2>
        <p className="ev-section-desc">
          Category Precision@{k}: fraction of recommended items falling in the user's
          demonstrated interest categories (ratings ≥ 4). Coverage: unique items recommended
          across all test users / catalog size.
        </p>

        <div className="ev-chart-wrap">
          <ResponsiveContainer width="100%" height={240}>
            <BarChart data={cbChartData} margin={{ top: 10, right: 20, left: 0, bottom: 5 }}>
              <CartesianGrid strokeDasharray="3 3" stroke="rgba(255,255,255,0.08)" />
              <XAxis dataKey="metric" tick={{ fill: 'var(--text-secondary)', fontSize: 12 }} />
              <YAxis unit="%" domain={[0, 100]} tick={{ fill: 'var(--text-secondary)', fontSize: 12 }} />
              <Tooltip content={<CustomTooltip />} />
              <Legend />
              {Object.keys(cb).map((key, i) => (
                <Bar key={key} dataKey={CB_LABELS[key]} fill={CB_COLORS[i]} radius={[4, 4, 0, 0]} />
              ))}
            </BarChart>
          </ResponsiveContainer>
        </div>

        <div className="ev-table-wrap">
          <table className="ev-table">
            <thead>
              <tr>
                <th>Method</th>
                <th>Cat. Precision@10 (%)</th>
                <th>Coverage (%)</th>
                <th>Avg Score</th>
              </tr>
            </thead>
            <tbody>
              {cbRows.map(({ key, label, data }, i) => (
                <tr key={key} className={best_cb === key ? 'ev-row-best' : ''}>
                  <td>
                    <span className="ev-method-pill" style={{ background: CB_COLORS[i] + '22', color: CB_COLORS[i] }}>
                      {label}
                    </span>
                    {best_cb === key && <span className="ev-badge-best">Best</span>}
                  </td>
                  <td>{data.precision}%</td>
                  <td>{data.coverage}%</td>
                  <td>{data.avg_score}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </section>

      {/* ── KB Methods ─────────────────────────────────────── */}
      <section className="ev-section glass animate-in">
        <h2 className="ev-section-title">
          <BrainCircuit size={20} className="ev-section-icon" style={{ color: '#f59e0b' }} />
          Knowledge-Based Filtering — Method Comparison
        </h2>
        <p className="ev-section-desc">
          KB methods are constraint-based and non-personalized, so leave-one-out metrics do
          not apply. We report Catalog Coverage (% of products returned with no constraints)
          and Average Utility Score.
        </p>

        <div className="ev-chart-wrap">
          <ResponsiveContainer width="100%" height={220}>
            <BarChart data={kbChartData} margin={{ top: 10, right: 20, left: 0, bottom: 5 }}>
              <CartesianGrid strokeDasharray="3 3" stroke="rgba(255,255,255,0.08)" />
              <XAxis dataKey="method" tick={{ fill: 'var(--text-secondary)', fontSize: 12 }} />
              <YAxis unit="%" domain={[0, 100]} tick={{ fill: 'var(--text-secondary)', fontSize: 12 }} />
              <Tooltip content={<CustomTooltip />} />
              <Legend />
              <Bar dataKey="Coverage" fill={KB_COLORS[0]} radius={[4, 4, 0, 0]} />
              <Bar dataKey="Avg Score" fill={KB_COLORS[1]} radius={[4, 4, 0, 0]} />
            </BarChart>
          </ResponsiveContainer>
        </div>

        <div className="ev-table-wrap">
          <table className="ev-table">
            <thead>
              <tr>
                <th>Method</th>
                <th>Catalog Coverage (%)</th>
                <th>Result Count</th>
                <th>Avg Score</th>
              </tr>
            </thead>
            <tbody>
              {Object.entries(kb).map(([key, data], i) => (
                <tr key={key}>
                  <td>
                    <span className="ev-method-pill" style={{ background: KB_COLORS[i] + '22', color: KB_COLORS[i] }}>
                      {KB_LABELS[key]}
                    </span>
                  </td>
                  <td>{data.coverage}%</td>
                  <td>{data.result_count}</td>
                  <td>{data.avg_score}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </section>

      {/* ── Cross-Approach Comparison ───────────────────────── */}
      <section className="ev-section glass animate-in">
        <h2 className="ev-section-title">
          <BarChart2 size={20} className="ev-section-icon" style={{ color: '#ec4899' }} />
          Cross-Approach Comparison (Best of Each)
        </h2>
        <p className="ev-section-desc">
          Radar comparing the best CF method ({CF_LABELS[best_cf]}), best CB method (
          {CB_LABELS[best_cb]}), and KB approach. CF uses LOO metrics; CB uses category
          precision; KB coverage is included where comparable.
        </p>

        <div className="ev-radar-wrap">
          <ResponsiveContainer width="100%" height={340}>
            <RadarChart data={radarData} margin={{ top: 10, right: 60, bottom: 10, left: 60 }}>
              <PolarGrid stroke="rgba(255,255,255,0.1)" />
              <PolarAngleAxis dataKey="metric" tick={{ fill: 'var(--text-secondary)', fontSize: 13 }} />
              <PolarRadiusAxis angle={30} domain={[0, 100]} tick={{ fill: 'var(--text-secondary)', fontSize: 10 }} />
              <Radar name={`CF (${CF_LABELS[best_cf]})`} dataKey="CF" stroke="#6366f1" fill="#6366f1" fillOpacity={0.25} />
              <Radar name={`CB (${CB_LABELS[best_cb]})`} dataKey="CB" stroke="#10b981" fill="#10b981" fillOpacity={0.25} />
              <Radar name="KB (Best)" dataKey="KB" stroke="#f59e0b" fill="#f59e0b" fillOpacity={0.25} />
              <Legend />
              <Tooltip content={<CustomTooltip />} />
            </RadarChart>
          </ResponsiveContainer>
        </div>

        <div className="ev-table-wrap">
          <table className="ev-table">
            <thead>
              <tr>
                <th>Approach</th>
                <th>Precision@10</th>
                <th>Hit Rate@10</th>
                <th>NDCG@10</th>
                <th>Coverage</th>
                <th>MRR</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>
                  <span className="ev-method-pill" style={{ background: '#6366f122', color: '#6366f1' }}>
                    CF — {CF_LABELS[best_cf]}
                  </span>
                </td>
                <td>{bestCfData.precision ?? '—'}%</td>
                <td>{bestCfData.hit_rate ?? '—'}%</td>
                <td>{bestCfData.ndcg ?? '—'}%</td>
                <td>{bestCfData.coverage ?? '—'}%</td>
                <td>{bestCfData.mrr ?? '—'}%</td>
              </tr>
              <tr>
                <td>
                  <span className="ev-method-pill" style={{ background: '#10b98122', color: '#10b981' }}>
                    CB — {CB_LABELS[best_cb]}
                  </span>
                </td>
                <td>{bestCbData.precision ?? '—'}%*</td>
                <td>—</td>
                <td>—</td>
                <td>{bestCbData.coverage ?? '—'}%</td>
                <td>—</td>
              </tr>
              <tr>
                <td>
                  <span className="ev-method-pill" style={{ background: '#f59e0b22', color: '#f59e0b' }}>
                    KB (Best)
                  </span>
                </td>
                <td>—</td>
                <td>—</td>
                <td>—</td>
                <td>{maxKbCoverage}%</td>
                <td>—</td>
              </tr>
            </tbody>
          </table>
          <p className="ev-table-footnote">* CB Precision = Category Precision (fraction of recs in user's preferred categories)</p>
        </div>
      </section>

      {/* ── Analysis ───────────────────────────────────────── */}
      <section className="ev-section glass animate-in">
        <h2 className="ev-section-title">
          <TrendingUp size={20} className="ev-section-icon" style={{ color: '#a78bfa' }} />
          Analysis & Insights
        </h2>
        <div className="ev-analysis-grid">
          <div className="ev-analysis-card">
            <h3>Which CF method performs best?</h3>
            <p>
              <strong>{CF_LABELS[best_cf]}</strong> achieves the highest NDCG@{k} ({bestCfData.ndcg}%),
              indicating it ranks the held-out item highest on average. User-based methods leverage
              cross-user rating patterns directly, while item-based methods exploit
              item–item similarity, which tends to be more stable for sparse datasets.
            </p>
          </div>
          <div className="ev-analysis-card">
            <h3>Which approach performs best overall?</h3>
            <p>
              <strong>Collaborative Filtering</strong> achieves the strongest personalised metrics
              (Precision, Recall, NDCG) because it draws on explicit user feedback — ratings from
              similar users act as a direct signal of relevance. Content-Based methods excel at
              category alignment and catalogue coverage without needing user history.
              Knowledge-Based methods offer the widest coverage and highest transparency but
              require user-specified constraints to be truly personalised.
            </p>
          </div>
          <div className="ev-analysis-card">
            <h3>Under what conditions does each approach excel?</h3>
            <ul>
              <li><strong>CF</strong> — works best when users have a rating history and the user
              base is large enough to find neighbours. Degrades under the cold-start problem.</li>
              <li><strong>Content-Based</strong> — works best when product metadata is rich and
              users have rated at least a few items (to build a profile). Not affected by user
              sparsity since it uses item features.</li>
              <li><strong>Knowledge-Based</strong> — ideal for new users or domain-specific
              constraints (e.g., budget, brand). Does not improve with more data but is always
              explainable and controllable.</li>
            </ul>
          </div>
          <div className="ev-analysis-card">
            <h3>Why do differences occur?</h3>
            <p>
              CF methods differ in <em>similarity measure</em>: Cosine treats all ratings equally
              while Pearson normalises for user rating scale, making it more robust to grade
              inflation. Item-based methods are generally more stable than user-based ones as item
              profiles change less frequently than user behaviour. CB methods differ in
              <em> text representation</em>: TF-IDF captures keyword frequency, LSA captures
              latent topics, Word2Vec captures semantic proximity, and Feature-Based uses
              structured attributes — each capturing a different aspect of product similarity.
            </p>
          </div>
        </div>
      </section>
    </div>
  );
}
