# Content-Based Recommendation Engine

## Introduction
This module implements the **Phase 2 Content-Based Recommendation Engine** for the E-Commerce platform. A content-based recommender system suggests items to users by analyzing the properties (content) of items a user has interacted with in the past. It assumes that if a user liked an item, they will also like similar items.

## Architecture
The system is built with a strictly decoupled architecture:
1. **Data Loader (`data_loader.py`)**: Acts as the single source of truth. It reads mock schema, preprocesses textual data, one-hot encodes categorical data, scales numerical properties, and exposes canonical `O(1)` structures for model training.
2. **Recommenders (`base_recommender.py` & specific engines)**: Abstract base class enforcing the `fit()` and `recommend()` interfaces. All engines rely exclusively on the `DataLoader` for consistency.
3. **API Router (`router.py`)**: A FastAPI module managing the initialization lifecycle, fitting the models into memory at server startup to guarantee `O(1)` or `O(log n)` real-time inference latency via `/recommend/all`.

---

## 1. TF-IDF (Term Frequency-Inverse Document Frequency)
### Description
TF-IDF is a statistical method used to evaluate how important a specific word is to a product within the entire catalog. It analyzes textual data (`title`, `description`, `features`) and rewards words that are highly specific to a single product while penalizing generic terms.

### How it Works
It converts each product's combined text into a sparse vector matrix. We then find recommendations by calculating the Cosine Similarity between the aggregated profile of products a user previously liked and all other products.

### Inputs & Outputs
- **Input**: Unstructured product text corpus.
- **Output**: Top `K` product recommendations based on sparse cosine similarity.

### Equations
1. **Term Frequency (TF)**: 
   $$TF(t, d) = \frac{\text{Count of term } t \text{ in product } d}{\text{Total words in product } d}$$
2. **Inverse Document Frequency (IDF)**: 
   $$IDF(t) = \log\left(\frac{\text{Total Products } N}{\text{Products containing term } t}\right)$$
3. **TF-IDF Weight**: 
   $$W(t, d) = TF(t, d) \times IDF(t)$$
4. **Cosine Similarity**: 
   $$\text{similarity}(A, B) = \frac{A \cdot B}{||A|| \times ||B||}$$

---

## 2. LSA (Latent Semantic Analysis)
### Description
LSA builds upon TF-IDF by reducing the extremely sparse TF-IDF matrix into a lower-dimensional, dense matrix. It captures latent (hidden) relationships and concepts, effectively solving the "synonymy" problem (e.g., matching "laptop" and "notebook").

### How it Works
It applies **Truncated Singular Value Decomposition (SVD)** to the TF-IDF matrix, projecting products into a continuous semantic space of `N` hidden topics. Recommendations are served by computing cosine similarity in this compressed dense space.

### Inputs & Outputs
- **Input**: The fitted TF-IDF sparse matrix.
- **Output**: Top `K` product recommendations based on dense topic similarity.

### Equations
1. **Matrix Factorization (Truncated SVD)**: 
   The term-document matrix $X$ is decomposed:
   $$X \approx U \Sigma V^T$$
   *Where:*
   - $U$: Document-to-Topic matrix
   - $\Sigma$: Singular values (importance of topics)
   - $V^T$: Term-to-Topic matrix
2. **Dense Similarity**: Cosine similarity is then applied directly to the rows of the $U$ matrix.

---

## 3. Word2Vec (Neural Embeddings)
### Description
Word2Vec is a predictive neural network algorithm that learns vector representations of words based on their context. Unlike TF-IDF, it inherently understands linguistic relationships (e.g., King - Man + Woman = Queen) based on how frequently words appear near each other in sentences.

### How it Works
We train a Gensim Word2Vec model on the tokenized product texts using a CBOW (Continuous Bag of Words) or Skip-gram architecture. A product's final mathematical representation is calculated by taking the average vector of all words in its text.

### Inputs & Outputs
- **Input**: Tokenized sentences/words from product descriptions.
- **Output**: Top `K` product recommendations based on semantic vector similarity.

### Equations
1. **Skip-Gram Objective Function**: Maximizing the probability of predicting context words given a target word $w_t$:
   $$J(\theta) = \frac{1}{T} \sum_{t=1}^{T} \sum_{-c \le j \le c, j \neq 0} \log P(w_{t+j} | w_t)$$
2. **Softmax Probability**:
   $$P(w_o | w_i) = \frac{\exp(v_{w_o}'^T v_{w_i})}{\sum_{w=1}^{V} \exp(v_{w}'^T v_{w_i})}$$
3. **Product Vector Aggregation**:
   $$\text{Vector}(Product) = \frac{1}{|Words|} \sum_{w \in Product} \text{Vector}(w)$$

---

## 4. Feature-Based (Structural Matrix)
### Description
Instead of relying on textual NLP descriptions, this method calculates mathematical similarity based purely on structured metadata properties: Price, Ratings, Category Level, and Brand.

### How it Works
Numerical values (like `price` and `rating`) are normalized using Min-Max scaling to ensure they fit between `0` and `1`. Categorical values (like `category_l1`, `brand`) are One-Hot Encoded. All these transformed features are concatenated into a single structural matrix, and similarity is calculated using distance metrics.

### Inputs & Outputs
- **Input**: Structured numerical and categorical metadata fields.
- **Output**: Top `K` product recommendations based on Euclidean/Cosine similarity.

### Equations
1. **Min-Max Scaling (Normalization)**:
   $$X_{scaled} = \frac{X - X_{min}}{X_{max} - X_{min}}$$
2. **One-Hot Encoding**: A category is mapped to a binary vector. E.g., `Category = Gaming` becomes $[0, 1, 0, 0, 0]$.
3. **Cosine Similarity**: Applied identically to the resulting $N$-dimensional feature matrix.
