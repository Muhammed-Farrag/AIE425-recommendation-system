import { useState } from 'react';
import { NavLink } from 'react-router-dom';
import { PackageSearch, Users, FileText, BrainCircuit, BarChart2 } from 'lucide-react';
import './Navbar.css';

export default function Navbar() {
  const [isOpen, setIsOpen] = useState(false);

  const links = [
    { to: '/', label: 'Products', icon: <PackageSearch size={18} /> },
    { to: '/collaborative', label: 'Collaborative', icon: <Users size={18} /> },
    { to: '/content-based', label: 'Content-Based', icon: <FileText size={18} /> },
    { to: '/knowledge-based', label: 'Knowledge AI', icon: <BrainCircuit size={18} /> },
    { to: '/evaluation', label: 'Evaluation', icon: <BarChart2 size={18} /> },
  ];

  return (
    <nav className="navbar glass">
      <div className="navbar-inner">
        <NavLink to="/" className="navbar-brand">
          <span className="brand-icon">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M12 2L2 7L12 12L22 7L12 2Z" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
              <path d="M2 17L12 22L22 17" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
              <path d="M2 12L12 17L22 12" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
            </svg>
          </span>
          <span className="brand-text gradient-text">RecoMix</span>
        </NavLink>

        <button className="menu-toggle" onClick={() => setIsOpen(!isOpen)}>
          <span className={`hamburger ${isOpen ? 'open' : ''}`} />
        </button>

        <ul className={`nav-links ${isOpen ? 'active' : ''}`}>
          {links.map(link => (
            <li key={link.to}>
              <NavLink
                to={link.to}
                className={({ isActive }) => `nav-link ${isActive ? 'active' : ''}`}
                onClick={() => setIsOpen(false)}
              >
                <span className="nav-icon">{link.icon}</span>
                {link.label}
              </NavLink>
            </li>
          ))}
        </ul>
      </div>
    </nav>
  );
}
