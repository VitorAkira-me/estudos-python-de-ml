##Bibliotecas do Python
São conjuntos de módulos e funções úteis para a pessoa usuária, desenpanhando certas tarefas de acordo com a necessidade do usuário.

##Importanto biblioteca
O pip gerenciador de bibliotecas do python, vai catalogar e organizar os pacotes dentro do python.
a '!' no inicio do pip diz que é para instalar uma biblioteca no python

##Versão especifica da biblioteca
Quando escolhemos uma versão especifica da biblioteca no python, serve que continuar rodando uma aplicação que daquela versão estava funcionando, por exemplo, se uma versão mais atualizada deixou de ter alguns parametros da versão que estava rodando o codigo e instalada a versão nova, pode quebrar o código inteiro.

##Precisamos importar a biblioteca
Usamos a palavra 'import' e o nome da biblioteca

##Sabendo mais sobre algumas bibliotecas
1. A importação de métodos específicos de uma biblioteca pode trazer algumas vantagens para o nosso projeto, como:

Maior clareza no código: importar apenas os métodos que vamos usar torna o código mais claro e fácil de entender.
Redução de conflitos de nome: quando importamos uma biblioteca inteira, podemos acabar tendo conflitos de nome com outras variáveis ou funções em nosso código.
Além das formas vistas anteriormente, podemos citar mais dois exemplos que podemos encontrar ao longo de suas práticas e estudos da linguagem Python:

from nome_biblioteca import met_1, met_2
Este código resulta na importação de 2 ou mais métodos de uma biblioteca, não necessitando repetir a importação desta a cada método desejado. Podemos, por exemplo, importar 2 métodos da biblioteca random para colher uma amostra de 5 valores de uma lista de 20 valores gerada aleatoriamente com números de 0 a 99.

from random import randrange, sample

lista = []

for i in range(0, 20):
  lista.append(randrange(100))

sample(lista, 5) 
Saída: [28, 66, 53, 81, 85]

from nome_biblioteca import *
Esta forma é utilizada para importar todos os métodos de uma dada biblioteca. A diferença desta para o import nome_biblioteca é que, neste caso, não precisamos usar o nome da biblioteca para chamar um método. Podemos passar apenas o nome dele. Por exemplo, se formos calcular a raiz quadrada de certo número poderíamos seguir por uma das duas formas:

Usando import nome_biblioteca

import math 

n = int(input("Digite um número positivo para calcular sua raiz quadrada:"))
print(f"\nA raiz quadrada de {n} é igual a {math.sqrt(n)}")
Copiar código
Usando from nome_biblioteca import *

from math import * 

n = int(input("Digite um número positivo para calcular sua raiz quadrada:"))
print(f"\nA raiz quadrada de {n} é igual a {sqrt(n)}")
Note que, no segundo exemplo, suprimimos o nome math utilizando o método desejado e escrevendo o código com menos caracteres.

Atenção: A importação nesse sentido precisa de alguns cuidados:

Podemos ter choque de nomes entre as variáveis. Por exemplo: no caso de termos uma função chamada sqrt antes de importar a da biblioteca math.
Não fica explícito de onde aquela variável, método ou classe veio.