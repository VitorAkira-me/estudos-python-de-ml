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





