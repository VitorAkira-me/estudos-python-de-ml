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

--CREATE TABLE IF NOT EXISTS tabelapedidos (
--    id INTEGER,
--    data_do_pedido DATE,
--    status TEXT,
--    total_do_pedido INTEGER,
--    cliente INTEGER,
--    data_de_envio_estimada DATE
--);


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

--INSERT INTO tabelaclientes (
--    id_cliente,
--    nome_cliente,
--    informacoes_de_contato,
--    endereco_cliente
--) VALUES (
--    '1',
--    'Ana Silva',
--    'ana.silva@email.com',
--    'Rua Flores - casa 1'
--);


--INSERT INTO tabelaclientes (id_cliente,nome_cliente,informacoes_de_contato,endereco_cliente) 
--VALUES ('2','João Santos','joao.santos@provedor.com','Rua do Pinheiros, 25'),
--('3','Maria Fernandes','maria.fernandes@email.com','Rua Santo Antonio, 57'),
--('4','Carlos Pereira','carlos.pereira@email.com','Avenida Rio, 96');

--INSERT INTO Tabelaclientes (id_cliente,nome_cliente,informacoes_de_contato,endereco_cliente)
--VALUES (5, 'Patrícia Lima', 'patricia.lima@email.com', 'Rua das Flores, 123'), 
--(6, 'Rodrigo Almeida', 'rodrigo.almeida@email.com', 'Avenida Central, 456'),
--(7, 'André Oliveira', 'andre.oliveira@email.com', 'Travessa do Sol, 789'),
--(8, 'Isabela Rodrigues', 'isabela.rodrigues@email.com', 'Rua da Paz, 321'),
--(9, 'Ricardo Sousa', 'ricardo.sousa@email.com', 'Alameda dos Sonhos, 654'),
--(10, 'Luana Gomes', 'luana.gomes@email.com', 'Praceta das Estrelas, 987'),
--(11, 'Juliano Costa', 'juliano.costa@email.com', 'Av. Principal, 234'),
--(12, 'Sandra Ferreira', 'sandra.ferreira@email.com', 'Rua da Liberdade, 567'),
--(13, 'Roberto Barbosa', 'roberto.barbosa@email.com', 'Rua da Esquina, 432'),
--(14, 'Alice Santos', 'alice.santos@email.com', 'Largo da Amizade, 765'),
--(15, 'Gustavo Lima', 'gustavo.lima@email.com', 'Avenida das Árvores, 876'),
--(16, 'Carla Silva', 'carla.silva@email.com', 'Travessa das Aves, 345'),
--(17, 'Daniel Oliveira', 'daniel.oliveira@email.com', 'Alameda dos Bosques, 678'),
--(18, 'Luciana Almeida', 'luciana.almeida@email.com', 'Rua das Colinas, 123'),
--(19, 'Fernando Pereira', 'fernando.pereira@email.com', 'Avenida das Ondas, 987'),
--(20, 'Marina Lima', 'marina.lima@email.com', 'Praceta dos Girassóis, 456'),
--(21, 'Lucas Rodrigues', 'lucas.rodrigues@email.com', 'Rua das Montanhas, 321'),
--(22, 'Adriana Sousa', 'adriana.sousa@email.com', 'Travessa dos Rios, 654'),
--(23, 'Eduardo Gomes', 'eduardo.gomes@email.com', 'Avenida das Pedras, 789'),
--(24, 'Marcia Costa', 'marcia.costa@email.com', 'Largo das Praias, 234'),
--(25, 'José Silva', 'jose.silva@email.com', 'Av. dos Ventos, 432'),
--(26, 'Beatriz Alves', 'beatriz.alves@email.com', 'Rua dos Coqueiros, 765'),
--(27, 'André Santos', 'andre.santos@email.com', 'Avenida dos Lagos, 876'),
--(28, 'Carolina Lima', 'carolina.lima@email.com', 'Travessa das Neves, 345'),
--(29, 'Fábio Rodrigues', 'fabio.rodrigues@email.com', 'Alameda dos Campos, 678'),
--(30, 'Larissa Pereira', 'larissa.pereira@email.com', 'Rua dos Bosques, 123');


--INSERT INTO tabelaprodutos (id_produto, nome_do_produto, descricao, categoria, preco_de_compra, unidade, fornecedor, data_de_inclusao)
--VALUES (1, 'Smartphone X', 'Smartphone de última geração', 1, 699.99, 'Unidade', 1, '2023-08-01'),
--(2, 'Notebook Pro', 'Notebook poderoso com tela HD', 2, 1199.99, 'Unidade', 2, '2023-08-02'),
--(3, 'Tablet Lite', 'Tablet compacto e leve', 3, 299.99, 'Unidade', 3, '2023-08-03'),
--(4, 'TV LED 55"', 'TV LED Full HD de 55 polegadas', 4, 599.99, 'Unidade', 4, '2023-08-04'),
--(5, 'Câmera DSLR', 'Câmera digital DSLR com lente intercambiável', 5, 699.99, 'Unidade', 5, '2023-08-05'),
--(6, 'Impressora Laser', 'Impressora laser de alta qualidade', 6, 349.99, 'Unidade', 6, '2023-08-06'),
--(7, 'Mouse Óptico', 'Mouse óptico sem fio', 7, 19.99, 'Unidade', 7, '2023-08-07'),
--(8, 'Teclado sem Fio', 'Teclado sem fio ergonômico', 8, 39.99, 'Unidade', 8, '2023-08-08'),
--(9, 'Headphones Estéreo', 'Headphones estéreo com cancelamento de ruído', 9, 149.99, 'Unidade', 9, '2023-08-09'),
--(10, 'Smartwatch', 'Smartwatch com monitor de frequência cardíaca', 10, 199.99, 'Unidade', 10, '2023-08-10'),
--(11, 'Monitor 24"', 'Monitor LED Full HD de 24 polegadas', 11, 149.99, 'Unidade', 11, '2023-08-11'),
--(12, 'HD Externo 1TB', 'HD Externo portátil de 1TB', 12, 79.99, 'Unidade', 12, '2023-08-12'),
--(13, 'Drone DJI', 'Drone DJI com câmera 4K', 13, 799.99, 'Unidade', 13, '2023-08-13'),
--(14, 'Console de Jogos', 'Console de jogos de última geração', 14, 299.99, 'Unidade', 14, '2023-08-14'),
--(15, 'Fones de Ouvido Bluetooth', 'Fones de ouvido Bluetooth com estojo de carregamento', 15, 59.99, 'Unidade', 15, '2023-08-15'),
--(16, 'Projetor HD', 'Projetor HD de alta definição', 16, 499.99, 'Unidade', 16, '2023-08-16'),
--(17, 'Impressora Multifuncional', 'Impressora multifuncional com scanner', 6, 249.99, 'Unidade', 6, '2023-08-17'),
--(18, 'Notebook Ultrafino', 'Notebook ultrafino com SSD rápido', 2, 999.99, 'Unidade', 2, '2023-08-18'),
--(19, 'Mouse Gamer', 'Mouse gamer com iluminação RGB', 7, 49.99, 'Unidade', 7, '2023-08-19'),
--(20, 'Câmera de Ação', 'Câmera de ação à prova d''água', 5, 129.99, 'Unidade', 5, '2023-08-20'),
--(21, 'Tablet Profissional', 'Tablet profissional para designers', 3, 499.99, 'Unidade', 3, '2023-08-21'),
--(22, 'Monitor Curvo', 'Monitor LED curvo de 32 polegadas', 11, 299.99, 'Unidade', 11, '2023-08-22'),
--(23, 'Teclado Mecânico', 'Teclado mecânico para jogos', 8, 89.99, 'Unidade', 8, '2023-08-23'),
--(24, 'Console Portátil', 'Console de jogos portátil', 14, 199.99, 'Unidade', 14, '2023-08-24'),
--(25, 'HD Externo 2TB', 'HD Externo portátil de 2TB', 12, 109.99, 'Unidade', 12, '2023-08-25'),
--(26, 'Kit de Caixas de Som', 'Kit de caixas de som estéreo', 17, 29.99, 'Unidade', 17, '2023-08-26'),
--(27, 'Câmera de Segurança', 'Câmera de segurança com visão noturna', 18, 79.99, 'Unidade', 18, '2023-08-27'),
--(28, 'Projetor Mini', 'Projetor mini portátil', 16, 199.99, 'Unidade', 16, '2023-08-28'),
--(29, 'Impressora a Jato de Tinta', 'Impressora a jato de tinta colorida', 6, 89.99, 'Unidade', 6, '2023-08-29'),
--(30, 'Servidor de Rede', 'Servidor de rede empresarial', 19, 799.99, 'Unidade', 19, '2023-08-30'),
--(31, 'Smartphone Y', 'Smartphone de última geração', 1, 699.99, 'Unidade', 1, '2022-08-01'),
--(32, 'Notebook Avançado', 'Notebook poderoso com tela Full HD', 2, 1299.99, 'Unidade', 2, '2022-08-02'),
--(33, 'Tablet Pro', 'Tablet profissional com caneta stylus', 3, 399.99, 'Unidade', 3, '2022-08-03'),
--(34, 'TV OLED 65"', 'TV OLED 4K de 65 polegadas', 4, 899.99, 'Unidade', 4, '2022-08-04'),
--(35, 'Câmera Mirrorless', 'Câmera digital mirrorless de alta qualidade', 5, 799.99, 'Unidade', 5, '2022-08-05'),
--(36, 'Impressora Jato de Tinta', 'Impressora jato de tinta colorida', 6, 299.99, 'Unidade', 6, '2022-08-06'),
--(37, 'Mouse Bluetooth', 'Mouse Bluetooth ergonômico', 7, 29.99, 'Unidade', 7, '2022-08-07'),
--(38, 'Teclado Mecânico RGB', 'Teclado mecânico RGB para gamers', 8, 59.99, 'Unidade', 8, '2022-08-08'),
--(39, 'Fones de Ouvido Sem Fio', 'Fones de ouvido sem fio com cancelamento de ruído', 9, 169.99, 'Unidade', 9, '2022-08-09'),
--(40, 'Smartwatch Pro', 'Smartwatch com GPS e monitor de saúde', 10, 249.99, 'Unidade', 10, '2022-08-10'),
--(41, 'Monitor 27"', 'Monitor LED Quad HD de 27 polegadas', 11, 199.99, 'Unidade', 11, '2022-08-11'),
--(42, 'HD Externo 4TB', 'HD Externo portátil de 4TB', 12, 129.99, 'Unidade', 12, '2022-08-12'),
--(43, 'Drone DJI Pro', 'Drone DJI com câmera 8K', 13, 1199.99, 'Unidade', 13, '2022-08-13'),
--(44, 'Console de Jogos Elite', 'Console de jogos de elite com VR', 14, 599.99, 'Unidade', 14, '2022-08-14'),
--(45, 'Fones de Ouvido com Cancelamento de Ruído', 'Fones de ouvido com cancelamento de ruído ativo', 15, 89.99, 'Unidade', 15, '2022-08-15'),
--(46, 'Projetor 4K', 'Projetor 4K de alta definição', 16, 799.99, 'Unidade', 16, '2022-08-16'),
--(47, 'Impressora Laser Colorida', 'Impressora laser colorida de alta qualidade', 6, 349.99, 'Unidade', 6, '2022-08-17'),
--(48, 'Notebook Ultrafino SSD', 'Notebook ultrafino com SSD rápido', 2, 1099.99, 'Unidade', 2, '2022-08-18'),
--(49, 'Mouse Gamer RGB', 'Mouse gamer com iluminação RGB personalizável', 7, 69.99, 'Unidade', 7, '2022-08-19'),
--(50, 'Câmera de Ação Pro', 'Câmera de ação 4K à prova dágua', 5, 149.99, 'Unidade', 5, '2022-08-20'),
--(51, 'Tablet Profissional', 'Tablet profissional para designers e artistas', 3, 449.99, 'Unidade', 3, '2021-08-21'),
--(52, 'Monitor Curvo 34"', 'Monitor LED curvo ultra-amplo de 34 polegadas', 11, 399.99, 'Unidade', 11, '2021-08-22'),
--(53, 'Teclado Mecânico Retroiluminado', 'Teclado mecânico com retroiluminação', 8, 79.99, 'Unidade', 8, '2021-08-23'),
--(54, 'Console Portátil Clássico', 'Console portátil com jogos clássicos', 14, 149.99, 'Unidade', 14, '2021-08-24'),
--(55, 'HD Externo 5TB', 'HD Externo portátil de 5TB', 12, 149.99, 'Unidade', 12, '2021-08-25'),
--(56, 'Kit de Caixas de Som Bluetooth', 'Kit de caixas de som Bluetooth estéreo', 17, 49.99, 'Unidade', 17, '2021-08-26'),
--(57, 'Câmera de Segurança HD', 'Câmera de segurança HD com gravação em nuvem', 18, 99.99, 'Unidade', 18, '2021-08-27'),
--(58, 'Projetor Portátil', 'Projetor portátil de alta qualidade', 16, 249.99, 'Unidade', 16, '2021-08-28'),
--(59, 'Impressora a Laser Monocromática', 'Impressora a laser monocromática de alta velocidade', 6, 169.99, 'Unidade', 6, '2021-08-29'),
--(60, 'Servidor de Rede Empresarial', 'Servidor de rede empresarial com suporte 24/7', 19, 1999.99, 'Unidade', 19, '2021-08-30');


CREATE TABLE tabelapedidosgold (
ID_pedido_gold INT PRIMARY KEY,
Data_Do_Pedido_gold DATE,
Status_gold VARCHAR(50),
Total_Do_Pedido_gold DECIMAL(10, 2),
Cliente_gold INT,
Data_De_Envio_Estimada_gold DATE,
FOREIGN KEY (cliente_gold) REFERENCES tabelaclientes(id_cliente)
);


INSERT INTO tabelapedidosgold (
    ID_pedido_gold, 
    Data_Do_Pedido_gold, 
    Status_gold, 
    Total_Do_Pedido_gold, 
    Cliente_gold, 
    Data_De_Envio_Estimada_gold)
SELECT id, 
data_do_pedido, 
status, 
total_do_pedido, 
cliente, 
data_de_envio_estimada 
FROM tabelapedidos WHERE total_do_pedido >= 400.00;


INSERT INTO tabelapedidos (id, 
data_do_pedido, 
status, 
total_do_pedido, 
cliente, 
data_de_envio_estimada)
VALUES (1,2023-08-01,'Pendente',150.00,5,2023-08-10), 
(2,2023-08-02,'Processando',280.50,8,2023-08-15),
(3,2023-08-03,'Enviado',450.75,12,2023-08-12),
(4,2023-08-04,'Entregue',90.25,2,2023-08-05),
(5,2023-08-05,'Processando',520.00,17,2023-08-20),
(6,2023-08-06,'Pendente',200.00,6,2023-08-09),
(7,2023-08-07,'Processando',380.90,9,2023-08-18),
(8,2023-08-08,'Enviado',600.25,14,2023-08-11),
(9,2023-08-09,'Entregue',120.50,4,2023-08-14),
(10,2023-08-10,'Processando',420.75,10,2023-08-16),
(11,2023-08-11,'Pendente',180.00,1,2023-08-22),
(12,2023-08-12,'Enviado',320.25,7,2023-08-19),
(13,2023-08-13,'Pendente',90.75,3,2023-08-07),
(14,2023-08-14,'Entregue',420.50,11,2023-08-25),
(15,2023-08-15,'Processando',300.00,13,2023-08-17),
(16,2023-08-16,'Enviado',510.25,16,2023-08-21),
(17,2023-08-17,'Pendente',75.00,15,2023-08-08),
(18,2023-08-18,'Processando',420.90,18,2023-08-13),
(19,2023-08-19,'Enviado',720.25,20,2023-08-23),
(20,2023-08-20,'Entregue',140.50,19,2023-08-06),
(21,2023-08-21,'Processando',380.75,22,2023-08-28),
(22,2023-08-22,'Pendente',250.00,21,2023-08-30),
(23,2023-08-23,'Enviado',530.25,23,2023-08-29),
(24,2023-08-24,'Entregue',110.90,25,2023-08-31),
(25,2023-08-25,'Processando',360.75,24,2023-08-27),
(26,2023-08-26,'Pendente',190.50,26,2023-09-03),
(27,2023-08-27,'Enviado',620.00,29,2023-09-01),
(28,2023-08-28,'Entregue',85.25,30,2023-09-02),
(29,2023-08-29,'Processando',480.75,28,2023-09-05),
(30,2023-08-30,'Pendente',210.50,27,2023-09-04),
(31,2023-08-31,'Enviado',550.00,31,2023-09-07),
(32,2023-09-01,'Entregue',125.25,34,2023-09-08),
(33,2023-09-02,'Processando',360.75,33,2023-09-06),
(34,2023-09-03,'Pendente',160.50,32,2023-09-10),
(35,2023-09-04,'Enviado',690.00,35,2023-09-09),
(36,2023-09-05,'Entregue',105.25,37,2023-09-12),
(37,2023-09-06,'Processando',400.75,36,2023-09-11),
(38,2023-09-07,'Pendente',180.50,38,2023-09-14),
(39,2023-09-08,'Enviado',590.00,39,2023-09-13),
(40,2023-09-09,'Entregue',95.25,41,2023-09-16),
(41,2023-09-10,'Processando',380.75,40,2023-09-15),
(42,2023-09-11,'Pendente',250.50,42,2023-09-19),
(43,2023-09-12,'Enviado',560.00,45,2023-09-18),
(44,2023-09-13,'Entregue',110.25,47,2023-09-21),
(45,2023-09-14,'Processando',410.75,44,2023-09-20),
(46,2023-09-15,'Pendente',175.50,43,2023-09-23),
(47,2023-09-16,'Enviado',750.00,49,2023-09-22),
(48,2023-09-17,'Entregue',130.25,50,2023-09-25),
(49,2023-09-18,'Processando',390.75,48,2023-09-24),
(50,2023-09-19,'Pendente',200.50,46,2023-09-27),
(51,2023-09-20,'Processando',420.00,1,2023-09-25),
(52,2023-09-21,'Enviado',180.75,5,2023-09-28),
(53,2023-09-22,'Processando',280.50,1,2023-09-27),
(54,2023-09-23,'Enviado',150.25,2,2023-09-30),
(55,2023-09-24,'Pendente',520.00,3,2023-10-05),
(56,2023-09-25,'Processando',320.00,1,2023-09-29),
(57,2023-09-26,'Enviado',75.50,4,2023-10-02),
(58,2023-09-27,'Pendente',420.75,5,2023-10-06),
(59,2023-09-28,'Processando',250.00,2,2023-10-04),
(60,2023-09-29,'Enviado',110.25,1,2023-10-03),
(61,2023-10-01,'Pendente',300.00,6,2023-10-10),
(62,2023-10-02,'Processando',420.50,3,2023-10-12),
(63,2023-10-03,'Enviado',180.25,1,2023-10-15),
(64,2023-10-04,'Pendente',520.00,4,2023-10-14),
(65,2023-10-05,'Processando',250.75,5,2023-10-11),
(66,2023-10-06,'Enviado',90.50,2,2023-10-13),
(67,2023-10-07,'Processando',420.00,1,2023-10-16),
(68,2023-10-08,'Enviado',220.25,7,2023-10-18),
(69,2023-10-09,'Pendente',360.75,4,2023-10-17),
(70,2023-10-10,'Processando',150.00,3,2023-10-19);



