import pandas as pd
import numpy as np
import re

# Carica il dataset
df = pd.read_csv('dataset/amazon.csv')

# -----------------------------
# 🔧 Pulizia e normalizzazione
# -----------------------------

# Rimozione duplicati
df.drop_duplicates(inplace=True)

# Rimozione righe completamente vuote
df.dropna(how='all', inplace=True)

# Rimozione spazi e uniformazione nomi colonne
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# Pulizia prezzi: rimuove simboli e converte in numerico
def clean_price(price):
    if pd.isnull(price):
        return np.nan
    price = re.sub(r'[^\d.]', '', str(price))
    return pd.to_numeric(price, errors='coerce')

df['actual_price'] = df['actual_price'].apply(clean_price)
df['discounted_price'] = df['discounted_price'].apply(clean_price)

# Pulizia percentuali sconto
df['discount_percentage'] = df['discount_percentage'].str.replace('%', '', regex=False).astype(float)

# Rating: rimuove outlier sopra 5 e sotto 0
df = df[df['rating'].between(0, 5, inclusive='both') | df['rating'].isna()]

# Rating count: to numeric
df['rating_count'] = df['rating_count'].astype(str).str.replace(',', '', regex=False).astype(float)

# Fill valori NaN di rating e rating_count con mediana
df['rating'].fillna(df['rating'].median(), inplace=True)
df['rating_count'].fillna(df['rating_count'].median(), inplace=True)

# Crea una colonna utile per analisi: percentuale sconto reale
df['real_discount'] = 100 * (df['actual_price'] - df['discounted_price']) / df['actual_price']
df['real_discount'] = df['real_discount'].clip(lower=0)

# -----------------------------
# 💾 Salva il file preprocessato
# -----------------------------

df.to_csv('dataset/amazon_clean.csv', index=False)
print("✅ File pulito salvato in: dataset/amazon_clean.csv")