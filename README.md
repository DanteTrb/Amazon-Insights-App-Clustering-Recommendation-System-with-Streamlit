# 🛍️ Amazon Insights App

An interactive Streamlit app to explore, cluster, and generate smart recommendations on Amazon products.  
Includes preprocessing, KMeans clustering, visualizations (boxplots, t-SNE), and a data-driven suggestion system for sellers.

---

## 🚀 Demo Online

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)]
https://amazon-insight-wapp.streamlit.app
---

## 📁 Project Structure

amazon_insights_app/
├── dataset/
│ ├── amazon.csv # Original raw dataset
│ ├── amazon_clean.csv # Cleaned dataset
│ └── amazon_clustered.csv # Clustered dataset
├── models/
│ └── kmeans_model.pkl # Trained KMeans model
├── notebooks/
│ ├── preprocessing.ipynb # Data cleaning and transformation
│ └── cluster.ipynb # Clustering analysis and t-SNE
├── pages/
│ ├── 1_Descrizione.py # Data overview and stats
│ ├── 2_Clustering.py # Cluster visualizations
│ └── 3_Raccomandazioni.py # Interactive recommendation system
├── app.py # Main Streamlit app entry point
└── requirements.txt


---

## 📦 Dataset Info

The dataset contains real Amazon product information:

- Product name, price (actual/discounted), discount percentage
- Ratings and number of reviews
- Product category and description
- Image and purchase links

---

## 📊 Features

- **🧾 Data Overview**: Preview data, inspect basic stats, plot price distributions.
- **🤖 Clustering**: Group products by pricing, rating and discount using KMeans.
- **📉 Visualizations**: Boxplots, category counts, t-SNE plots for dimensionality reduction.
- **📦 Recommendation Engine**: Suggest the best category and product example based on user input.

---

## ⚙️ Setup Instructions

1. **Clone the repo**:
   ```bash
   git clone https://github.com/your_username/amazon_insights_app.git
   cd amazon_insights_app

**Install dependencies**:
pip install -r requirements.txt

**Run the app**:
streamlit run app.py

🧠 **Built With**
*Python* 🐍
Streamlit – for building the interactive UI
Pandas & NumPy – for data wrangling
Scikit-Learn – for clustering and preprocessing
Matplotlib & Seaborn – for beautiful charts

👤 **Author**
Developed with ❤️ by Dante Trabassi
Feel free to open an issue or contribute via pull request!


---

License MIT
