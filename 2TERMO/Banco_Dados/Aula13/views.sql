-- Views ou Visões - Transformar determinadas consultas em visões reutilizáveis
-- Como posso disponibilizar uma consulta como se ela fosse uma tabela
-- Resposta: Views

USE smartcoffee_dml_otavio;

-- Ex 1: View - Como consultar uma visão lógica
CREATE VIEW vw_produtos_ativos AS SELECT id_produto, nome, preco 
FROM produto
WHERE ativo = TRUE;

-- VIZUALIZAR A CONSULTA CRIADA ATRAVÉS DA VIEW
SELECT * FROM vw_produtos_ativos;

-- OBS: A View guarda a definição da consulta. Em uma view comum os dados continuam pertencendo as tabelas de origem.

-- Tabela - Armazena registros
-- View - Representa o resultado lógico da consulta

-- Por que utilizar?
-- Para simplificar a consulta
-- Reutilizar lógica onde a consulta ganha um nome
-- Padronização de relatórios 
-- Restrição de exposição da lógica

-- EX 1:
-- Uma consulta original ou inicial:

SELECT id_produto, nome, preco
FROM produto
WHERE ativo = TRUE;

-- TRANSFORMAR EM UMA VIEW
CREATE VIEW vw_produtos_ativos AS SELECT id_produto, nome, preco 
FROM produto
WHERE ativo = TRUE;

-- COMO UTILIZAR:
SELECT * FROM vw_produtos_ativos;

-- EX 2: UTILIZAR FILTROS NAS VIEWS
SELECT id_produto, nome, preco
FROM produto
WHERE preco >= 10.00
ORDER BY preco DESC;

SELECT * FROM vw_produtos_ativos
WHERE preco >= 10.00
ORDER BY preco DESC;

-- OBS: View não elimina a possibilidade de usar WHERE, ORDER BY e outras cláusulas

-- EX 3: VIEW COM JOINS - MOSTRAR PRODUTOS E CATEGORIAS
-- Consulta original
SELECT p.id_produto, p.nome AS produto, ca.nome AS categoria, p.preco
FROM produto AS p
INNER JOIN categoria AS ca
ON ca.id_categoria = p.id_categoria;

-- Criando em View
CREATE VIEW vm_produtos_categorias AS 
SELECT p.id_produto, p.nome AS produto, ca.nome AS categoria, p.preco
FROM produto AS p
INNER JOIN categoria AS ca
ON ca.id_categoria = p.id_categoria;

-- Resultando visual por view
SELECT * FROM vm_produtos_categorias
ORDER BY categoria, produto;

-- EX 4: VIEW com várias tabelas - Relatório de pedidos
CREATE VIEW vm_pedidos_clientes AS 
SELECT p.id_pedido, p.data_pedido, p.status_pedido, c.id_cliente, c.nome AS cliente, pr.id_produto, pr.nome AS Produto
FROM pedido AS p
INNER JOIN cliente AS c
ON c.id_cliente = p.id_cliente
INNER JOIN produto AS pr
ON p.id_pedido = pr.id_produto;

-- RESULTADO
SELECT * FROM vm_pedidos_clientes
WHERE status_pedido = 'ABERTO';

-- EX 5: VIEW para um relatório completo
CREATE VIEW vw_itens_pedidos AS
SELECT pe.id_pedido, pe.data_pedido, c.nome AS Cliente, pr.nome AS Produto, ip.quantidade, ip.preco_unitario, ip.quantidade * ip.preco_unitario AS Subtotal
FROM pedido AS pe
INNER JOIN cliente AS c
ON c.id_cliente = pe.id_cliente
INNER JOIN item_pedido AS ip
ON ip.id_pedido = pe.id_pedido
INNER JOIN produto AS pr
ON pr.id_produto = ip.id_produto;

-- Resultado
SELECT * FROM vw_itens_pedidos
WHERE id_pedido = 1;

-- EX 6: VIEW COM FUNÇÕES DE AGREGAÇÃO 
CREATE VIEW vw_vendas_por_produto AS
SELECT pr.id_produto, pr.nome AS produto, SUM(ip.quantidade) AS Unidades_Vendidas, SUM(ip.quantidade * ip.preco_unitario) AS Faturamento
FROM produto AS pr
INNER JOIN item_pedido AS ip
ON ip.id_produto = pr.id_produto
INNER JOIN pedido AS pe
ON pe.id_pedido = ip.id_pedido
WHERE pe.status_pedido = 'FINALIZADO'
GROUP BY pr.id_produto, pr.nome;

-- Resultado: Consulta gerencial
SELECT * FROM vw_vendas_por_produto
ORDER BY Faturamento DESC;

-- EX 7: VIEW com LEFT JOIN - Apresenta quem nunca realizou pedidos
CREATE VIEW vw_clientes_resumo AS
SELECT c.id_cliente, c.nome AS cliente, COUNT(p.id_pedido) AS Quantidade_Pedidos
FROM cliente AS c
LEFT JOIN pedido AS p
ON p.id_cliente = c.id_cliente
GROUP BY c.id_cliente, c.nome;

-- RESULTADO
SELECT * FROM vw_clientes_resumo
WHERE Quantidade_Pedidos = 0;

-- EX 8: NOMEANDO VIEWS 
-- ALIASES TORNAM AS VIEWS MAIS CLARAS -- AS

CREATE VIEW vw_precos_produtos AS
SELECT id_produto, nome AS Produto, preco AS preco_atual
FROM produto;

SELECT * FROM vw_precos_produtos;

-- EX 9: VISUALIZAR AS VIEWS EXISTENTES
-- VISUALIZAR O RESULTADO DE TODAS AS VIEWS CRIADAS
SHOW FULL TABLES WHERE TABLE_TYPE = 'VIEW';

-- PODEMOS CONSULTAR O CATÁLOGO
-- QUER DIZER TODO O BD MYSQL
SELECT TABLE_NAME FROM information_schema.VIEWS
WHERE TABLE_SCHEMA = DATABASE();

-- EX 10: VISUALIZANDO DEFINIÇÕES
SHOW CREATE VIEW vm_produtos_categorias;

-- EX 11: CREATE OR REPLACE VIEW
CREATE OR REPLACE VIEW vw_produto_ativos AS
SELECT id_produto, nome, preco, id_categoria
FROM produto
WHERE ativo = TRUE;
-- OBS: Irá substituir ou alterar uma view já criada com suas informações

-- EX 12: VIEW ATUALIZÁVEL
CREATE VIEW vw_clientes_ativos AS
SELECT id_cliente, nome, email, ativo
FROM cliente
WHERE ativo = TRUE;

-- Atualizar a tabela Cliente
UPDATE vw_clientes_ativos
SET nome = 'Ana Francis'
WHERE id_cliente = 2;

-- EX 13: VIEW NÃO ATUALIZÁVEL
UPDATE vw_vendas_por_produto
SET Faturamento = 1000
WHERE id_produto = 1;

-- OBS: O campo é calculado. Simplemente não possível receber 1000.

-- EX 14: WITH CHECK OPTION - VIEW QUE MOSTRA APENAS PRODUTOS ATIVOS
CREATE OR REPLACE VIEW vw_produtos_ativos AS
SELECT id_produto, nome, preco, ativo, id_categoria
FROM produto
WHERE ativo = TRUE
WITH CHECK OPTION;

SELECT * FROM vw_produtos_ativos

-- OBS: O With Check Option ajuda a impedir alterações realizadas pela view que fariam o registro.
-- Verificar se tudo o que eu pedi para ele está OK, se estiver ele confirma

-- EX 15: PADRÃO DEFINIÇÃO DE NOMENCLATURA
-- vw - views
-- nome - complementar a tabela ou consultar que deseja realizar
-- vw_nome_desejo
-- vw_nome_da_finalidade
-- vw_produtos_ativos

-- APAGAR VIEWS
DROP VIEW vm_pedidos_clientes;
