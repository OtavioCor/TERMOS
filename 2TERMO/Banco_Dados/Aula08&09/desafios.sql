Drop database if exists Atividade_DML_OTAVIO;

-- ============================================================
-- AULA 08 - ATIVIDADE PRÁTICA DE DML
-- Nome: _______________________________________________
-- Turma: ______________________ Data: _________________
-- Base: smartcoffee_dml
-- ============================================================
Use SMARTCOFFEE_DML_OTAVIO;
-- IMPORTANTE:
-- Para toda questão de UPDATE ou DELETE, escreva primeiro um SELECT
-- com o mesmo WHERE para validar os registros afetados.

-- PARTE A - INSERT

-- 1. Cadastre dois novos clientes com dados diferentes.
INSERT INTO cliente (nome, email, telefone, cidade, ativo) VALUES
('Bruno','bruno@email.com','1999888852','Piracicaba',TRUE),
('Celso','celso@email.com','1999888851','Limeira',TRUE);

-- 2. Cadastre a categoria 'Especiais da Casa'.
INSERT INTO categoria (nome) VALUES
('Especiais da Casa')

-- 3. Localize o id da categoria criada e cadastre três produtos nela.
----------------ADICIONAIS DO PROF---------------
SELECT * FROM categoria;
SET @categoria_especial = (SELECT id_categoria FROM categoria WHERE nome = 'Especiais da Casa');
-- UTILIZAR O SET ANTES DA TAREFA AJUDA A ARMAZENAR O VALOR DA DEFINIÇÃO ATRIBUIDA E PODE SER UTILIZADA DEPOIS.   
INSERT INTO produto (nome, preco, ativo, id_categoria) VALUES
('Sorvete Fit', 8.00, TRUE, @categoria_especial);
-------------------------------------------------

INSERT INTO produto (nome, preco, ativo, id_categoria) VALUES
('Croissant da Casa', 35.00, TRUE, 7),
('Cookie Vulcão', 23.50, TRUE, 7),
('Torta de Limão com Café', 18.75, TRUE, 7);

-- 4. Cadastre um terceiro cliente sem telefone.
INSERT INTO cliente (nome, email, telefone, cidade, ativo) VALUES
('José','jose@email.com',NULL,'Ourinhos',TRUE);

-- 5. Crie um novo pedido para um dos clientes cadastrados.

----------------ADICIONAIS DO PROF---------------
SET @cliente_especial = (SELECT id_cliente FROM cliente WHERE email = 'jose@email.com');
-- UTILIZAR O SET ANTES DA TAREFA AJUDA A ARMAZENAR O VALOR DA DEFINIÇÃO ATRIBUIDA E PODE SER UTILIZADA DEPOIS.   
INSERT INTO pedido (data_pedido, status_pedido, valor_total, id_cliente) VALUES
(NOW(), 'ABERTO', 0.00, @cliente_especial);
SELECT * FROM pedido;
-------------------------------------------------

INSERT INTO pedido (data_pedido, status_pedido, valor_total, id_cliente) VALUES
(NOW(), 'ABERTO', 23.50, 18);

-- 6. Use LAST_INSERT_ID() para guardar o id do pedido em @pedido_atividade
--    e insira pelo menos dois itens nesse pedido.
SET @pedido_atividade = LAST_INSERT_ID();

INSERT INTO item_pedido (id_pedido, id_produto, quantidade, preco_unitario)
VALUES (@pedido_atividade, 4, 1, 13.00), (@pedido_atividade, 9, 2, 9.00);
SELECT * FROM item_pedido;

-- PARTE B - UPDATE

-- 7. Corrija o telefone de um dos clientes criados.
-- SELECT de validação:
-- UPDATE:
-- SELECT final:
----------------CORREÇÃO DO PROF---------------
UPDATE cliente
SET telefone = '112512345789'
WHERE id_cliente = 121
-- SELECT final:
SELECT * FROM cliente WHERE email = 'luana.a09@email.com';
---------------------------------------------------

SELECT * FROM cliente;
UPDATE cliente
SET telefone = '19999886767'
WHERE id_cliente = 17;


-- 8. Altere cidade e telefone de outro cliente em um único UPDATE.
UPDATE cliente
SET telefone = '19999884224',
cidade = 'Xique-Xique'
WHERE id_cliente = 18;

-- 9. Aumente em 8% o preço dos produtos da categoria 'Especiais da Casa'.
UPDATE produto
SET preco = preco * 1.08
WHERE id_categoria = 7;

SELECT* FROM produto;

-- 10. Altere o status do pedido criado para 'PREPARANDO'.
----------------CORREÇÃO DO PROF---------------
UPDATE pedido
SET status_pedido = 'PREPARANDO'
WHERE id_pedido = @pedido_atividade;
----------------------------------------------------
UPDATE pedido
SET status_pedido = 'PREPARANDO'
WHERE id_pedido = 5;

SELECT* FROM pedido;

-- 11. Atualize valor_total do pedido de acordo com os itens cadastrados.
--     Você pode calcular previamente com SELECT SUM(quantidade * preco_unitario).
-- PRIMEIRA VERSÃO 
SELECT SUM(quantidade*preco_unitario) AS total
FROM item_pedido
WHERE id_pedido = @pedido_atividade;
-- SEGUNDA VERSÃO
UPDATE pedido
SET valor_total = (SELECT SUM(quantidade*preco_unitario) FROM item_pedido WHERE id_pedido=@pedido_atividade)

-- 12. Escolha um dos produtos criados e faça uma exclusão lógica (ativo = FALSE).
-- Exclusão lógica - Permanece no banco mas tornando inativo
----------------CORREÇÃO DO PROF---------------
SELECT * FROM produto WHERE nome='Pão de Queijo';
UPDATE produto SET ativo=FALSE WHERE nome='Pão de Queijo';
SELECT * FROM produto WHERE nome='Pão de Queijo';
-----------------------------------------------
SELECT* FROM produto;
UPDATE produto
SET ativo = FALSE
WHERE id_produto = 3;

-- PARTE C - DELETE

-- 13. Crie um cliente de teste sem pedidos.
--     Depois localize e exclua apenas esse cliente.
----------------CORREÇÃO DO PROF---------------
INSERT INTO cliente (nome,email,cidade)
VALUES ('Cliente Temporário','temporario.a09@email.com','Limeira');

SELECT * FROM cliente WHERE email='temporario.a09@email.com';

DELETE FROM cliente WHERE email='temporario.a09@email.com';

SELECT * FROM cliente WHERE email='temporario.a09@email.com';
-----------------------------------------------
INSERT INTO cliente (nome, email, telefone, cidade, ativo) VALUES
('Paulo','paulo@email.com','1999254765','Limeira',TRUE);
DELETE FROM cliente
WHERE id_cliente = 20;
SELECT* FROM cliente;


-- 14. Tente excluir um cliente da base original que possua pedidos.
--     Deixe o DELETE comentado após o teste e descreva o erro abaixo.
-- Resultado observado:
----------------CORREÇÃO DO PROF---------------
DELETE FROM cliente
WHERE id_cliente = @cliente_atividade;
-----------------------------------------------
DELETE FROM cliente
WHERE id_cliente = 7;
-- Resultado apresentado: Cannot delect or update a parent row

SELECT * FROM pedido;

-- 15. Explique em comentário por que a FK bloqueou a exclusão.
-- Resposta:
-- CORREÇÂO DO PROFESSOR
-- Pois possui dependencias em outra tabela e possui dados com informações
--------------------------------------------------------------

-- O FK bloqueou a exclusão por causa que está armazenada informações daquele cliente na tabela pedido, caso apague o cliente não irá ter o registro do cliente do pedido que relaciona com aquele id  

-- 16. Crie uma categoria temporária chamada 'Excluir Depois' e remova-a.
INSERT INTO categoria (nome) VALUES
('Excluir Depois');

DELETE FROM categoria
WHERE id_categoria = 8;

SELECT * FROM categoria;

-- PARTE D - INTEGRIDADE E ERROS CONTROLADOS
-- Execute uma tentativa por vez. Depois deixe o comando problemático comentado.

-- 17. Tente inserir um produto com id_categoria = 9999.
-- Qual restrição impediu a operação?
INSERT INTO produto (nome, preco, ativo, id_categoria) VALUES
('Cupcake', 9.00, TRUE, 9999);
-- Restrição - Cannot add or update a child row

-- 18. Tente cadastrar um cliente usando 'ana@email.com'.
-- Qual restrição impediu a operação?
INSERT INTO cliente (nome, email, telefone, cidade, ativo) VALUES
('Ana Julia','ana@email.com','19952982441','Limeira',TRUE);
-- Restrição - Não permite email duplicado

-- 19. Tente criar um pedido com id_cliente = 9999.
-- Qual restrição impediu a operação?
INSERT INTO pedido (data_pedido, status_pedido, valor_total, id_cliente) VALUES
('2026-09-05 23:32:00', 'cancelado', 67.67, 9999);
-- Restrição - Cannot add or update a child row

-- 20. Escreva em comentários a diferença entre os três erros anteriores.
-- Os exercícios 17 e 19 falharam devido a restrições da FK, pois tentaram usar de referencia IDs que não existem.
-- O exercício 18 falhou devido a uma restrição do UK, pois tentou cadastrar um e-mail que já existia na tabela.

-- PARTE E - DESAFIO COMPLETO COM TRANSAÇÃO

-- 21. Inicie uma transação.


-- 22. Dentro dela, cadastre um cliente, um pedido e dois itens relacionados.


-- 23. Faça uma consulta com JOIN comprovando que os registros existem
--     enquanto a transação está aberta.


-- 24. Execute ROLLBACK e depois use SELECT para provar que o cadastro foi desfeito.


-- 25. Repita o processo com novos dados e finalize usando COMMIT.
--     Depois consulte os registros persistidos.


-- DESAFIO EXTRA
-- 26. Escolha uma situação realista do SmartCoffee que exija INSERT + UPDATE
--     ou UPDATE + DELETE lógico. Descreva a regra de negócio e implemente.