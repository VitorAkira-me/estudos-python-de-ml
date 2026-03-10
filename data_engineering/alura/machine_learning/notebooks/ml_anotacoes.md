Dicionário de Dados (Data Dictionary)

/ id: identificador do paciente.

/ dataset: origem do caso (Cleveland, Hungarian, Switzerland, VA Long Beach).

/ age: idade (anos).

/ sex: sexo (Male/Female).

/ cp: tipo de dor no peito (typical angina, atypical angina, non-anginal, asymptomatic).

/ trestbps: pressão arterial em repouso (mmHg).

/ chol: colesterol sérico (mg/dl).

/ fbs: glicemia em jejum > 120 mg/dl (True/False).

/ restecg: ECG em repouso (normal, st-t abnormality, lv hypertrophy).

/ thalch: frequência cardíaca máxima alcançada.

/ exang: angina induzida por exercício (True/False).

/ oldpeak: depressão do ST induzida por exercício (unidades “ST depression”).

/ slope: inclinação do segmento ST de pico (upsloping, flat, downsloping).

/ ca: número de vasos principais coloridos por fluoroscopia (0–3).

/ thal: estado talassêmico (normal, fixed defect, reversable defect).

/ num: diagnóstico (0 = sem doença; 1–4 = presença).
-------------------------------------------------------------------------

O método df.info() é importante para a inspeção estrutural do DataFrame. Ele retorna um resumo conciso do conjunto de dados, o que é fundamental na fase inicial de Data Understanding (Entendimento dos Dados):

/ Tipos de Dados (Dtypes): informa o tipo de dado de cada coluna (e.g., int64, float64, object). Isso é crucial para a preparação de dados, pois modelos de ML só aceitam entradas numéricas e colunas do tipo object (geralmente strings ou categorias) precisam ser codificadas.

/ Contagem de Valores Não-Nulos: mostra quantos valores não-nulos existem em cada coluna. A diferença entre o total de entradas e o número de não-nulos indica a presença de dados faltantes (missing data), o que direciona a necessidade de imputação ou remoção (como faremos na etapa 3: Preparação e Limpeza de Dados).

/ Uso de Memória: indica a quantidade de memória RAM utilizada pelo DataFrame, útil para trabalhar com grandes volumes de dados.
--------------------------------------------------------------

O método df.describe() é utilizado para obter um resumo estatístico descritivo das colunas, o que é a base para a Análise Exploratória de Dados (EDA) Univariada.

Para Variáveis Numéricas:

/ Tendência Central: fornece a média e a mediana (através do 50% ou segundo quartil). A diferença significativa entre média e mediana sugere assimetria na distribuição (o que pode indicar a presença de outliers ou a necessidade de transformação de dados).

/ Dispersão: apresenta o desvio-padrão (std), que mede o quão dispersos os dados estão em relação à média.

/ Range e Limites: mostra os valores mínimo e máximo (útil para identificar valores implausíveis ou erros de registro, como uma idade de 200 anos ou um colesterol de 0, mencionados na discussão sobre outliers).

/ Quartis: indica os quartis (25%, 50%, 75%), que são essenciais para construir boxplots e identificar outliers usando a regra do Intervalo Interquartil (IQR).
-------------------------------------------------------------------
Para Variáveis Categóricas (quando include='all'):

/ Contagem (count): total de entradas não-nulas.

/ Categoria Mais Frequente (top): informa a categoria mais comum.

/ Frequência da Categoria Mais Frequente (freq): indica quantas vezes a categoria mais frequente aparece (útil para avaliar o balanceamento das categorias).

/ Número de Valores Únicos (unique): essencial para verificar a cardinalidade das variáveis categóricas (se há muitas categorias, pode ser necessário agrupá-las ou usar técnicas de codificação mais robustas).

Em resumo, df.info() e df.describe() são os primeiros comandos a serem executados em qualquer projeto de Ciência de Dados, pois fornecem uma fotografia inicial da estrutura, dos tipos e da qualidade estatística dos dados, pavimentando o caminho para a preparação e modelagem subsequentes.