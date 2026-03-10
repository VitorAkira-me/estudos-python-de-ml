import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

path = "data_engineering/alura/machine_learning/data/heart_disease_uci.csv"

# Carregar dados
df = pd.read_csv(path)
print(f"Shape dos dados: {df.shape}")
print(f"\nPrimeiras linhas do dataset \n{df.head(10)}:")

# Informações gerais sobre o dataset
print("=== INFORMAÇÕES GERAIS DO DATASET ===\n")
print(df.info())
print("\n=== ESTATÍSTICAS DESCRITIVAS ===\n")
print(df.describe())
print("\n=== TOTAL DE ENTRADAS NÃO NULAS ===\n")
print(df.count())
print("\n=== ESTATÍSTICAS DESCRITIVAS ===\n")
print(df.unique())