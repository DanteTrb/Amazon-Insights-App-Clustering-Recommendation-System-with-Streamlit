🛍️ Amazon Insights App
An interactive Streamlit app to explore, cluster, and generate smart recommendations on Amazon products.
Includes preprocessing, KMeans clustering, visualizations (boxplots, t-SNE), and a data-driven suggestion system for sellers.

🚀 Demo Online


📁 Project Structure
bash
Copia
Modifica
amazon_insights_app/
├── dataset/
│   ├── amazon.csv              # Original raw dataset
│   └── amazon_clean.csv        # Cleaned dataset (preprocessed)
│   └── amazon_clustered.csv    # Clustered dataset
├── models/
│   └── kmeans_model.pkl        # Trained KMeans model
├── notebooks/
│   ├── preprocessing.ipynb     # Notebook for data cleaning
│   └── cluster.ipynb           # Exploratory clustering analysis
├── pages/
│   ├── 1_Descrizione.py        # Dataset overview and visualizations
│   ├── Clustering.py         # Cluster analysis and t-SNE
│   └── Raccomandazioni.py    # Smart recommendation system
├── requirements.txt
└── app.py                      # Main Streamlit app entry point
📦 Dataset Info
The dataset includes reviews and details about Amazon products:

Product details (name, price, discount)

Ratings and reviews

Categories and links

Cleaned and enriched for ML usage

📊 Features
Data Overview: Preview raw data, visualize price distribution and category ratings.

Clustering: Automatically group products using KMeans based on price, rating, and discount.

Visualizations: Interactive boxplots and t-SNE projections.

Recommendation Engine: Suggest categories/products to new sellers based on entered features.

⚙️ Setup Instructions
Clone the repo:

bash
Copia
Modifica
git clone https://github.com/your_username/amazon_insights_app.git
cd amazon_insights_app
Install dependencies:

bash
Copia
Modifica
pip install -r requirements.txt
Run locally:

bash
Copia
Modifica
streamlit run app.py
🤖 Built With
Python 🐍

Pandas & NumPy

Scikit-Learn (KMeans, t-SNE)

Seaborn & Matplotlib

Streamlit

📬 Contact
Developed by Dante Trabassi
Feel free to open an issue or suggestion on GitHub!
