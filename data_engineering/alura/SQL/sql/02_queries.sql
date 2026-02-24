--SELECT * FROM fornecedores WHERE pais_de_origem = 'China';

--SELECT * FROM tabelaclientes; --WHERE status = 'Pendente';

--ALTER TABLE tabelaclientes ADD endereco_cliente varchar(250);


SELECT * FROM tabelaclientes;
SELECT * FROM tabelaprodutos WHERE preco_de_compra >= 400.00;
SELECT * FROM tabelapedidosgold;
SELECT * FROM tabelaclientes WHERE nome_cliente LIKE 'C%';
SELECT * FROM tabelapedidos WHERE total_do_pedido > 200;
SELECT * FROM tabelapedidos WHERE total_do_pedido >= 200;
SELECT * FROM tabelapedidos WHERE total_do_pedido < 200;
SELECT * FROM tabelapedidos WHERE total_do_pedido <= 200;
SELECT * FROM tabelapedidos WHERE total_do_pedido <> 200;
SELECT * FROM tabelaclientes WHERE nome_cliente > 'C';
SELECT * FROM tabelapedidos WHERE data_do_pedido > '2023-09-19';
SELECT * FROM tabelapedidos WHERE total_do_pedido >= 200 AND Status = ‘Pendente’;
SELECT * FROM tabelapedidos WHERE status = ‘Pendente’ OR status = ‘Processando’;
SELECT * FROM tabelapedidos WHERE NOT status = ‘Pendente’;
SELECT * FROM tabelapedidos WHERE data_de_envio_estimada BETWEEN ‘2023-08-01’ AND ‘2023-09-01’;
SELECT * FROM tabelaprodutos WHERE preco_de_compra BETWEEN 200 AND 600 ORDER BY nome_do_produto;
SELECT * FROM tabelaprodutos WHERE preco_de_compra BETWEEN 200 AND 600 ORDER BY data_de_inclusao;
SELECT * FROM tabelaprodutos WHERE preco_de_compra BETWEEN 200 AND 600 ORDER BY fornecedor DESC;
SELECT informacoes_de_contato AS email_cliente FROM tabelaclientes;

SELECT P.ID AS IDPedido, C.ID_cliente AS IDCliente,C.nome_cliente
FROM tabelapedidos AS P
JOIN tabelaclientes AS C ON P.ID = C.ID_cliente;
