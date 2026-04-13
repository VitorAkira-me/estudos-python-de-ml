import pandas as pd

path_raw = 'C:/Users/vitor/Documents/estudos-python-de-ml/projects/data/raw/vgsales.csv'
df_raw = pd.read_csv(path_raw)

df_processed = df_raw.copy()
df_processed.columns = df_processed.columns.str.lower()
df_processed.to_csv("projects/data/processed/vgsales_tratado.csv", index=False)
