-- Active: 1788435098023@@127.0.0.1@3306@smartcoffee_dml_otavio
-- Banco de dados - SmartCoffee - DML

-- Recurso de reset de banco de dados 
Drop database if exists SMARTCOFFEE_DML_OTAVIO;

Create database if not exists SMARTCOFFEE_DML_OTAVIO;
Use SMARTCOFFEE_DML_OTAVIO;

CREATE TABLE cliente (
    id_cliente INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(120) UNIQUE,
    telefone VARCHAR(15),
    cidade VARCHAR(60) NOT NULL,
    ativo BOOLEAN NOT NULL DEFAULT TRUE
);

CREATE TABLE categoria (
    id_categoria INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(60) NOT NULL UNIQUE
);

CREATE TABLE produto (
    id_produto INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    preco DECIMAL(10, 2) NOT NULL,
    ativo BOOLEAN NOT NULL DEFAULT TRUE,

    id_categoria INT NOT NULL,
    CONSTRAINT fk_produto_categoria FOREIGN KEY (id_categoria)
    REFERENCES categoria (id_categoria)
);
-- Organização e documentação
-- Constraint - denominar 

CREATE TABLE pedido (
    id_pedido INT PRIMARY KEY AUTO_INCREMENT,
    data_pedido DATETIME NOT NULL,
    status_pedido ENUM('ABERTO','PREPARANDO','FINALIZADO','CANCELADO') NOT NULL,
    valor_total DECIMAL(10 ,2) NOT NULL DEFAULT 0.00,

    id_cliente INT NOT NULL,
    CONSTRAINT fk_pedido_cliente FOREIGN KEY (id_cliente)
    REFERENCES cliente (id_cliente)
);

CREATE TABLE item_pedido (
    id_item INT PRIMARY KEY AUTO_INCREMENT,
    preco_unitario DECIMAL(10, 2) NOT NULL,
    observacao VARCHAR(150),
    quantidade INT NOT NULL,

    id_produto INT NOT NULL,
    CONSTRAINT fk_item_produto FOREIGN KEY (id_produto)
    REFERENCES produto (id_produto),
    id_pedido INT NOT NULL,
    CONSTRAINT fk_item_pedido FOREIGN KEY (id_pedido)
    REFERENCES pedido (id_pedido)
);

CREATE TABLE forma_pagamento (
    id_forma_pagamento INT PRIMARY KEY AUTO_INCREMENT,
    descricao VARCHAR(40) NOT NULL UNIQUE
);

CREATE TABLE pagamento (
    id_pagamento INT PRIMARY KEY AUTO_INCREMENT,
    valor DECIMAL(10, 2) NOT NULL,
    data_pagamento DATETIME,

    id_pedido INT NOT NULL,
    CONSTRAINT fk_pagamento_pedido FOREIGN KEY (id_pedido)
    REFERENCES pedido (id_pedido),

    id_forma_pagamento INT NOT NULL,
    CONSTRAINT fk_pagamento_forma_pagamento FOREIGN KEY (id_forma_pagamento)
    REFERENCES forma_pagamento (id_forma_pagamento)
);

-- INSERINDO DADOS NO BD
INSERT INTO cliente (nome, email, telefone, cidade, ativo) VALUES
('Luis Felipe','luis@email.com','1999999901','Limeira',TRUE),
('Maria Eduarda','maria@email.com','1999999902','Limeira',TRUE),
('Mateus Silva','mateus@email.com','1999999903','Limeira',TRUE),
('Matheus Oricolli','matheusc@email.com','1999999904','Limeira',TRUE),
('Nicolas Filipe','nicolas@email.com','1999999906','Limeira',TRUE),
('Otavio Correia','otavio@email.com','1999999905','Conchal',TRUE),
('Pedro Miranda','pedro@email.com','1999999907','Limeira',TRUE),
('Rafael Viera','rafael@email.com','1999999908','Limeira',TRUE),
('Rebecca','rebecca@email.com',NULL,'Limeira',TRUE),
('Rennan Campos','rennan@email.com','1999999909','Americana',TRUE),
('Samira Emily Dalosto','samira@email.com',NULL,'Ourinhos',FALSE),
('Sophia Carolina','sophia@email.com','1999999911','Taubaté',TRUE),
('Stefany Santana','stefany@email.com',NULL,'Campinas',TRUE),
('Vanessa Queiroz','vanessa@email.com','1999999912','Limeira',TRUE),
('Vinicius Henrique','vinicius@email.com','1999999913','Limeira',TRUE),
('Vanessa Oliveira','viniciuso@email.com','1999999914','Chicago',TRUE);

-- Vizualizar tabela 
SELECT * FROM cliente;

INSERT INTO categoria (nome) VALUES
('Café'),('Bebidas Quentes'),('Bebidas Geladas'),('Doces'),('Salgados'),('Combo');

SELECT * FROM categoria;

INSERT INTO produto (nome, preco, ativo, id_categoria) VALUES
('Café Espresso', 5.00, TRUE, 1),
('Cappuccino', 9.50, TRUE, 2),
('Suco de Laranja Natural', 9.00, TRUE, 3),
('Croissant de Nutella', 12.00, TRUE, 4),
('Pão de Queijo', 4.00, TRUE, 5),
('Combo Manhã (Espresso + Pão de Queijo)', 8.00, TRUE, 6);

SELECT * FROM produto;

INSERT INTO pedido (data_pedido, status_pedido, valor_total, id_cliente) VALUES
('2026-09-07 23:32:00', 'cancelado', 67.67, 4),
('2026-09-10 11:01:23', 'finalizado', 03.50, 9),
('2026-09-16 17:40:54', 'finalizado', 666, 11),
('2026-09-22 01:02:10', 'preparando', 43.99, 7),
(NOW(), 'aberto', 23.00, 14);

SELECT * FROM pedido;

INSERT INTO item_pedido (preco_unitario, observacao, quantidade, id_produto, id_pedido) VALUES
(5.00, 'Sem açúcar', 2, 1, 1),
(12.00, 'Bem assado', 1, 4, 1),
(9.50, 'Com canela em pó', 1, 2, 2),
(4.00, 'Quentinho', 2, 5, 2),
(8.00, 'Sem observação', 1, 6, 3),
(9.00, 'Gelo e adoçante', 1, 3, 4),
(4.00, 'Para viagem', 2, 5, 5);

SELECT * FROM item_pedido;

INSERT INTO forma_pagamento (descricao) VALUES
('Dinheiro'),
('Cartão de Crédito'),
('Cartão de Débito'),
('Pix'),
('Vale Refeição');

SELECT * FROM forma_pagamento;

INSERT INTO pagamento (valor, data_pagamento, id_pedido, id_forma_pagamento) VALUES
(67.67, '2026-09-07 23:35:00', 1, 4),
(3.50, '2026-09-10 11:05:00', 2, 1),
(666.00, '2026-09-16 17:45:00', 3, 2),
(43.99, '2026-09-22 01:05:00', 4, 3),
(23.00, NOW(), 5, 4);

SELECT * FROM pagamento;

-- EXEMPLO NOVO DE INSERÇÃO DE DADOS PORÉM COM RECUPERAÇÃO DO ÚLTIMO ID    

INSERT INTO pedido (data_pedido, status_pedido, valor_total, id_cliente) VALUES 
(NOW(), 'ABERTO','0.00',1);
SET @pedido = LAST_INSERT_ID();
SELECT @pedido

------------------------------------------------------------------------------------------

-- Atualizações e modificações de dados
UPDATE cliente 
SET telefone = '1999888801'
WHERE id_cliente = 11;

UPDATE produto
SET preco = 1.00;
-- NUNCA REALIIZAR UM UPDATE SEM --- WHERE 😤
 
UPDATE cliente
SET telefone = '1997777701',
cidade = 'Valinhos'
Where id_cliente = 11;

-- Ajuste de valor
UPDATE produto
SET preco = preco * 1.05
WHERE id_categoria = 1;

-- Ajuste de atualizações condicionais
UPDATE produto
SET preco = CASE
    WHEN preco < 10 THEN preco * 1.10
    ELSE preco * 1.05
END
WHERE ativo = TRUE;

------------------------------------------------------------------------------------------

-- APAGAR DADOS DO BD

-- Apagar um cliente específico
DELETE FROM cliente
WHERE id_cliente = 2;

-- Apagar todos os clientes inativos

DELETE FROM cliente 
WHERE ativo = FALSE;

-- Apagar todos os clientes de uma cidade específica
DELETE FROM cliente 
WHERE cidade = 'Chicago';

-- Exclusão lógica
UPDATE cliente 
SET ativo = FALSE
WHERE id_cliente = 10;


