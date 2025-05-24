import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Imposta il titolo della pagina
st.title("📊 Overview del Dataset Amazon")

# Caricamento dataset pulito
@st.cache_data
def load_data():
    path = os.path.join("dataset", "amazon_clean.csv")
    return pd.read_csv(path)

df = load_data()

# Mostra dimensione e prime righe
st.subheader("🧾 Anteprima Dati")
st.write(f"Numero di righe: {df.shape[0]} | Numero di colonne: {df.shape[1]}")
st.dataframe(df.head())

# Statistiche descrittive principali
st.subheader("📈 Statistiche Descrittive")
st.write(df[["discounted_price", "actual_price", "discount_percentage", "rating", "rating_count"]].describe())

# Grafico 1 – Distribuzione dei prezzi scontati
st.subheader("💰 Distribuzione dei Prezzi Scontati")
fig1, ax1 = plt.subplots()
sns.histplot(df["discounted_price"], bins=30, kde=True, ax=ax1, color="green")
ax1.set_xlabel("Prezzo Scontato")
ax1.set_ylabel("Frequenza")
ax1.tick_params(axis='x', labelrotation=45, labelsize=8)
plt.tight_layout()
st.pyplot(fig1)

# Grafico 2 – Valutazione media per categoria (top 10)
st.subheader("⭐ Valutazione Media per Categoria")
top_cat = df["category"].value_counts().nlargest(10).index
df_top = df[df["category"].isin(top_cat)].copy()
df_top["rating"] = pd.to_numeric(df_top["rating"], errors='coerce')  # Assicura tipo numerico

mean_rating = df_top.groupby("category")["rating"].mean().sort_values(ascending=False)

fig2, ax2 = plt.subplots()
mean_rating.plot(kind="bar", ax=ax2, color="orange")
ax2.set_ylabel("Valutazione Media")
plt.tight_layout()
st.pyplot(fig2)

# Footer
st.markdown("---")
st.markdown("📁 *Fonte dati: dataset Amazon*")