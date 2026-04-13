# Install dependencies as needed:
# pip install kagglehub[pandas-datasets]
import kagglehub
from kagglehub import KaggleDatasetAdapter
import pandas as pd
import os

pasta_kaggle = kagglehub.dataset_download("gregorut/videogamesales")

path_csv = os.path.join(pasta_kaggle, "vgsales.csv")

df = pd.read_csv(
    path_csv,
    encoding="latin-1",
    sep=",",
    on_bad_lines="skip"
)

df.to_csv(r'C:/Users/vitor/Documents/estudos-python-de-ml/projects/data/raw/vgsales.csv', index=False)

#---------#

path_raw = 'C:/Users/vitor/Documents/estudos-python-de-ml/projects/data/raw/vgsales.csv'
df_raw = pd.read_csv(path_raw)

df_processed = df_raw.copy()
df_processed.columns = df_processed.columns.str.lower()
df_processed.to_csv("projects/data/processed/vgsales_tratado.csv", index=False)

print("Shape:", df.shape)
print("Columns:", df.columns)
print("\nDtypes:\n", df.dtypes)
print("\nValores nulos:\n", df.isnull().sum())
print("\nAmostra:\n", df.head())

df.columns = df.columns.str.lower().str.replace(" ","_")
df["year"] = df["year"].fillna(0).astype(int)
df = df.dropna(subset=["name"])
df = df.drop_duplicates()
df.to_parquet("C:/Users/vitor/Documents/estudos-python-de-ml/projects/data/processed/vgsales.parquet", index=False)