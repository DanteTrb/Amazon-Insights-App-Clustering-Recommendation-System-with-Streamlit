import streamlit as st
import pandas as pd
import joblib
import os
from sklearn.preprocessing import StandardScaler

# Titolo dell'app
st.title("🎯 Sistema di Raccomandazione Amazon")
st.write("Inserisci le caratteristiche del prodotto che vuoi vendere:")

# Caricamento modello e dataset
model_path = os.path.join("models", "kmeans_model.pkl")
data_path = os.path.join("dataset", "amazon_clustered.csv")

model = joblib.load(model_path)
df = pd.read_csv(data_path)

# Form utente
with st.form("form"):
    prezzo = st.number_input("💰 Prezzo scontato", min_value=0.0, value=500.0)
    rating = st.slider("⭐ Rating", min_value=1.0, max_value=5.0, step=0.1, value=4.0)
    sconto = st.number_input("📉 Percentuale di sconto reale", min_value=0.0, max_value=100.0, value=20.0)
    submitted = st.form_submit_button("Ottieni Raccomandazione")

# Funzione per predire cluster
def suggerisci_cluster(df, model, prezzo, rating, sconto):
    X = df[['discounted_price', 'actual_price', 'discount_percentage', 'rating', 'rating_count', 'real_discount']]
    scaler = StandardScaler()
    scaler.fit(X)

    # Feature mancanti → valori medi o derivati
    actual_price = prezzo / (1 - sconto / 100) if sconto < 100 else prezzo
    discount_percentage = sconto
    rating_count = 1000  # valore medio ipotetico

    input_features = [[prezzo, actual_price, discount_percentage, rating, rating_count, sconto]]
    input_scaled = scaler.transform(input_features)
    cluster = model.predict(input_scaled)[0]
    return cluster

# Output
if submitted:
    cluster = suggerisci_cluster(df, model, prezzo, rating, sconto)
    st.success(f"📦 Il tuo prodotto appartiene al cluster **{cluster}**")

    cluster_df = df[df['cluster'] == cluster]
    prodotto = cluster_df.sample(1).iloc[0]

    st.markdown("### 🎁 Prodotto suggerito per questo cluster:")
    st.write(f"**🛍️ Categoria**: {prodotto['category']}")
    st.write(f"**📦 Nome**: {prodotto['product_name']}")
    st.write(f"**💰 Prezzo**: ₹{prodotto['discounted_price']}")
    st.markdown(f"[🔗 Link al prodotto]({prodotto['product_link']})")
