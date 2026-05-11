import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import Navbar from './components/Navbar';
import HomePage from './pages/HomePage';
import ProductDetailPage from './pages/ProductDetailPage';
import CollaborativePage from './pages/CollaborativePage';
import ContentBasedPage from './pages/ContentBasedPage';
import KnowledgeBasedPage from './pages/KnowledgeBasedPage';
import EvaluationPage from './pages/EvaluationPage';

export default function App() {
  return (
    <BrowserRouter>
      <Navbar />
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/product/:id" element={<ProductDetailPage />} />
        <Route path="/collaborative" element={<CollaborativePage />} />
        <Route path="/content-based" element={<ContentBasedPage />} />
        <Route path="/knowledge-based" element={<KnowledgeBasedPage />} />
        <Route path="/evaluation" element={<EvaluationPage />} />
        {/* Legacy redirects */}
        <Route path="/for-you" element={<Navigate to="/collaborative" replace />} />
        <Route path="/recommendations" element={<Navigate to="/collaborative" replace />} />
      </Routes>
    </BrowserRouter>
  );
}
