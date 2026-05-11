/**
 * API Service Layer
 * Centralised API calls to the FastAPI backend.
 */
import axios from 'axios';

const API_BASE = 'http://localhost:8000';

const api = axios.create({
  baseURL: API_BASE,
  headers: { 'Content-Type': 'application/json' },
});

// ── Products ────────────────────────────────────────────────────
export const getProducts = (params = {}) =>
  api.get('/products', { params }).then(r => r.data);

export const getProductById = (id) =>
  api.get(`/products/${id}`).then(r => r.data);

export const getCategories = () =>
  api.get('/products/meta/categories').then(r => r.data.categories);

export const getBrands = () =>
  api.get('/products/meta/brands').then(r => r.data.brands);

// ── Users ───────────────────────────────────────────────────────
export const rateProduct = (userId, productId, rating) =>
  api.post('/users/rate', { user_id: userId, product_id: productId, rating }).then(r => r.data);

export const getUserRatings = (userId) =>
  api.get(`/users/ratings/${userId}`).then(r => r.data);

// ── Recommendations ─────────────────────────────────────────────
export const getRecommendations = (method, inputData) =>
  api.post(`/recommend/${method}`, inputData).then(r => r.data);

export const getKnowledgeBasedRecommendations = (kbMethod, inputData) =>
  api.post(`/recommend/knowledge-based/${kbMethod}`, inputData).then(r => r.data);

export const compareKnowledgeBased = (inputData) =>
  api.post('/recommend/knowledge-based-compare', inputData).then(r => r.data);

// ── Collaborative Filtering ────────────────────────────────────
export const getCollaborativeRecommendations = (cfMethod, inputData) =>
  api.post('/recommend/collaborative', { ...inputData, cf_method: cfMethod }).then(r => r.data);

export const compareCollaborative = (inputData) =>
  api.post('/recommend/collaborative-compare', inputData).then(r => r.data);

// ── Content-Based ──────────────────────────────────────────────
export const getContentBasedRecommendations = (cbMethod, inputData) =>
  api.post('/recommend/content-based', { ...inputData, cb_method: cbMethod }).then(r => r.data);

export const compareContentBased = (inputData) =>
  api.post('/recommend/content-based-compare', inputData).then(r => r.data);

// ── Evaluation ──────────────────────────────────────────────────
export const getEvaluationMetrics = () =>
  api.get('/evaluate/metrics').then(r => r.data);

export default api;
