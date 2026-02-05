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


CREATE TABLE IF NOT EXISTS tabelaClienteDesafio (
    id_cliente INTEGER,
    nome_do_cliente TEXT,
    data_de_cadastro TEXT
)

CREATE TABLE IF NOT EXISTS tabelaProdutoDesafio(
    id_produto INTEGER,
    nome_do_produto TEXT,
    preco_unitario TEXT
)

CREATE TABLE IF NOT EXISTS tabelaVendasDesafio(
    id_venda INTEGER,
    id_cliente INTEGER,
    id_produto INTEGER,
    quantidade_comprada INTEGER,
    data_da_venda TEXT
)