/**
 * Intelligent E-commerce Recommender System
 * Main JavaScript File
 */

// ============ API Configuration ============
const API_BASE_URL = '/api';

// ============ Utility Functions ============

/**
 * Fetch data from API
 */
async function fetchAPI(endpoint, options = {}) {
    try {
        const response = await fetch(`${API_BASE_URL}${endpoint}`, {
            headers: {
                'Content-Type': 'application/json',
                ...options.headers
            },
            ...options
        });

        if (!response.ok) {
            throw new Error(`API Error: ${response.statusText}`);
        }

        return await response.json();
    } catch (error) {
        console.error('API Error:', error);
        throw error;
    }
}

/**
 * Show toast notification
 */
function showToast(message, type = 'info') {
    const toast = document.createElement('div');
    toast.className = `toast toast-${type}`;
    toast.textContent = message;
    
    document.body.appendChild(toast);
    
    setTimeout(() => {
        toast.classList.add('show');
    }, 10);
    
    setTimeout(() => {
        toast.classList.remove('show');
        setTimeout(() => toast.remove(), 300);
    }, 3000);
}

/**
 * Format number to percentage
 */
function formatPercent(value) {
    return `${(value * 100).toFixed(1)}%`;
}

/**
 * Format number to fixed decimal
 */
function formatDecimal(value, decimals = 2) {
    return parseFloat(value).toFixed(decimals);
}

// ============ Navigation ============

/**
 * Update active navigation link
 */
function updateActiveNav() {
    const currentPath = window.location.pathname;
    
    document.querySelectorAll('.nav-link').forEach(link => {
        const href = link.getAttribute('href');
        if (href === currentPath) {
            link.classList.add('active');
        } else {
            link.classList.remove('active');
        }
    });
}

// Update nav on page load
document.addEventListener('DOMContentLoaded', updateActiveNav);

// ============ Recommendations Page ============

/**
 * Load all users for recommendations page
 */
async function loadUsers() {
    try {
        const users = await fetchAPI('/users');
        
        const select = document.getElementById('userSelect');
        if (!select) return;
        
        users.forEach(user => {
            const option = document.createElement('option');
            option.value = user.id;
            option.textContent = user.name;
            select.appendChild(option);
        });
    } catch (error) {
        console.error('Error loading users:', error);
        showToast('Error loading users', 'error');
    }
}

/**
 * Handle user selection change
 */
async function handleUserChange(e) {
    const userId = e.target.value;
    
    if (!userId) {
        const container = document.getElementById('recommendationsContainer');
        if (container) {
            container.innerHTML = '<p class="placeholder">Select a user to see recommendations</p>';
        }
        return;
    }
    
    // Show loading
    const spinner = document.getElementById('loadingSpinner');
    if (spinner) spinner.style.display = 'flex';
    
    try {
        // Fetch user profile
        const users = await fetchAPI('/users');
        const user = users.find(u => u.id == userId);
        
        if (user) {
            displayUserProfile(user);
        }
        
        // Fetch recommendations
        const response = await fetch(`${API_BASE_URL}/recommendations/${userId}`, {
            method: 'POST'
        });
        
        if (!response.ok) throw new Error('Failed to fetch recommendations');
        
        const recommendations = await response.json();
        displayRecommendations(recommendations);
    } catch (error) {
        console.error('Error:', error);
        showToast('Error loading recommendations', 'error');
        const container = document.getElementById('recommendationsContainer');
        if (container) {
            container.innerHTML = '<p class="error">Error loading recommendations</p>';
        }
    } finally {
        if (spinner) spinner.style.display = 'none';
    }
}

/**
 * Display user profile
 */
function displayUserProfile(user) {
    const profileDiv = document.getElementById('userProfile');
    if (!profileDiv) return;
    
    profileDiv.innerHTML = `
        <div class="profile-item">
            <strong>${user.name}</strong>
            <p>Budget: $${user.budget}</p>
            <p>Preferences: ${user.preferences.join(', ')}</p>
        </div>
    `;
}

/**
 * Display recommendations
 */
function displayRecommendations(recommendations) {
    const container = document.getElementById('recommendationsContainer');
    if (!container) return;
    
    let html = '';
    
    const allRecs = [
        ...recommendations.collaborativeFiltering.map(r => ({...r, type: 'cf'})),
        ...recommendations.contentBased.map(r => ({...r, type: 'cb'})),
        ...recommendations.knowledgeBased.map(r => ({...r, type: 'kb'}))
    ];
    
    if (allRecs.length === 0) {
        container.innerHTML = '<p class="placeholder">No recommendations available</p>';
        return;
    }
    
    allRecs.forEach(rec => {
        const typeClass = `rec-${rec.type}`;
        const typeLabel = rec.type === 'cf' ? 'CF' : rec.type === 'cb' ? 'CB' : 'KB';
        
        html += `
            <div class="recommendation-card ${typeClass}" data-type="${rec.type}">
                <div class="rec-header">
                    <span class="rec-badge">${typeLabel}</span>
                    <span class="rec-score">${formatDecimal(rec.score, 1)}</span>
                </div>
                <h4>Product ID: ${rec.productId}</h4>
                <p class="rec-reason">${rec.reason}</p>
                <p class="rec-method">Method: ${rec.method}</p>
            </div>
        `;
    });
    
    container.innerHTML = html;
}

/**
 * Handle filter change
 */
function handleFilterChange(e) {
    const filter = e.target.dataset.filter;
    
    // Update active button
    document.querySelectorAll('.filter-btn').forEach(btn => {
        btn.classList.remove('active');
    });
    e.target.classList.add('active');
    
    // Filter cards
    document.querySelectorAll('.recommendation-card').forEach(card => {
        if (filter === 'all') {
            card.style.display = 'block';
        } else {
            card.style.display = card.dataset.type === filter ? 'block' : 'none';
        }
    });
}

// ============ Custom Recommendations Page ============

/**
 * Handle custom form submission
 */
async function handleFormSubmit(e) {
    e.preventDefault();
    
    const name = document.getElementById('userName')?.value;
    const categories = Array.from(document.querySelectorAll('input[name="categories"]:checked'))
        .map(cb => cb.value)
        .join(',');
    const budget = document.getElementById('budget')?.value;
    
    if (!name || !categories) {
        showToast('Please fill in all fields', 'warning');
        return;
    }
    
    // Show loading
    const spinner = document.getElementById('loadingSpinner');
    if (spinner) spinner.style.display = 'flex';
    
    try {
        const formData = new FormData();
        formData.append('name', name);
        formData.append('categories', categories);
        formData.append('budget', budget);
        
        const response = await fetch(`${API_BASE_URL}/recommendations/custom`, {
            method: 'POST',
            body: formData
        });
        
        if (!response.ok) throw new Error('Failed to generate recommendations');
        
        const recommendations = await response.json();
        displayCustomResults(name, recommendations);
    } catch (error) {
        console.error('Error:', error);
        showToast('Error generating recommendations', 'error');
    } finally {
        if (spinner) spinner.style.display = 'none';
    }
}

/**
 * Display custom results
 */
function displayCustomResults(name, recommendations) {
    const resultName = document.getElementById('resultName');
    if (resultName) resultName.textContent = name;
    
    const formSection = document.getElementById('formSection');
    const resultsSection = document.getElementById('resultsSection');
    
    if (formSection) formSection.style.display = 'none';
    if (resultsSection) resultsSection.style.display = 'block';
    
    const container = document.getElementById('recommendationsContainer');
    if (!container) return;
    
    let html = '';
    
    const allRecs = [
        ...recommendations.collaborativeFiltering.map(r => ({...r, type: 'cf'})),
        ...recommendations.contentBased.map(r => ({...r, type: 'cb'})),
        ...recommendations.knowledgeBased.map(r => ({...r, type: 'kb'}))
    ];
    
    if (allRecs.length === 0) {
        container.innerHTML = '<p class="placeholder">No recommendations found</p>';
        return;
    }
    
    allRecs.forEach(rec => {
        const typeClass = `rec-${rec.type}`;
        const typeLabel = rec.type === 'cf' ? 'CF' : rec.type === 'cb' ? 'CB' : 'KB';
        
        html += `
            <div class="recommendation-card ${typeClass}" data-type="${rec.type}">
                <div class="rec-header">
                    <span class="rec-badge">${typeLabel}</span>
                    <span class="rec-score">${formatDecimal(rec.score, 1)}</span>
                </div>
                <h4>Product ID: ${rec.productId}</h4>
                <p class="rec-reason">${rec.reason}</p>
                <p class="rec-method">Method: ${rec.method}</p>
            </div>
        `;
    });
    
    container.innerHTML = html;
    
    const metricsContainer = document.getElementById('metricsContainer');
    if (metricsContainer) metricsContainer.style.display = 'block';
}

/**
 * Handle tab change
 */
function handleTabChange(e) {
    const tab = e.target.dataset.tab;
    
    // Update active tab
    document.querySelectorAll('.tab-btn').forEach(btn => {
        btn.classList.remove('active');
    });
    e.target.classList.add('active');
    
    // Filter cards
    document.querySelectorAll('.recommendation-card').forEach(card => {
        if (tab === 'all') {
            card.style.display = 'block';
        } else {
            card.style.display = card.dataset.type === tab ? 'block' : 'none';
        }
    });
}

// ============ Analysis Page ============

/**
 * Load analysis data
 */
async function loadAnalysisData() {
    try {
        const response = await fetch(`${API_BASE_URL}/analysis/metrics`);
        if (!response.ok) throw new Error('Failed to load metrics');
        
        const metrics = await response.json();
        
        displayMetricsTable(metrics);
        createCharts(metrics);
        displaySummary(metrics);
    } catch (error) {
        console.error('Error loading analysis data:', error);
        showToast('Error loading analysis data', 'error');
    }
}

/**
 * Display metrics table
 */
function displayMetricsTable(metrics) {
    const tbody = document.getElementById('metricsTableBody');
    if (!tbody) return;
    
    let html = '';
    
    for (const [method, data] of Object.entries(metrics)) {
        const methodName = method === 'collaborativeFiltering' ? 'Collaborative Filtering' :
                           method === 'contentBased' ? 'Content-Based' :
                           'Knowledge-Based';
        
        html += `
            <tr>
                <td><strong>${methodName}</strong></td>
                <td>${formatPercent(data.precision)}</td>
                <td>${formatPercent(data.recall)}</td>
                <td>${formatDecimal(data.rmse, 3)}</td>
                <td>${formatPercent(data.coverage)}</td>
                <td>${data.description}</td>
            </tr>
        `;
    }
    
    tbody.innerHTML = html;
}

/**
 * Create charts
 */
function createCharts(metrics) {
    const methods = ['CF', 'CB', 'KB'];
    const precision = [metrics.collaborativeFiltering.precision, metrics.contentBased.precision, metrics.knowledgeBased.precision];
    const recall = [metrics.collaborativeFiltering.recall, metrics.contentBased.recall, metrics.knowledgeBased.recall];
    const rmse = [metrics.collaborativeFiltering.rmse, metrics.contentBased.rmse, metrics.knowledgeBased.rmse];
    const coverage = [metrics.collaborativeFiltering.coverage, metrics.contentBased.coverage, metrics.knowledgeBased.coverage];
    
    // Precision Chart
    createBarChart('precisionChart', methods, precision, 'Precision', '#3b82f6');
    
    // Recall Chart
    createBarChart('recallChart', methods, recall, 'Recall', '#10b981');
    
    // RMSE Chart
    createBarChart('rmseChart', methods, rmse, 'RMSE', '#ef4444');
    
    // Coverage Chart
    createBarChart('coverageChart', methods, coverage, 'Coverage', '#f59e0b');
    
    // Radar Chart
    createRadarChart(methods, precision, recall, coverage);
}

/**
 * Create bar chart
 */
function createBarChart(canvasId, labels, data, label, color) {
    const canvas = document.getElementById(canvasId);
    if (!canvas) return;
    
    const ctx = canvas.getContext('2d');
    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [{
                label: label,
                data: data,
                backgroundColor: color,
                borderColor: color,
                borderWidth: 2,
                borderRadius: 5
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: true,
            plugins: {
                legend: {
                    display: true,
                    position: 'top'
                }
            },
            scales: {
                y: {
                    beginAtZero: true,
                    max: 1
                }
            }
        }
    });
}

/**
 * Create radar chart
 */
function createRadarChart(labels, precision, recall, coverage) {
    const canvas = document.getElementById('radarChart');
    if (!canvas) return;
    
    const ctx = canvas.getContext('2d');
    new Chart(ctx, {
        type: 'radar',
        data: {
            labels: labels,
            datasets: [
                {
                    label: 'Precision',
                    data: precision,
                    borderColor: '#3b82f6',
                    backgroundColor: 'rgba(59, 130, 246, 0.1)',
                    tension: 0.3
                },
                {
                    label: 'Recall',
                    data: recall,
                    borderColor: '#10b981',
                    backgroundColor: 'rgba(16, 185, 129, 0.1)',
                    tension: 0.3
                },
                {
                    label: 'Coverage',
                    data: coverage,
                    borderColor: '#f59e0b',
                    backgroundColor: 'rgba(245, 158, 11, 0.1)',
                    tension: 0.3
                }
            ]
        },
        options: {
            responsive: true,
            maintainAspectRatio: true,
            plugins: {
                legend: {
                    position: 'top'
                }
            },
            scales: {
                r: {
                    beginAtZero: true,
                    max: 1
                }
            }
        }
    });
}

/**
 * Display analysis summary
 */
function displaySummary(metrics) {
    const summary = document.getElementById('analysisSummary');
    if (!summary) return;
    
    const html = `
        <ul>
            <li><strong>Best Precision:</strong> Collaborative Filtering (${formatPercent(metrics.collaborativeFiltering.precision)})</li>
            <li><strong>Best Recall:</strong> Content-Based (${formatPercent(metrics.contentBased.recall)})</li>
            <li><strong>Best Coverage:</strong> Content-Based (${formatPercent(metrics.contentBased.coverage)})</li>
            <li><strong>Lowest RMSE:</strong> Collaborative Filtering (${formatDecimal(metrics.collaborativeFiltering.rmse, 3)})</li>
        </ul>
        <p><strong>Recommendation:</strong> Choose based on your priority:</p>
        <ul>
            <li>🎯 <strong>Accuracy:</strong> Use Collaborative Filtering</li>
            <li>📊 <strong>Diversity:</strong> Use Content-Based</li>
            <li>⚡ <strong>Constraints:</strong> Use Knowledge-Based</li>
        </ul>
    `;
    
    summary.innerHTML = html;
}

// ============ Page-specific Initialization ============

document.addEventListener('DOMContentLoaded', () => {
    const currentPath = window.location.pathname;
    
    // Recommendations page
    if (currentPath === '/recommendations') {
        loadUsers();
        const userSelect = document.getElementById('userSelect');
        if (userSelect) userSelect.addEventListener('change', handleUserChange);
        
        document.querySelectorAll('.filter-btn').forEach(btn => {
            btn.addEventListener('click', handleFilterChange);
        });
    }
    
    // Custom recommendations page
    if (currentPath === '/custom') {
        const form = document.getElementById('customForm');
        if (form) form.addEventListener('submit', handleFormSubmit);
        
        const budgetInput = document.getElementById('budget');
        if (budgetInput) {
            budgetInput.addEventListener('input', (e) => {
                const budgetValue = document.getElementById('budgetValue');
                if (budgetValue) budgetValue.textContent = e.target.value;
            });
        }
        
        const editBtn = document.getElementById('editBtn');
        if (editBtn) {
            editBtn.addEventListener('click', () => {
                const formSection = document.getElementById('formSection');
                const resultsSection = document.getElementById('resultsSection');
                if (formSection) formSection.style.display = 'block';
                if (resultsSection) resultsSection.style.display = 'none';
            });
        }
        
        document.querySelectorAll('.tab-btn').forEach(btn => {
            btn.addEventListener('click', handleTabChange);
        });
    }
    
    // Analysis page
    if (currentPath === '/analysis') {
        loadAnalysisData();
    }
});
