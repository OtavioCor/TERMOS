Drop database if exists Atividade_DML_OTAVIO;

Use SMARTCOFFEE_DML_OTAVIO;

INSERT INTO cliente (nome, email, telefone, cidade, ativo) VALUES
('Bruno','bruno@email.com','1999888852','Piracicaba',TRUE),
('Celso','celso@email.com','1999888851','Limeira',TRUE);

INSERT INTO categoria (nome) VALUES
('Especiais da Casa')

INSERT INTO produto (nome, preco, ativo, id_categoria) VALUES
('Croissant da Casa', 35.00, TRUE, 7),
('Cookie Vulcão', 23.50, TRUE, 7),
('Torta de Limão com Café', 18.75, TRUE, 7);

INSERT INTO cliente (nome, email, telefone, cidade, ativo) VALUES
('José','jose@email.com',NULL,'Ourinhos',TRUE);

INSERT INTO pedido (data_pedido, status_pedido, valor_total, id_cliente) VALUES
(NOW(), 'aberto', 23.50, 18);

-- 6. Inserir pelo menos dois itens no último pedido criado usando LAST_INSERT_ID()
INSERT INTO item_pedido (preco_unitario, observacao, quantidade, id_produto, id_pedido) VALUES
(23.50, 'Quentinho', 1, 7, LAST_INSERT_ID()),
(18.75, 'Sem observação', 1, 8, LAST_INSERT_ID());