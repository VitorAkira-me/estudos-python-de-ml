O curso é voltado para aprender sobre "Árvores de Decisão"

Na imagem está sendo mostrado uma arvore de decisão.
![alt text](image.png)

ALGORITMO
CART (Classification and regression tree)
![alt text](image-1.png)

Um exemplo de dados
![alt text](image-2.png)

Dentro de uma tabela existe alguns "ATRIBUTOS" que podem ser bom ou ruim para divisão da arvore.
Porem como sabemos o quão boa são esses "ATRIBUTOS"?
Existe algumas métricas para calcular o índice de impureza GINI.
![alt text](image-3.png)
Basicamente essa métrica calcula o quão puro é um nó, quanto mais puro for o nó, siginifica que o nó possuiu mais transações de uma mesma classe. 
A classe usada como exemplo foi fraude ou não fraude, se por exemplo o nó voltar 100% fraude, quer dizer que ele é totalmente puro, pois conseguimos classificar todos em uma mesma classe.

E como fazer os calculos?
Calculo do primeiro nó da esquerda SIM.
Primeiro os Pk
![alt text](image-4.png)
formula = p1 = 1/3 (1 = Fraude e 3 = Transações)
p1 = 0.33 (Dizendo que 33% são fraudes)

p2 = 2/3 (2 = Não fraudes e 3 = Transações)
p2 = 0.66 (Dizendo que 66% não são fraudes)

O indice GINI calculcar primeiro cada nó separadamente e depois fazemos um somatorio do indice da arvore.

Na imagem como exemplo mostra como é feito o calculo da formula que nos devolve o resultado de 44% impuro. 
0% é um nó puro, sendo uma divisão perfeita.
![alt text](image-5.png)
---
Calculo do segundo nó da direita NÃO.
![alt text](image-6.png)
Agora calculcar o indice GINI
p1 = 1/2
p2 = 1/2

p1 = 0.50
p2 = 0.50

Forumula para p1 e p2
![alt text](image-7.png)
Resultado de 50% de impureza no nó da direita.
---
Agora com os valores G de cada nó (G=0.44 e G=0.50) para calculcar o GINI da arvore Gtree

Precisamos primeiro no peso de cada nó, que é com base na QUANTIDADE de transações de cada nó.

![alt text](image-8.png)

fazemos a divisão 3/5 = 0.60 e 2/5 = 0.40

usamos a formula Gtree:
Gtree = (0.44 * 0.60) + (0.50 * 0.40)
Gtree = 0.26 + 0.20
Gtree = 0.46

Resultado que:
A arvore é 46% impura.
----------------------------------------------------
![alt text](image-9.png)
Vamos escolher o GINI de menor valor, quanto menor o valor = melhor.

![alt text](image-10.png)
Podemos ver que do lado direito so tem 1 transação, então podemos colocar a classificação como FRAUDE.

Do lado esquerdo precisa fazer as contas do GINI.

![alt text](image-11.png)

Olhando para a arvore, foi decidido uma hierarquia de tamanho 2, quanto maior a arvoro, mais complexo.

![alt text](image-12.png)
No final analizando a arvore, faz sentido.
---------------------------------------------------
Alem de problemas de classificação, porem se tiver problema de REGRESSÃO?
Exemplo de dados:
![alt text](image-13.png)

Temos as propabilidades daquela transição ser uma fraude.

Primeiro passo é dividir as transções no atributo país, e agora vamos colocar as probabilidades de cada nó, depois é calculcar a média de cada nó (43% - 80%)
![alt text](image-14.png)

Dessa vez vamos utilizar a formúla de RSS (A soma dos quadrados dos resídiuos), quanto menor o valor/residuos é mais proximo da média, esse é o objetivo, significa que os valores represente aquele nó.
![alt text](image-15.png)

Depois precisamos somar todos os valores para chegar no valor de RSS da arvore.
![alt text](image-16.png)

Final dos resultados:
![alt text](image-17.png)
----------------------------------------------------------------------
1. temos que dividir os dados de treino (construir o modelo) e dados de teste (testar o modelo)
2. Como vimos que esta desbalanceados vamos utilizar um método do Scikit Learn, que é chamado de Stratified Shuffle Split.

3. em vez de tirar um conjunto inteiro de dados, desse conjunto pegamos 10% pra teste e 90% pra treino.
4. E oque o metodo faz é separar pela porcentagem 10% de teste e 90% de treino apenas do numero de fraudes, e faremos a mesma coisa para as transações normais 10% de teste e 90% de treino

5. Modelos preditivos servem para saber o que pode acontecer no futuro com base nos dados do passado, teste e treino servem para evitar overfitting, treino = O modelo aprende padrões e teste = modelo prova que aprendeu. Sem teste você não sabe se o modelo generaliza.
6. Stratified mantém a proporção de classes, pois cria aleatoriedade mantendo a proporção. Porque se quase nenhuma é fraude tanto com treino quanto com teste, o teste seria zero fraude.

É descobrir padrões como:
Se V17 <= -2
E V14 <= -3
Então alta probabilidade de fraude

Isso é regra de decisão.

Isso é aprendizado supervisionado.

7. O modelo pode parecer perfeito, pode ter uma acurracy altissima, porem nao significa que aprendeu os padrões REAIS, significa que apenas memorizou os dados = OVERFITTING
Ele aprende o passado perfeitamente, porem quando aparece uma transação nova, ele falha.
É como estudar exatamente as perguntas da prova
e depois pegar uma prova diferente.

8. Quando a árvore cresce sem limite em dados desbalanceados, ela tende a memorizar padrões raros da classe minoritária, criando regras muito específicas e levando ao overfitting, o que compromete a generalização para novos dados.

Árvore de decisão cresce até:
separar completamente os dados
ou até não conseguir mais dividir

Em dados extremamente desbalanceados:
Ela pode criar regras muito específicas como:

Se V17 <= -1.732
E V10 <= -5.123
E Time <= 123456.78
E Amount <= 345.12
E ...

Ela vai criando divisões cada vez mais específicas.
Isso pode resultar em:

Gini = 0 em quase todos os nós finais.

Treino → perfeito
Teste → pode cair bastante
-------------------------------------------------------------------------
🏗 Arquitetura completa (do jeito certo)
1️⃣ Dados chegam

Transações chegam via:

API

Kafka

Banco relacional

Streaming


2️⃣ Data Lake (Bronze)

Dados crus, exatamente como chegaram.

Sem transformação.

Só ingestão.

3️⃣ Silver (limpeza + padronização)

Aqui acontece:

tratamento de nulos

normalização

padronização de tipos

remoção de inconsistências

Agora os dados estão confiáveis.

4️⃣ Feature Engineering (a parte que você perguntou)

Essa é a parte MAIS importante para ML.

Feature engineering = criar novas variáveis úteis para o modelo.

Exemplos reais de fraude:

Quantidade de transações do cliente nas últimas 2 horas

Valor médio das últimas 5 transações

Desvio padrão do valor

Distância geográfica entre duas compras

Frequência de compra noturna

Isso não vem pronto no dataset.

Você cria.

E muitas vezes isso vale mais que o modelo.

📌 80% do ML é feature engineering.


5️⃣ Aplicação do modelo

Você pega as features prontas e roda:

modelo.predict()

ou

modelo.predict_proba()

Agora você tem:

Probabilidade de fraude = 0.87

6️⃣ Tomada de decisão automática

Se probabilidade > 0.7:

bloqueia

pede validação

marca como suspeita

7️⃣ Log da decisão

Salva:

features usadas

probabilidade

decisão tomada

Isso é importante para auditoria.

8️⃣ Power BI

Agora o BI mostra:

Fraudes detectadas hoje

Probabilidade média

Falsos positivos

Economia gerada

Agora BI vira monitoramento do modelo.
-------------------------------------------------------
Memorizar → aprende regras extremamente específicas dos dados vistos.

Aprender padrão → aprende estrutura estatística que se mantém em novos dados.

Se não houver fraude no teste, métricas como Recall e Precision perdem significado.

10% de teste e 90% de treino - Teste mede generalização
---------------------------------------------------------
1. treinou demais / armazenou padrões

Isso é exatamente o ponto:

👉 GINI baixo só prova que o modelo organizou bem o TREINO, não que ele entende o mundo real.

Resumo mental rápido:

treino → aprender regras

teste → provar que não decorou

Instável =
👉 pequenas mudanças nos dados causam grandes mudanças nas métricas.

E isso acontece quando:

✅ existem pouquíssimos exemplos da classe importante.

👉 Quanto MENOS exemplos da classe rara, MAIS instáveis são as métricas.

👉 Quanto MAIS exemplos, MAIS confiável é a avaliação.


Quando o teste possui apenas uma fraude, as métricas ficam instáveis, pois um único erro ou acerto altera drasticamente o resultado, tornando a avaliação do modelo pouco confiável.
--------------------------------------------
Dataset desbalanceado NÃO é o problema principal.
O verdadeiro problema é:

👉 avaliar o modelo com poucos exemplos da classe crítica.

Por isso existem técnicas como:

Stratified Split ✅ (você já viu)

Cross Validation

Oversampling (SMOTE)

Undersampling

Ajuste de threshold
-------------------------------------------
Accuracy alta não quer dizer que o nó foi puro

Cuidado aqui.

Accuracy não mede pureza de nó.
Ela mede:

(acertos totais) / (total de previsões)
----------------------------------
Realidade	| Modelo disse	| Nome
Fraude	    | Fraude	    | ✅ True Positive (TP)
Não fraude	| Não fraude	| ✅ True Negative (TN)
Não fraude	| Fraude	    | ⚠️ False Positive (FP)
Fraude      | Não fraude	| 🚨 False Negative (FN)


o que REALMENTE era fraude → y_test
o que o modelo ACHOU → y_pred

Confusion Matrix (A BASE DE TUDO)
Quantas vezes o modelo acertou e errou?
[[28419   13]
 [   13   36]]

1. Primeira linha (compras normais)
28419 vezes: era normal - modelo disse normal - ✅ ACERTO
13 vezes: era normal - modelo disse fraude - ❌ bloqueou cliente inocente

2. Segunda linha (fraudes)
13 vezes: era fraude - modelo disse normal - ❌ fraude passou
36 vezes: era fraude - modelo disse fraude - ✅ salvou dinheiro

| Realidade | Modelo | Resultado           |
| --------- | ------ | ------------------- |
| Normal    | Normal | ✅                   |
| Normal    | Fraude | ❌ cliente bloqueado |
| Fraude    | Normal | ❌ prejuízo          |
| Fraude    | Fraude | ✅ proteção          |


2️⃣ Accuracy (Acurácia)
Conta TODOS os acertos:
28419 + 36
Divide pelo total.

Problema:
Como quase tudo é normal,
acertar normal já dá nota alta.
Por isso ela engana em fraude.

1) Tradução humana
Accuracy = nota geral da prova.
Mas a prova tem 99 perguntas fáceis e 1 difícil.

3️⃣ Precision (Precisão)
Pergunta:
Quando o modelo GRITOU “FRAUDE”, ele estava certo?

Olhamos só para os casos onde ele acusou fraude.
Entre esses:
quantos eram fraude de verdade?
Tradução humana
Precision mede:

👉 quantos clientes inocentes você bloqueou sem querer.

Precision alta =
modelo só acusa quando tem certeza.

3. Quando a Precision fica baixa?

Quando o modelo vira paranoico:

🚨 FRAUDE
🚨 FRAUDE
🚨 FRAUDE

Ele pega fraude…
mas também bloqueia muita compra normal.

Resultado:

Clientes irritados.
----------------------------------
4️⃣ Recall (Sensibilidade)
Pergunta:
Das fraudes que EXISTIAM, quantas eu consegui pegar?

Aqui olhamos todas as fraudes reais.
E vemos quantas o modelo capturou.

Tradução humana
Recall mede:

👉 quanto dinheiro você conseguiu salvar.

Recall alto =
poucas fraudes escapam.

4. Recall pergunta outra coisa:

Das fraudes que EXISTIAM, quantas eu consegui pegar?

Então:

Precision olha para os ALARMES

Recall olha para as FRAUDES REAIS
--------------------------------
🧩 RESUMO DEFINITIVO
| Métrica          | Pergunta humana             |
| ---------------- | --------------------------- |
| Confusion Matrix | O que exatamente aconteceu? |
| Accuracy         | Acertei no geral?           |
| Precision        | Bloqueei só quem devia?     |
| Recall           | Peguei as fraudes?          |
------------------------------------------------------------------

🎯 Visual definitivo (guarda isso)

Imagine:
Existiam 100 fraudes.

O modelo marcou 200 compras como fraude.

Entre essas 200:

80 eram fraude

120 eram normais

Então:

Precision:

80 / 200 = 40%


Recall:

80 / 100 = 80%


👉 Pegou bastante fraude (recall bom)
👉 Mas acusou muita gente inocente (precision ruim)
----------------------------------------------------------
🧠 Consolidação final (guarda isso)

Pensa sempre assim:

🔵 Recall

Olha para as fraudes reais.

Pergunta:

Eu consegui capturar elas?

Fraude escapando → Recall baixo.

🟢 Precision

Olha para os alarmes do modelo.

Pergunta:

Quando eu acusei fraude, eu estava certo?

Muitos clientes inocentes bloqueados → Precision baixa.

🟡 Accuracy

Olha tudo misturado.

Pergunta:

Acertei no geral?

Em fraude, quase sempre engana.

⚫ Confusion Matrix

É o “placar completo”.
Todas as métricas nascem dela.
----------------------------------------------------------

2. A grande ideia: Ensemble Learning

Aqui vem o pulo do gato.

Em vez de confiar em UMA árvore, fazemos:

várias árvores pequenas trabalhando juntas.

Pensa assim:

👤 1 especialista → pode errar
👥 100 especialistas → decisão mais confiável

Isso é Ensemble Learning.
---
3. Bagging (Bootstrapping + Aggregating)

Agora entra o conceito mais importante da aula.

✅ Bootstrapping (amostragem)

O algoritmo pega o dataset e cria vários subconjuntos aleatórios:

Dataset original:
1 2 3 4 5 6 7 8 9 10 ...

Amostra A → [1,12,17,9,14]
Amostra B → [1,3,11,4,5]
Amostra C → [3,7,16,17,20]

Cada amostra cria uma árvore diferente.

👉 Cada árvore aprende uma visão diferente do problema.
---
Aggregating (agregação)

Depois todas votam:

Árvore 1 → FRAUDE
Árvore 2 → NÃO FRAUDE
Árvore 3 → FRAUDE

Resultado final:

👉 maioria vence = FRAUDE

Isso reduz muito erro individual.
---
4. Random Forest (a floresta)

Random Forest = Bagging + aleatoriedade extra.

Cada árvore:

✅ usa transações aleatórias
✅ usa atributos aleatórios (país, valor, média…)

Então nenhuma árvore fica igual à outra.

Visualmente:
        🌳
     🌳 🌳 🌳
   🌳 🌳 🌳 🌳

Cada árvore é fraca sozinha.

Mas juntas → modelo forte.
---
5. O que são Out-of-Bag (OOB)?

Isso é MUITO importante.

Quando uma árvore é criada:

ela usa só parte dos dados

os dados não usados viram teste automático

Exemplo:

Árvore A1 treinou com:
[1,2]

Então valida com:
[3,4,5]

Isso chama:

👉 Out of Bag samples

É como ter um mini validation set grátis.
---
6. O voto final (parte da tabela)

Na aula:

Transação	A1	A2	Resultado
5	SIM	SIM	✅ SIM

As árvores votam.

Random Forest decide pela maioria.
---
7. Por que Random Forest melhora métricas?

Porque ele:

✅ reduz overfitting
✅ reduz variância
✅ evita decisões extremas de uma única árvore

Resultado da aula:

Modelo	Recall
Árvore simples	0.73
Random Forest	0.75

Pequena melhora, mas muito mais robusto.
---
8. A árvore tenta achar:

"qual regra perfeita?"

Random Forest pensa:

"qual decisão é consistente entre várias visões?"

Isso é exatamente o que modelos reais fazem.
---
Decision Tree
→ aprende regras

Overfit
→ árvore profunda demais

Bagging
→ várias árvores com amostras diferentes

Random Forest
→ várias árvores + atributos aleatórios

Resultado
→ votação final mais estável