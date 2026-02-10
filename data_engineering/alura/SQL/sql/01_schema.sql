--Banco de Dados
-- └── Schema
--      └── Tabela
--           └── Dados

-- SQL (Structe Querie Language) - Consultas em bancos relacionais, tabelas que se ligam de alguma forma
-- SGBD - Sistema Gerencial de Banco de dados, estamos usando o SQLite.

---############################################---

--CREATE TABLE IF NOT EXISTS fornecedores (
--    id INTEGER,
--    nome_do_fornecedor TEXT,
--    pais_de_origem TEXT,
--    informacoes_de_contato TEXT,
--    data_de_inicio TEXT
--)

--CREATE TABLE IF NOT EXISTS pedidos (
--    id INTEGER,
--    data_do_pedido TEXT,
--    status TEXT,
--    total_do_pedido TEXT,
--    cliente TEXT,
--    data_de_envio_estimada TEXT
--)


--CREATE TABLE IF NOT EXISTS tabelaClienteDesafio (
--    id_cliente INTEGER,
--    nome_do_cliente TEXT,
--    data_de_cadastro TEXT
--)
--
--CREATE TABLE IF NOT EXISTS tabelaProdutoDesafio(
--    id_produto INTEGER,
--    nome_do_produto TEXT,
--    preco_unitario TEXT
--)
--
--CREATE TABLE IF NOT EXISTS tabelaVendasDesafio(
--    id_venda INTEGER,
--    id_cliente INTEGER,
--    id_produto INTEGER,
--    quantidade_comprada INTEGER,
--    data_da_venda TEXT
--)

--CREATE TABLE IF NOT EXISTS tabelaclientes(
--    id_cliente INT PRIMARY KEY,
--    nome_cliente VARCHAR (250),
--    informacoes_de_contato VARCHAR (250)
--);

--CREATE TABLE IF NOT EXISTS tabelacategorias(
--    id_categoria INT PRIMARY KEY,
--    nome_categoria varchar (250),
--    descricao_categoria TEXT
--);



--CREATE TABLE IF NOT EXISTS tabelaprodutos(
--    id_produto int PRIMARY KEY,
--    nome_do_produto varchar (250),
--    descricao text,
--    categoria int,
--    preco_de_compra decimal (10,2),
--    unidade varchar (50),
--    fornecedor int,
--    data_de_inclusao date,
--    FOREIGN KEY (categoria) REFERENCES tabelacategorias (id_categoria),
--    FOREIGN key (fornecedor) REFERENCES fornecedores (id)
--);
