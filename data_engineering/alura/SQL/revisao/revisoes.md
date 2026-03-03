Glossário SQL
https://cdn3.gnarususercontent.com.br/2953-sqlite-conhecendo-instrucoes-sql/GLOSS%C3%81RIO%20SQL.pdf



🧠 1️⃣ Revisão conceitual (quero ouvir de você)

Responda com suas palavras, sem copiar definição:

##Pergunta 1

👉 O que é um SGBD e por que ele é essencial em um sistema de dados?

(pense em: armazenamento, segurança, concorrência, integridade)

R:
Um SGBD é o software responsável por armazenar, organizar e gerenciar dados de forma estruturada, garantindo segurança, integridade, concorrência e performance.
Ele é essencial porque permite que vários usuários e aplicações acessem e modifiquem dados ao mesmo tempo, sem corromper a informação, além de oferecer controle de acesso, recuperação de falhas e padronização das consultas.

##Pergunta 2

👉 Por que o SQLite é diferente de MySQL ou PostgreSQL?
Em que cenário ele é ideal e em qual ele não seria recomendado?

R:
O SQLite é diferente de MySQL e PostgreSQL porque ele é um banco embarcado, ou seja, não possui servidor. O banco é apenas um arquivo local que a aplicação acessa diretamente.
Ele é ideal para prototipagem, testes, aplicações locais, mobile e estudos, porque é leve e simples.
Não é recomendado para sistemas com alta concorrência, múltiplos usuários simultâneos ou grandes volumes de dados, onde bancos como PostgreSQL e MySQL são mais adequados.




##Pergunta 3

👉 Explique essa consulta como se estivesse ensinando alguém iniciante:

SELECT * FROM fornecedores;

O que cada parte faz?

R:
Está sendo criado uma query para consultar a tabela Fornecedores, o SELECT define que vamos consultar dados, o * significa que você está solicitando todas as informações da tabela, o FROM é de onde vem os dados e "fornecedores" é o nome da tabelo que estamos consultando.




🧠 2️⃣ SELECT na prática (nível entrevista)
##Pergunta 4

Qual a diferença prática entre:

SELECT * FROM pedidos;


e

SELECT cliente FROM pedidos;

R: 
A primeira query está consultando todos os dados da tabela Pedidos, enquanto a segunda query está consultando a tabela pedido que retorne apenas a coluna cliente.

👉 Quando usar cada um no mundo real?

R: 
SELECT * é util para consultar a tabela inteira para debugging e entendimento da tabela.
SELECT coluna serve para consultar apenas a coluna que queremos, é mais leve para consultar, não chama dados desnecessarios e não quebra pipelines futuros.


##Pergunta 5

Explique o papel do ; no SQL.
Por que em projetos reais ele é obrigatório?

R:
O ponto e virgula indica o fim de uma instrução em SQL.
Permite multiplas queries no mesmo script, evita ambiguidade para os parses no bando e é obrigatorio em ambientes corporativos.



🔍 3️⃣ WHERE — filtro de verdade
##Pergunta 6

Explique exatamente o que essa query faz:

SELECT * 
FROM fornecedores 
WHERE pais_de_origem = 'China';


👉 O que acontece se eu não usar aspas em 'China'?

R:
Uma query que está consultando a todos os dados da tabela de fornecedores com uma condição que pela coluna pais de origem filtrar apenas os dados que sejam da China.

Se não usar as aspas simples a query retorna erro, pois os valores são String.

##Pergunta 7

Se eu quisesse buscar pedidos pendentes, o WHERE entra antes ou depois do FROM?
Explique a ordem lógica da query.

R:
Para buscar os pedidos pendentes, a condição WHERE precisa ser depois do FROM aonde é passado o nome da tabela.
SELECT * FROM pedidos WHERE status = 'pendente'


🧪 4️⃣ DISTINCT — sem duplicidade
##Pergunta 8

Explique por que essa query faz sentido:

SELECT DISTINCT cliente 
FROM pedidos;

R:
Uma query que está consultando a tabela pedidos com uma condição DISTINCT na coluna cliente para não haver duplicidade de nomes e retornar valores únicos.

👉 O que aconteceria se não usássemos DISTINCT?
R:
Iria retornar todos os valores da coluna de clientes até mesmo com duplicados.


##Pergunta 9 (importante)

DISTINCT age sobre:

linhas?

colunas?

tabela inteira?

Explique com um exemplo simples.

R:
O DISCTINCT age sobre o conjunto de colunas que estamos selecionando, não sobre a tabela inteira.
SELECT DISTINCT cliente
FROM pedidos;

🧠 5️⃣ Conexão com Data Engineering (nível maduro)
##Pergunta 10

Por que dados duplicados são um problema sério em:

relatórios

métricas

pipelines de dados?

👉 Onde o DISTINCT entra como primeira linha de defesa?

R:
Porque retornaria resultados e métricas falsas/erradas que ocasionaria em relátorios incorretos e decisões erradas. E o DISCTIC vem para eliminar esses valores duplicados como primeira defesa de leitura, porem nao substitui modelagem, chaves primárias e validações.


🧪 6️⃣ Desafios práticos (mão na massa)
🔹 Desafio 1

Escreva a query para:

Buscar todos os produtos distintos vendidos.
(pense em tabela de vendas)

R:
SELECT DISTINCT id_produto
FROM vendas;


🔹 Desafio 2

Escreva a query para:

Listar clientes cadastrados antes de 2020, mostrando nome e data.

R:
SELECT nome, data_de_cadastro FROM clientes
WHERE data_de_cadastro < '2020-01-01';


🔹 Desafio 3 (mental)

Se uma query está retornando muitas linhas repetidas,
qual cláusula você pensa primeiro em testar?

R:
Pensaria em deixar única os dados e usuaria o DISTINCT na coluna que está com muito duplicados.
--------------------------------------------------------------
Os Sistemas de Gerenciamento de Banco de Dados (SGBD) 
é um softwarte que armazena, estrutura, concorrencia, integridade dos dados, recuperação de falhas, escalabilidade, suporte para multiplos usuarios ebackups.

1) Armazenamento Estruturado: Armazena dados de forma estruturadas, organizados em tabelas, linhas e colunas representando informações específicas. Facilitando na busca de informações e recuperação de dados.
2) Segurança: Oferecem controles de acessos, criptografia nos dados e autenticação.
3) Recuperação de Dados: Mecanismos para facilitar na recuperação de dados de maneira rápida.
4) Concorrência: Significa que váris pessoas ou aplicativos acessando e modificando os dados ao mesmo tempo, sem corrompe-los.
5) Integridade dos dados: Por meio de restrições e validaçõesa garantem a integridade evitando informações inconsistentes ou inválidas no banco de dados.
6) Escalabilidade: Permitindo que os sistemas crescam á medida que a quantidade de dados aumentam e o numero de usuarios aumentam, sem comprometer o desempenho.
7) Suporte a Multiplos Usuarios: Atende a diversos usuarios simultaneamente, gerenciando transações de forma eficiente.
8) Backup e Restauração: Facilitam a criação de cópias de segurança regulares dos dados, tornando possível a restauração em caso de perda de dados.

---------------------------------------------------------------
1) MySQL: Um SGBD de codigo aberto conhecido por sua velocidadee confiabilidade. Facil de uso para aplicativos da web compativel com diversas lingues.
2) Oracle Database: Um SGBD usado para suportar grandes volumes de dados, por empresas com fluxo maiores. Oferecendo recursos avançados de segurança, escalabilidade e recuperação.
3) Microsoft SQL Server: Amplamente utilizado para aplicativos windows em ambientes corporativos.
4) PostgreSQL: Outro SGBD de codigo aberto, conhecido por sua flexibilidase e suporte para gama de aplicativos.
5) SQLite: Um SGBD leve que não requer um servidor separado usado para aplicativos moveis, navegadores WEB.

Já MySQL e PostgreSQL são bancos cliente-servidor, projetados para múltiplos usuários, alta concorrência e grandes volumes de dados.

---------------------------------------------------------------
1.	Qual a diferença entre SELECT DISTINCT e criar uma tabela?
R: SELECT DISTINCT é consulta: retorna valores únicos de uma coluna/resultado, sem mudar o banco. CREATE TABLE é DDL: cria um objeto permanente no banco com colunas, tipos e restrições.

2.	Por que PK não pode ser repetida nem nula? O que isso evita na prática?
R: A PK garante unicidade e identificação estável de cada linha. Evita registros duplicados/ambíguos e permite relacionamentos confiáveis (FK). “Não nula” garante que toda linha seja endereçável.

3.	Em quais casos Nome_Cliente não serve como PK? Me dá 2 exemplos reais.
R: Nomes duplicados (duas “Maria Silva”).
Nome pode mudar (casamento/retificação) → PK tem que ser estável.
E sim: CPF pode falhar em cenários como estrangeiros, menores sem doc, cadastro incompleto, etc.

4.	ALTER TABLE é sempre “seguro”? Que riscos ele traz em produção?
R: Não. Pode bloquear tabela, causar downtime, quebrar queries/ETLs, invalidar índices, exigir backfill/migração e gerar incompatibilidade com aplicações. Em produção: versionamento de schema + migrações controladas.

5.	Por que uma FK normalmente referencia uma PK (ou UNIQUE)?
R: Porque a FK precisa apontar para um valor garantidamente único, senão a relação fica ambígua (um mesmo valor apontaria para várias linhas). PK/UNIQUE garante integridade referencial.

6.	O que acontece se eu tentar inserir um produto com Categoria = 999 e essa categoria não existe?
R: Se FK estiver ativa, o insert falha com erro de integridade (violação de foreign key).
Se a FK não existir (ou estiver desabilitada), o banco aceita e você cria um dado órfão (inconsistente), quebrando relatórios e joins.
Dica prática (SQLite): PRAGMA foreign_keys = ON;

7.	DECIMAL(10,2): o que significam 10 e 2? Quando isso é melhor que FLOAT?
R: 10 = precisão total (quantidade máxima de dígitos no número).
2 = escala (casas decimais).
DECIMAL é melhor que FLOAT em valores financeiros porque evita erros de arredondamento binário (FLOAT é aproximação).

8.	Qual diferença prática entre DROP TABLE e DELETE FROM tabela?
R: DROP TABLE remove a tabela inteira (estrutura + dados).
DELETE FROM tabela remove linhas (dados), mantendo a estrutura.
(Para remover coluna é ALTER TABLE ... DROP COLUMN — quando suportado.)

---------------------------------------------------------------
Principais Diferenças e Comandos:
DDL (Estrutura):
CREATE: Cria novos objetos, como bancos de dados ou tabelas.
ALTER: Modifica a estrutura de um objeto existente (ex: adicionar uma coluna).
DROP: Exclui objetos do banco de dados.
TRUNCATE: Remove todos os registros de uma tabela, mas mantém a estrutura.
Características: As alterações são geralmente irreversíveis (auto-commit).

DML (Dados):
SELECT: Recupera dados de tabelas.
INSERT: Adiciona novos dados.
UPDATE: Atualiza dados existentes.
DELETE: Remove linhas de uma tabela.
Características: Permite reverter as alterações (rollback) antes de confirma