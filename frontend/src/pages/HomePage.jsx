import { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import ProductCard from '../components/ProductCard';
import { getProducts, getCategories, getBrands } from '../services/api';
import { Search, PackageOpen } from 'lucide-react';
import './HomePage.css';

export default function HomePage() {
  const [products, setProducts] = useState([]);
  const [categories, setCategories] = useState([]);
  const [brands, setBrands] = useState([]);
  const [loading, setLoading] = useState(true);
  const [filters, setFilters] = useState({
    search: '',
    category: '',
    brand: '',
    maxPrice: '',
    sort_by: 'rating',
    order: 'desc',
  });
  const navigate = useNavigate();

  // Load categories & brands on mount
  useEffect(() => {
    Promise.all([getCategories(), getBrands()])
      .then(([cats, brds]) => {
        setCategories(cats);
        setBrands(brds);
      })
      .catch(console.error);
  }, []);

  // Fetch products whenever filters change (debounced)
  useEffect(() => {
    const timer = setTimeout(() => {
      setLoading(true);
      const params = {};
      if (filters.search) params.search = filters.search;
      if (filters.category) params.category = filters.category;
      if (filters.brand) params.brand = filters.brand;
      if (filters.maxPrice) params.max_price = parseFloat(filters.maxPrice);
      params.sort_by = filters.sort_by;
      params.order = filters.order;

      getProducts(params)
        .then(setProducts)
        .catch(console.error)
        .finally(() => setLoading(false));
    }, 300);
    return () => clearTimeout(timer);
  }, [filters]);

  const updateFilter = (key, value) => {
    setFilters(prev => ({ ...prev, [key]: value }));
  };

  return (
    <div className="home-page">
      {/* Hero Section */}
      <section className="hero">
        <div className="hero-blob hero-blob-1" />
        <div className="hero-blob hero-blob-2" />
        <div className="hero-content animate-in">
          <h1 className="hero-title">
            Discover Products <br />
            <span className="gradient-text animated-gradient">Curated by Autonomous Agents</span>
          </h1>
          <p className="hero-subtitle">
            Experience a personalized shopping journey guided by intelligent agents. Our specialized recommendation engines analyze your unique preferences to find exactly what you need.
          </p>
        </div>
      </section>

      {/* Filters Section */}
      <section className="filters-section">
        <div className="filters-bar glass">
          <div className="search-wrapper">
            <span className="search-icon"><Search size={16} /></span>
            <input
              id="search-input"
              type="text"
              placeholder="Search products..."
              value={filters.search}
              onChange={(e) => updateFilter('search', e.target.value)}
              className="search-input"
            />
          </div>

          <div className="filter-group">
            <select
              id="category-filter"
              value={filters.category}
              onChange={(e) => updateFilter('category', e.target.value)}
              className="filter-select"
            >
              <option value="">All Categories</option>
              {categories.map(c => <option key={c} value={c}>{c}</option>)}
            </select>

            <select
              id="brand-filter"
              value={filters.brand}
              onChange={(e) => updateFilter('brand', e.target.value)}
              className="filter-select"
            >
              <option value="">All Brands</option>
              {brands.map(b => <option key={b} value={b}>{b}</option>)}
            </select>

            <input
              id="max-price-filter"
              type="number"
              placeholder="Max Price"
              value={filters.maxPrice}
              onChange={(e) => updateFilter('maxPrice', e.target.value)}
              className="filter-input"
              min="0"
            />

            <select
              id="sort-filter"
              value={`${filters.sort_by}-${filters.order}`}
              onChange={(e) => {
                const [sort_by, order] = e.target.value.split('-');
                setFilters(prev => ({ ...prev, sort_by, order }));
              }}
              className="filter-select"
            >
              <option value="rating-desc">Rating ↓</option>
              <option value="rating-asc">Rating ↑</option>
              <option value="price-desc">Price ↓</option>
              <option value="price-asc">Price ↑</option>
              <option value="name-asc">Name A-Z</option>
              <option value="name-desc">Name Z-A</option>
            </select>
          </div>
        </div>

        <div className="results-count">
          {loading ? 'Loading...' : `${products.length} products found`}
        </div>
      </section>

      {/* Product Grid */}
      <section className="products-grid">
        {loading ? (
          Array.from({ length: 8 }).map((_, i) => (
            <div key={i} className="skeleton-card glass" />
          ))
        ) : products.length === 0 ? (
          <div className="empty-state">
            <span className="empty-icon"><PackageOpen size={48} /></span>
            <h3>No products found</h3>
            <p>Try adjusting your filters</p>
          </div>
        ) : (
          products.map((product, i) => (
            <ProductCard
              key={product.id}
              product={product}
              onClick={() => navigate(`/product/${product.id}`)}
            />
          ))
        )}
      </section>
    </div>
  );
}
