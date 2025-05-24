import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.manifold import TSNE

# Titolo
st.title("🤖 Clustering sui Prodotti Amazon")

# Caricamento dataset
@st.cache_data
def load_data():
    return pd.read_csv("dataset/amazon_clean.csv")

df = load_data()

# Selezione feature numeriche
features = ['discounted_price', 'actual_price', 'discount_percentage', 'rating', 'rating_count', 'real_discount']
X = df[features]

# Standardizzazione
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Metodo del gomito
st.subheader("📉 Metodo del Gomito")
inertia = []
k_range = range(2, 10)
for k in k_range:
    km = KMeans(n_clusters=k, random_state=42)
    km.fit(X_scaled)
    inertia.append(km.inertia_)

fig_elbow, ax_elbow = plt.subplots()
sns.lineplot(x=list(k_range), y=inertia, marker='o', ax=ax_elbow)
ax_elbow.set_title("Metodo del Gomito")
ax_elbow.set_xlabel("Numero di cluster")
ax_elbow.set_ylabel("Inertia")
st.pyplot(fig_elbow)

# Addestramento KMeans finale con k=5
kmeans = KMeans(n_clusters=5, random_state=42)
df['cluster'] = kmeans.fit_predict(X_scaled)

# Statistiche descrittive per cluster
st.subheader("📊 Statistiche dei Cluster")
cluster_summary = df.groupby('cluster')[features].mean().round(2)
st.dataframe(cluster_summary)

# Boxplot dei prezzi reali per cluster
st.subheader("📦 Prezzo Reale per Cluster")
fig_box, ax_box = plt.subplots()
sns.boxplot(data=df, x='cluster', y='actual_price', ax=ax_box)
ax_box.set_title('Distribuzione Prezzo Reale per Cluster')
ax_box.set_ylabel('Prezzo Reale (₹)')
st.pyplot(fig_box)

# Distribuzione categorie (top 10) per cluster
st.subheader("📚 Top 10 Categorie nei Cluster")
top_categories = df['category'].value_counts().nlargest(10).index
filtered_df = df[df['category'].isin(top_categories)]

fig_cat, ax_cat = plt.subplots(figsize=(12, 6))
sns.countplot(data=filtered_df, x='category', hue='cluster', ax=ax_cat)
ax_cat.set_title('Distribuzione delle Top 10 Categorie nei Cluster')
ax_cat.set_xticklabels(ax_cat.get_xticklabels(), rotation=90)
st.pyplot(fig_cat)

# t-SNE visual
st.subheader("🌀 Visualizzazione t-SNE dei Cluster")
tsne = TSNE(n_components=2, perplexity=30, learning_rate=200, random_state=42)
tsne_results = tsne.fit_transform(X_scaled)
df['tsne_1'] = tsne_results[:, 0]
df['tsne_2'] = tsne_results[:, 1]

fig_tsne, ax_tsne = plt.subplots(figsize=(10, 6))
sns.scatterplot(data=df, x='tsne_1', y='tsne_2', hue='cluster', palette='tab10', alpha=0.7, ax=ax_tsne)
ax_tsne.set_title("📉 Visualizzazione t-SNE dei Cluster Amazon")
ax_tsne.set_xlabel("Dimensione 1")
ax_tsne.set_ylabel("Dimensione 2")
st.pyplot(fig_tsne)