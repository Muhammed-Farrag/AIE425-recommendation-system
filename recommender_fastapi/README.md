# Intelligent E-commerce Recommender System

A comprehensive web-based recommender system built with **FastAPI** backend and **HTML/CSS/JavaScript** frontend. Implements three recommendation approaches with multiple similarity algorithms.

## 🎯 Features

### Three Recommendation Approaches
1. **Collaborative Filtering** - 4 similarity methods:
   - Euclidean Distance
   - Jaccard Similarity
   - Cosine Similarity
   - KNN (K-Nearest Neighbors)

2. **Content-Based Recommendation**
   - Category matching
   - Attribute similarity
   - Feature-based filtering

3. **Knowledge-Based Recommendation**
   - Constraint-based logic
   - Rule-based filtering
   - Preference matching

### Key Features
- ✅ Real-time recommendations
- ✅ Performance metrics (Precision, Recall, RMSE, Coverage)
- ✅ Detailed explanations for each recommendation
- ✅ Custom user input for personalized recommendations
- ✅ Comprehensive analysis and comparison charts
- ✅ Responsive design for all devices

## 📋 Project Structure

```
recommender_fastapi/
├── app.py                          # Main FastAPI application
├── requirements.txt                # Python dependencies
├── algorithms/
│   ├── __init__.py
│   ├── data_manager.py            # Data management
│   ├── collaborative_filtering.py # CF algorithms
│   ├── content_based.py           # Content-based algorithms
│   └── knowledge_based.py         # Knowledge-based algorithms
├── templates/
│   ├── index.html                 # Home page
│   ├── recommendations.html       # Recommendations page
│   ├── custom.html                # Custom recommendations
│   └── analysis.html              # Analysis page
└── static/
    ├── css/
    │   └── style.css              # Main stylesheet
    └── js/
        └── script.js              # Frontend JavaScript
```

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8+
- pip or conda

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Run the Application
```bash
python app.py
```

The application will start on `http://localhost:8000`

### Step 3: Access the Web Interface
Open your browser and navigate to:
- **Home**: http://localhost:8000/
- **Recommendations**: http://localhost:8000/recommendations
- **Custom**: http://localhost:8000/custom
- **Analysis**: http://localhost:8000/analysis

## 📚 API Endpoints

### Data Endpoints
- `GET /api/users` - Get all users
- `GET /api/products` - Get all products
- `GET /api/products/category/{category}` - Get products by category

### Recommendation Endpoints
- `POST /api/recommendations/{user_id}` - Get recommendations for a user
- `POST /api/recommendations/custom` - Get custom recommendations

### Analysis Endpoints
- `GET /api/analysis/metrics` - Get evaluation metrics
- `GET /api/analysis/comparison` - Get comparison data

### Health Check
- `GET /api/health` - Health check endpoint

## 🔧 Configuration

### Modify Mock Data
Edit `algorithms/data_manager.py` to add/modify:
- Users
- Products
- Ratings

### Adjust Recommendation Parameters
Edit the algorithm files to modify:
- Number of recommendations
- Similarity thresholds
- Weighting factors

## 📊 Evaluation Metrics

The system evaluates recommendations using:
- **Precision**: Percentage of recommended items that are relevant
- **Recall**: Percentage of relevant items that are recommended
- **RMSE**: Root Mean Square Error for rating predictions
- **Coverage**: Percentage of items that can be recommended

## 🎓 How It Works

### Collaborative Filtering
1. Finds users with similar rating patterns
2. Recommends items liked by similar users
3. Uses 4 different similarity methods for comparison

### Content-Based
1. Analyzes product features and categories
2. Recommends similar products to those you liked
3. Matches user preferences with product attributes

### Knowledge-Based
1. Applies explicit constraints and rules
2. Filters products based on requirements
3. Prioritizes items matching user preferences

## 🛠️ Development

### Adding New Algorithms
1. Create a new file in `algorithms/`
2. Implement the algorithm class
3. Add endpoints in `app.py`
4. Update the frontend templates

### Customizing the UI
- Edit `static/css/style.css` for styling
- Edit `static/js/script.js` for functionality
- Edit `templates/*.html` for structure

## 📝 Notes

- Mock data is used for demonstration
- All calculations are done in-memory
- No database is required for basic operation
- Charts use Chart.js library

## 🤝 Contributing

Feel free to modify and extend the system for your needs!

## 📄 License

This project is open source and available under the MIT License.

---

**Built with FastAPI, HTML, CSS, and JavaScript**
