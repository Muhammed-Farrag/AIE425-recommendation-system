import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Navbar from './components/Navbar';
import HomePage from './pages/HomePage';
import ProductDetailPage from './pages/ProductDetailPage';
import RecommendationPage from './pages/RecommendationPage';
import KnowledgeBasedPage from './pages/KnowledgeBasedPage';

export default function App() {
  return (
    <BrowserRouter>
      <Navbar />
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/product/:id" element={<ProductDetailPage />} />
        <Route path="/recommendations" element={<RecommendationPage />} />
        <Route path="/knowledge-based" element={<KnowledgeBasedPage />} />
      </Routes>
    </BrowserRouter>
  );
}
