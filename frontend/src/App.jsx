import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import Navbar from './components/Navbar';
import HomePage from './pages/HomePage';
import ProductDetailPage from './pages/ProductDetailPage';
import ForYouPage from './pages/ForYouPage';
import KnowledgeBasedPage from './pages/KnowledgeBasedPage';

export default function App() {
  return (
    <BrowserRouter>
      <Navbar />
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/product/:id" element={<ProductDetailPage />} />
        <Route path="/for-you" element={<ForYouPage />} />
        <Route path="/knowledge-based" element={<KnowledgeBasedPage />} />
        {/* Backwards compat redirect */}
        <Route path="/recommendations" element={<Navigate to="/for-you" replace />} />
      </Routes>
    </BrowserRouter>
  );
}
