import pandas as pd
import numpy as np
from scipy import stats
from scipy.stats import zscore
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.experimental import enable_halving_search_cv  # noqa: F401
from sklearn.model_selection import train_test_split, GridSearchCV, RandomizedSearchCV, cross_val_score, RepeatedStratifiedKFold, HalvingRandomSearchCV
from sklearn.preprocessing import StandardScaler, RobustScaler, PolynomialFeatures
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, HistGradientBoostingClassifier, ExtraTreesClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score, roc_curve, accuracy_score, precision_score, recall_score, f1_score
from sklearn.feature_selection import SelectKBest, f_classif, mutual_info_classif
from scipy.stats import randint, uniform
import mlflow
import mlflow.sklearn
import joblib
import warnings
warnings.filterwarnings('ignore')

plt.style.use('seaborn-v0_8-darkgrid')

path = "data_engineering/alura/machine_learning/data/heart_disease_uci.csv"

# Carregar dados
df = pd.read_csv(path)

#print(f"Shape dos dados: {df.shape}")
#print(f"\nPrimeiras linhas do dataset \n{df.head(10)}:")

# Informações gerais sobre o dataset
#print("=== INFORMAÇÕES GERAIS DO DATASET ===\n")
#print(df.info())
#print("\n=== ESTATÍSTICAS DESCRITIVAS ===\n")
#print(df.describe())
#print("\n=== TOTAL DE ENTRADAS NÃO NULAS ===\n")
#print(df.count())
#print("\n=== ESTATÍSTICAS DESCRITIVAS ===\n")
#print(df.unique())


##-----------------------------------------------------------------------####
##3. Análise Exploratória de Dados (EDA)
##3.1 Análise de Missing Values
# Análise de valores ausentes
#print("=== ANÁLISE DE MISSING VALUES ===\n")
#missing_values = pd.DataFrame({
#   'Coluna': df.columns,
#   'Missing_Count': df.isnull().sum(),
#   'Missing_Percentage': (df.isnull().sum() / len(df) * 100).round(2)
#})
#missing_values = missing_values[missing_values['Missing_Count'] > 0].sort_values(
#   by='Missing_Percentage', ascending=False
#)
#print(missing_values)
#
#if len(missing_values) > 0:
#   print(missing_values)
#   # Visualizar missing values
#   plt.figure(figsize=(10, 6))
#   plt.barh(missing_values['Coluna'], missing_values['Missing_Percentage'], color='coral')
#   plt.xlabel('Porcentagem de Missing Values (%)')
#   plt.title('Distribuição de Missing Values por Coluna')
#   plt.tight_layout()
#   plt.show()
#else:
#   print("Nenhum missing value detectado!")
#
#
###-----------------------------------------------------------------------####
###3.2 Análise da Variável Target
###Objetivo: Entender a distribuição da variável alvo (balanceamento de classes)
#   # Renomear variável `num` para `target`
df.rename(columns={'num': 'target'}, inplace=True)
# Converter target para binário (0 = sem doença, 1 = com doença)
# No dataset original, valores > 0 indicam presença de doença
df['target'] = (df['target'] > 0).astype(int)
print("=== DISTRIBUIÇÃO DA VARIÁVEL TARGET ===\n")
target_counts = df['target'].value_counts()
target_percentages = df['target'].value_counts(normalize=True) * 100
print("Contagem:")
print(target_counts)
print("\nPercentual:")
for idx, pct in target_percentages.items():
   label = "Sem doença" if idx == 0 else "Com doença"
   print(f"{label} ({idx}): {pct:.2f}%")
# Visualização
fig, axes = plt.subplots(1, 2, figsize=(14, 5))
# Gráfico de barras
axes[0].bar(['Sem doença', 'Com doença'], target_counts.values, color=['lightblue', 'coral'])
axes[0].set_ylabel('Frequência')
axes[0].set_title('Distribuição da Variável Target')
axes[0].grid(axis='y', alpha=0.3)
# Gráfico de pizza
axes[1].pie(target_counts.values, labels=['Sem doença', 'Com doença'],
           autopct='%1.1f%%', colors=['lightblue', 'coral'], startangle=90)
axes[1].set_title('Proporção de Classes')
plt.tight_layout()
plt.show()
# Verificar se há desbalanceamento
ratio = target_counts.min() / target_counts.max()
print(f"\nRatio de balanceamento: {ratio:.2f}")
if ratio < 0.5:
   print("⚠️ Dataset desbalanceado! Considere usar técnicas como SMOTE ou class_weight.")
else:
   print("✓ Dataset razoavelmente balanceado.")


###-----------------------------------------------------------------------####
###3.3 Análise de Outliers
###Objetivo: Identificar valores extremos que podem ser erros de medição ou casos especiais
#
#   # Colunas numéricas (excluindo id e target)
numeric_cols = df.select_dtypes(include=[np.number]).columns
numeric_cols = numeric_cols.drop(['id', 'target'])
n = len(numeric_cols)
ncols = 3
nrows = int(np.ceil(n / ncols))
fig, axes = plt.subplots(nrows, ncols, figsize=(12, 4 * nrows))
axes = axes.ravel()
for idx, col in enumerate(numeric_cols):
   sns.boxplot(x=df[col], ax=axes[idx], color='coral')
   axes[idx].set_title(f'Boxplot: {col}', fontweight='bold')
   axes[idx].set_xlabel(col)
   axes[idx].grid(axis='x', alpha=0.3)
   col_zscore = np.abs(stats.zscore(df[col].dropna()))
   outlier_count = (col_zscore > 3).sum()
   axes[idx].text(0.95, 0.95, f'Outliers: {outlier_count}',
                  transform=axes[idx].transAxes, fontsize=9,
                  verticalalignment='top', horizontalalignment='right',
                  bbox=dict(facecolor='white', alpha=0.5, edgecolor='gray'))
for ax in axes[n:]:
   fig.delaxes(ax)
plt.tight_layout()
plt.show()
#
#
###-----------------------------------------------------------------------####
###3.4 Análise de Anomalias e Valores Inválidos
###Objetivo: Identificar valores que não fazem sentido no contexto médico/clínico
print("=== ANÁLISE DE ANOMALIAS E VALORES INVÁLIDOS ===\n")

# Verificações de consistência baseadas em conhecimento de domínio
anomalies = []

# 1. Idade (deve estar entre 0 e 120)
age_anomalies = df[(df['age'] < 0) | (df['age'] > 120)]
if len(age_anomalies) > 0:
    anomalies.append(f"Idade fora do intervalo válido: {len(age_anomalies)} casos")
    
# 2. Pressão arterial (trestbps) - valores típicos: 80-200 mmHg
bp_anomalies = df[(df['trestbps'] < 80) | (df['trestbps'] > 200)]
if len(bp_anomalies) > 0:
    anomalies.append(f"Pressão arterial anormal: {len(bp_anomalies)} casos")
    print(f"⚠️ Pressão arterial anormal detectada: {len(bp_anomalies)} casos")
    print(f"   Valores: min={df['trestbps'].min()}, max={df['trestbps'].max()}")

# 3. Colesterol (chol) - valores típicos: 100-400 mg/dl
chol_anomalies = df[(df['chol'] < 100) | (df['chol'] > 400)]
if len(chol_anomalies) > 0:
    anomalies.append(f"Colesterol anormal: {len(chol_anomalies)} casos")
    print(f"⚠️ Colesterol anormal detectado: {len(chol_anomalies)} casos")
    print(f"   Valores: min={df['chol'].min()}, max={df['chol'].max()}")

# 4. Frequência cardíaca máxima (thalch) - valores típicos: 60-220 bpm
hr_anomalies = df[(df['thalch'] < 60) | (df['thalch'] > 220)]
if len(hr_anomalies) > 0:
    anomalies.append(f"Frequência cardíaca anormal: {len(hr_anomalies)} casos")
    print(f"⚠️ Frequência cardíaca anormal detectada: {len(hr_anomalies)} casos")
    print(f"   Valores: min={df['thalch'].min()}, max={df['thalch'].max()}")

# 5. Variáveis categóricas com valores fora do esperado
categorical_checks = {
    'sex': [0, 1],
    'cp': [0, 1, 2, 3],
    'fbs': [0, 1],
    'restecg': [0, 1, 2],
    'exang': [0, 1],
    'slope': [0, 1, 2],
    'ca': [0, 1, 2, 3, 4],
    'thal': [0, 1, 2, 3]
}

for col, valid_values in categorical_checks.items():
    if col in df.columns:
        invalid = df[~df[col].isin(valid_values) & df[col].notna()]
        if len(invalid) > 0:
            anomalies.append(f"{col}: {len(invalid)} valores inválidos")
            print(f"⚠️ {col}: {len(invalid)} valores fora do domínio esperado {valid_values}")

if len(anomalies) == 0:
    print("✓ Nenhuma anomalia óbvia detectada nas validações de domínio!")
else:
    print(f"\n📊 Total de tipos de anomalias detectadas: {len(anomalies)}")

# Verificar duplicados
duplicates = df.duplicated().sum()
print(f"\n=== DUPLICADOS ===")
print(f"Registros duplicados: {duplicates}")
if duplicates > 0:
    print("⚠️ Considere remover ou investigar registros duplicados")

###-----------------------------------------------------------------------####
###3.5 Análise de Distribuições
###Objetivo: Entender a distribuição das variáveis numéricas e identificar assimetrias
## Análise de distribuições
print("=== ANÁLISE DE ASSIMETRIA (SKEWNESS) E CURTOSE ===\n")

distribution_stats = []
for col in numeric_cols:
    skewness = df[col].skew()
    kurtosis = df[col].kurtosis()
    distribution_stats.append({
        'Coluna': col,
        'Skewness': round(skewness, 3),
        'Kurtosis': round(kurtosis, 3),
        'Interpretação': 'Normal' if abs(skewness) < 0.5 else ('Assimétrica à direita' if skewness > 0 else 'Assimétrica à esquerda')
    })

dist_df = pd.DataFrame(distribution_stats)
print(dist_df.to_string(index=False))

# Visualizar distribuições
fig, axes = plt.subplots(3, 5, figsize=(18, 12))
axes = axes.ravel()

for idx, col in enumerate(numeric_cols):
    if idx < len(axes):
        axes[idx].hist(df[col].dropna(), bins=30, color='skyblue', edgecolor='black', alpha=0.7)
        axes[idx].set_title(f'{col}\nSkew: {df[col].skew():.2f}', fontsize=9, fontweight='bold')
        axes[idx].set_xlabel('Valor')
        axes[idx].set_ylabel('Frequência')
        axes[idx].grid(axis='y', alpha=0.3)

# Remover subplots vazios
for idx in range(len(numeric_cols), len(axes)):
    fig.delaxes(axes[idx])

plt.suptitle('Distribuições das Variáveis Numéricas', fontsize=14, fontweight='bold', y=1.00)
plt.tight_layout()
plt.show()
#
###-----------------------------------------------------------------------####
##3.6 Análise de Correlações
##Objetivo: Identificar relações entre variáveis e detectar multicolinearidade
## Matriz de correlação apenas para colunas numéricas
corr_numeric = df.select_dtypes(include=[np.number]).corr()

# Visualizar matriz de correlação
plt.figure(figsize=(14, 10))
sns.heatmap(corr_numeric, annot=True, fmt='.2f', cmap='coolwarm', 
            center=0, square=True, linewidths=1, cbar_kws={"shrink": 0.8})
plt.title('Matriz de Correlação - Heart Disease Dataset', fontsize=14, fontweight='bold', pad=20)
plt.tight_layout()
plt.show()

# Identificar correlações fortes com o target
print("=== CORRELAÇÕES COM A VARIÁVEL TARGET ===\n")
target_corr = corr_numeric['target'].sort_values(ascending=False)
print(target_corr)

# Identificar pares de features com alta correlação (possível multicolinearidade)
print("\n=== MULTICOLINEARIDADE (Correlação entre features) ===")
print("Pares de features com correlação > 0.7:\n")

high_corr_pairs = []
for i in range(len(corr_numeric.columns)):
    for j in range(i+1, len(corr_numeric.columns)):
        if abs(corr_numeric.iloc[i, j]) > 0.7 and corr_numeric.columns[i] != 'target' and corr_numeric.columns[j] != 'target':
            high_corr_pairs.append({
                'Feature 1': corr_numeric.columns[i],
                'Feature 2': corr_numeric.columns[j],
                'Correlação': round(corr_numeric.iloc[i, j], 3)
            })

if len(high_corr_pairs) > 0:
    high_corr_df = pd.DataFrame(high_corr_pairs).sort_values(by='Correlação', ascending=False)
    print(high_corr_df.to_string(index=False))
    print("\n⚠️ Alta correlação entre features pode causar multicolinearidade!")
else:
    print("✓ Nenhuma correlação forte detectada entre features (excluindo target)")

###-----------------------------------------------------------------------####
###4. Preparação dos Dados
###4.1 Tratamento de Missing Values
print("=== TRATAMENTO DE MISSING VALUES ===\n")

# Copiar o dataframe original para preservar os dados
df_clean = df.copy()

# Imputação para variáveis numéricas: mediana
num_missing = ['trestbps', 'chol', 'thalch', 'oldpeak', 'ca']
for col in num_missing:
    if col in df_clean.columns:
        median = df_clean[col].median()
        df_clean[col].fillna(median, inplace=True)
        print(f"{col}: imputado com mediana ({median:.2f})")

# Imputação para variáveis categóricas: moda
cat_missing = ['thal', 'slope', 'fbs', 'exang', 'restecg']
for col in cat_missing:
    if col in df_clean.columns:
        mode = df_clean[col].mode()[0]
        df_clean[col].fillna(mode, inplace=True)
        print(f"{col}: imputado com moda ('{mode}')")

print("\n✓ Tratamento de missing values concluído!")
print(f"Shape após imputação: {df_clean.shape}")
print("Valores ausentes restantes por coluna:")
print(df_clean.isnull().sum())

###-----------------------------------------------------------------------####
###4.2 Codificação de Variáveis Categóricas (One-hot Encoding)
## Remova a coluna `dataset`
df_clean.drop(columns=['dataset'], inplace=True)

# One-hot encoding das variáveis categóricas relevantes
categorical_cols = ['sex', 'cp', 'restecg', 'slope', 'thal']
df_encoded = pd.get_dummies(df_clean, columns=categorical_cols, drop_first=True)

print(f"Shape após one-hot encoding: {df_encoded.shape}")
df_encoded.head()

###-----------------------------------------------------------------------####
###5. Experimentação e MVP (Minimum Viable Product)
from sklearn.model_selection import train_test_split

# Divida o dataset em features (X) e target (y)
X = df_encoded.drop(columns=['id', 'target'])
y = df_encoded['target']

# Divida em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


import mlflow
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score

mlflow.set_experiment("heart_disease_classification")

with mlflow.start_run(run_name="logistic_regression_baseline"):
    model = LogisticRegression(random_state=42)
    model.fit(X_train, y_train)

    y_pred_train = model.predict(X_train)
    y_pred_test = model.predict(X_test)

    train_accuracy = accuracy_score(y_train, y_pred_train)
    test_accuracy = accuracy_score(y_test, y_pred_test)
    test_f1 = f1_score(y_test, y_pred_test)
    test_precision = precision_score(y_test, y_pred_test)
    test_recall = recall_score(y_test, y_pred_test)

    mlflow.log_metric("train_accuracy", train_accuracy)
    mlflow.log_metric("test_accuracy", test_accuracy)
    mlflow.log_metric("test_f1_score", test_f1)
    mlflow.log_metric("test_precision", test_precision)
    mlflow.log_metric("test_recall", test_recall)

    overfitting = train_accuracy - test_accuracy
    mlflow.log_metric("overfitting", overfitting)

    mlflow.sklearn.log_model(model, "model")

    print(f"=== LOGISTIC REGRESSION ===")
    print(f"Train Accuracy: {train_accuracy:.4f}")
    print(f"Test Accuracy:  {test_accuracy:.4f}")
    print(f"Test F1 Score:  {test_f1:.4f}")

    print(f"Test Precision: {test_precision:.4f}")
    print(f"Test Recall:    {test_recall:.4f}")
    print(f"Overfitting:    {overfitting:.4f}")


###-----------------------------------------------------------------------####
###6. Persistir dataframe pré-processado
## Persistir o dataframe pré-processado
#df_encoded.to_csv("../data/heart_disease_uci_preprocessed.csv", index=False)
####-----------------------------------------------------------------------####
####7. Persistir modelo
### Persistir o modelo treinado com MLFlow
#mlflow.sklearn.log_model(model, "logistic_regression_model")
#
#
## Persistir o modelo usando joblib
#import joblib
#joblib.dump(model, "../models/baseline_model.joblib")

############################################################################################################
#Aula 3
# Criar features adicionais sobre o dataset já pré-processado (Aula 2)
df_engineered = df_clean.copy()

# Garantir presença do alvo
y = df_engineered['target']
X = df_engineered.drop(columns=['target'])

# Criar features adicionais
eps = 1

# Dar maior peso a idade (quadrática)
df_engineered['age_squared'] = df_engineered['age'] ** 2

# Relação colesterol/idade: pode indicar risco relativo
df_engineered['cholesterol_to_age'] = df_engineered['chol'] / (df_engineered['age'] + eps)  # Evitar divisão por zero

# Percentual da frequência cardíaca máxima alcançada (regra 220 - age)
# Interpretação: quão próximo do máximo previsto o paciente chegou no esforço
if 'thalch' in df_engineered.columns and 'age' in df_engineered.columns:
    predicted_max_hr = (220 - df_engineered['age']).clip(lower=1)  # evita divisão por zero
    df_engineered['max_hr_pct'] = df_engineered['thalch'] / (predicted_max_hr + eps)

# Razão pressão/colesterol: pode sinalizar perfil de risco vascular relativo
if 'trestbps' in df_engineered.columns and 'chol' in df_engineered.columns:
    df_engineered['bp_chol_ratio'] = df_engineered['trestbps'] / (df_engineered['chol'] + 1)

# Mapear flags booleanas/ binárias para 0/1
if 'fbs' in df_engineered.columns:
    df_engineered['fbs_flag'] = df_engineered['fbs'].astype(int)
if 'exang' in df_engineered.columns:
    df_engineered['exang_flag'] = df_engineered['exang'].astype(int)

# Índice de estresse: relação entre frequência máxima alcançada e pressão de repouso
# (indicador simples de capacidade cardiorrespiratória frente à pressão arterial)
if 'thalch' in df_engineered.columns and 'trestbps' in df_engineered.columns:
    df_engineered['stress_index'] = df_engineered['thalch'] / (df_engineered['trestbps'] + eps)

# Década de idade (faixa etária simples, útil para interação e interpretação)
if 'age' in df_engineered.columns:
    df_engineered['age_decade'] = (df_engineered['age'] // 10).astype(int)

# Interação idade x oldpeak: pacientes mais velhos com maior depressão ST têm maior risco
if 'age' in df_engineered.columns and 'oldpeak' in df_engineered.columns:
    df_engineered['risk_interaction'] = df_engineered['age'] * df_engineered['oldpeak']

# Flag indicando depressão ST elevada (threshold pragmático)
if 'oldpeak' in df_engineered.columns:
    df_engineered['high_st_depression_flag'] = (df_engineered['oldpeak'] > 1.0).astype(int)

# Conferência rápida das novas features adicionadas
new_feats = ['fbs_flag', 'exang_flag', 'bp_chol_ratio', 'max_hr_pct',
             'stress_index', 'age_decade', 'risk_interaction', 'high_st_depression_flag']
present = [c for c in new_feats if c in df_engineered.columns]
print(f"Novas features adicionadas ({len(present)}): {present}")

df_engineered.head(100)




# Seleção de features usando ANOVA F-value
from sklearn.feature_selection import SelectKBest, f_classif
selector_preview = SelectKBest(f_classif, k=min(25, X_train.shape[1]))
X_train_selected = selector_preview.fit_transform(X_train, y_train)


# Exemplo ajuste de modelo Decision Tree
dt = DecisionTreeClassifier(random_state=42)
dt.fit(X_train_selected, y_train)
# Exemplo ajuste de modelo Random Forest
rf = RandomForestClassifier(random_state=42)
rf.fit(X_train_selected, y_train)
# Exemplo ajuste de modelo SVM
svm = SVC(probability=True, random_state=42)
svm.fit(X_train_selected, y_train)