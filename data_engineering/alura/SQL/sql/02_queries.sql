-- SQL (Structe Querie Language) - Consultas em bancos relacionais, tabelas que se ligam de alguma forma
-- SGBD - Sistema Gerencial de Banco de dados, estamos usando o SQLite.
SELECT * FROM fornecedores WHERE pais_de_origem = 'China';

SELECT DISTINCT(cliente) FROM pedidos; --WHERE status = 'Pendente';
