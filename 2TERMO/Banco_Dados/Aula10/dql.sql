-- Active: 1788435098023@@127.0.0.1@3306@smartcoffee_dml_otavio

-- DQL - DATA QUERY LANGUEGE (LINGUAGEM DE CONSULTA DE DADOS)

-- Antes de Inciar  

Insert into cliente(nome, email, telefone, cidade, ativo) VALUES
('Ana Flavia','anaf@gmail.com','19998451456','Campinas',TRUE);

-- EX 1: SELECT Simples ou Consulta Simples
-- Estrutura SELECT como exemplo
SELECT coluna
from tabela;

-- Consultar todas as colunas
SELECT * 
FROM cliente;

-- Consultar colunas especificas
SELECT nome, telefone
FROM cliente;

-- EX 2: AS como apelido ou nome para colunas
SELECT nome AS Nome_Cliente
FROM cliente;

SELECT email AS Email_Cliente, telefone AS Contato_CLiente
FROM cliente;

-- EX 3: DISTINCT - Eliminando Repetições
SELECT DISTINCT cidade
FROM cliente;

SELECT cidade
FROM cliente;
-- Sem o DISTINCT o resultado irá se repetir mais vezes
-- Com o DISTINCT o resultado irá aparecer uma vez

-- EX 4: WHERE - Filtro por Registros
-- = IGUAL
-- <> ou ! = DIFERENTE
-- > MAIOR QUE
-- >= MAIOR IGUAL
-- < MENOR QUE
-- <= MENOR IGUAL

-- Consulta para valores acima de 10.00 reais
SELECT nome, preco
From produto
WHERE preco > 10.00;

-- Consulta Status de clientes se está ativo ou inativo
SELECT nome AS Produto, preco AS Valor, ativo AS Status
FROM produto
WHERE ativo = TRUE;

-- Consulta pedidos acima de determinado valor
SELECT id_pedido, data_pedido, valor_total
FROM pedido
WHERE valor_total >= 25.00;

-- EX 5: Uso do AND, OR e NOT

-- AND todas as condições verdadeiras
SELECT nome, preco
FROM produto
WHERE preco >= 8.00 AND preco <= 25.00;

-- OR pelo menos uma condição verdadeira
SELECT nome, cidade
FROM cliente
WHERE cidade = 'Limeira' OR cidade = 'Piracicaba';

-- NOT não irá buscar ou consultar o valor desejado
SELECT nome, cidade
FROM cliente
WHERE NOT cidade = 'Limeira';

-- EXTRA - Utilizando AND e OR juntos separar por ()
SELECT nome, cidade, ativo
FROM cliente
WHERE ativo = TRUE
AND (cidade = 'Limeira' OR cidade = 'Piracicaba');

-- EX 6: BETWEEN - Entre dois valores
-- Limite inicial e final

-- Consulta por valores entre 8 e 15
SELECT nome, preco
FROM produto
WHERE preco BETWEEN 8.00 and 15.00;

-- Consulta por intervalo de datas
SELECT id_pedido, data_pedido, valor_total
FROM pedido
WHERE data_pedido BETWEEN '2026-09-01 00:00:00' AND '2026-09-23 23:59:59';

-- EX 7: IN várias possibilidades

-- Consulta com várias condições e diminuindo o uso de OR
SELECT nome, cidade
FROM cliente
WHERE cidade IN ('Limeira','Campinas','Americana','Piracicaba');

-- Consulta com excessão dos valores especificados
SELECT nome, cidade
FROM cliente
WHERE cidade NOT IN ('Limeira','Piracicaba');

-- EX 8: LIKE - Pesquisar por textos
-- Coringas
-- % Vários caracteres
-- _ Exatamente um caracter

-- Consulta todos os produtos que começam com a palavra desejada
SELECT nome
FROM produto
WHERE nome LIKE 'Café%';

-- Consulta todos os produtos que possuam a palavra desejada
SELECT nome 
FROM produto
WHERE nome LIKE '%chocolate%';

-- Consulta todos os clientes que terminam com a palavra desejada
SELECT nome
FROM cliente
WHERE nome LIKE '%Silva';

SELECT nome
FROM cliente
WHERE nome LIKE '%Si_va';

-- Consulta especificamente o carater que não se lembra

-- EX 9: NULL - Ausência de valores

-- Consulta campos que possuem o NULL
SELECT nome, telefone
FROM cliente
WHERE telefone IS NULL;

-- Consulta campos que não são mais NULL
SELECT nome, telefone
FROM cliente
WHERE telefone IS NOT NULL;

-- EX 10: ORDER BY - Ordenando resultados
-- ASC Crescente
-- DESC Decrescente

-- Consultar dados de forma crescente
SELECT nome, preco
FROM produto
ORDER BY preco ASC;

-- Consultar dados de forma decrescente
SELECT nome, preco
FROM produto
ORDER BY preco DESC;

-- Consulta por mais de uma coluna
SELECT cidade, nome
FROM cliente
ORDER BY cidade ASC, nome DESC;

-- EX 11: LIMIT - Limitar quantidade de linhas

-- Consultar apenas uma quantidade especifica de linhas
SELECT nome, preco
FROM produto
ORDER BY preco DESC
LIMIT 5;

-- Consultar com limite de valores e linhas
SELECT nome, preco
FROM produto
ORDER BY nome
LIMIT 5 OFFSET 5;

-- EX 12: Calculo de colunas
SELECT nome, preco, preco * 1.10 AS preco_ajustado
FROM produto;

SELECT id_item, quantidade, preco_unitario, quantidade * preco_unitario AS Sub_Total
FROM item_pedido;

-- EX 13: Funções para consultar 

-- Textos
SELECT UPPER(nome) AS Nome_Cliente, LOWER(email) AS Email_Cliente
FROM cliente;

-- CONCAT concatenação de valores
SELECT CONCAT(nome, ' --- ', cidade) AS Cidade_Clientes
FROM cliente;

-- Números
SELECT nome, preco, ROUND(preco * 0.90, 2) AS Preco_Desconto
FROM produto;

-- Datas
SELECT id_pedido, data_pedido, DATE(data_pedido) AS Datas, MONTH(data_pedido) AS Mês, YEAR(data_pedido) AS Ano, DAY(data_pedido) AS Dia, TIME(data_pedido) AS Horário
FROM pedido;

-- COALESCE - Substituir a informação que deixamos em NULL ou não deixamos
SELECT nome, COALESCE(telefone, 'Não Informado') AS telefone
FROM cliente;

-- EX 14: Funções de agrupamento 
-- COUNT - Contar quantos registros existem
-- SUM - Soma de valores
-- AVG - Média de valores
-- MIN - Menor valor
-- MAX - Maior valor

-- Contar quantos clientes existem
SELECT COUNT(*) AS Total_Clientes
FROM cliente;

-- Calcular média dos preços dos produtos
SELECT ROUND(AVG(preco),2) AS Média_Preços
FROM produto;

-- Resumo de preços
SELECT MIN(preco) AS Menor_Preço, MAX(preco) AS Maior_Preço, AVG(preco) AS Média_Preço
FROM produto;

-- Total de vendas ou pedidos realizados com critério
SELECT SUM(valor_total) AS Faturamento_Mensal
FROM pedido
WHERE status_pedido = 'FINALIZADO';

-- EX 15: GROUP BY - Agrupar todos


SELECT cidade, COUNT(*) AS Quantidade_Clientes
FROM cliente 
GROUP BY cidade;


SELECT id_categoria, COUNT(*) AS Quantidade_Produtos
FROM produto
GROUP BY id_categoria;

-- EX 16: HAVING - Filtro por grupos

-- WHERE - Filtra linhas antes do agrupamento
-- HAVING - Filtra linhas depois do GROUP BY

SELECT cidade, COUNT(*) AS Quantidade_Clientes
FROM cliente
GROUP BY cidade
HAVING COUNT(*) >= 2;

-- EX 17: Ordem de criação de uma consulta completa
SELECT colunas
FROM tabela
WHERE condicao
GROUP BY colunas_agrupar
HAVING condicao_agrupar
ORDER BY colunas
LIMIT quantidade;

-----------------------------------------------------
-- PARTE II - COM INNER JOIN, LEFT JOIN, RIGHT JOIN - CONSULTA DE ENTIDADES RELACIONADAS

-- INNER JOIN - CONSULTA DE REGISTROS RELACIONADOS ENTRE DUAS TABELAS 
-- RETORNA REGISTROS QUE POSSUEM CORRESPONDÊNCIAS
-- EX 1: PEDIDOS COM O NOME DO CLIENTE

SELECT P.ID_PEDIDO, P.DATA_PEDIDO, C.NOME AS CLIENTE, P.VALOR_TOTAL FROM PEDIDO AS P
INNER JOIN cliente AS C
ON C.id_cliente = P.id_cliente;

-- LEIA ON: CLIENTE CUJO ID_CLIENTE É IGUAL AO ID_CLIENTE GRAVADO NO PEDIDO
-- ALIAS DE TABELA
-- P E C SÃO APELIDOS QUE DEIXAM CONSULTAS MAIS CURTAS E LEGÍVEIS.

-- EX 2: LEFT JOIN MANTEM TODOS OS REGISTROS DA TABELA DA ESQUERDA MESMO QUANDO NÃO EXISTE CORRESPONDÊNCIA NA TABELA DA DIREITA
-- TODOS OS CLIENTE, INCLUSIVE QUEM NUNCA COMPROU

SELECT C.NOME, P.ID_PEDIDO, P.DATA_PEDIDO
FROM cliente AS C
LEFT JOIN pedido AS P
ON P.id_cliente = C.id_cliente
ORDER BY C.nome;

-- DESCOBRINDO CLIENTES SEM PEDIDOS

SELECT C.ID_CLIENTE, C.NOME
FROM cliente AS C
LEFT JOIN pedido AS P
ON P.id_cliente = C.id_cliente
WHERE P.id_pedido IS NULL;

-- EX 3: JOINS COM TRÊS TABELAS
-- ITENS DE PEDIDO COM NOME DO PRODUTO
SELECT P.ID_PEDIDO, PR.NOME AS PRODUTO, IP.QUANTIDADE, IP.PRECO_UNITARIO, IP.QUANTIDADE * IP.PRECO_UNITARIO AS SUBTOTAL
FROM PEDIDO AS P
INNER JOIN item_pedido AS IP
ON IP.ID_PEDIDO = P.id_pedido
INNER JOIN PRODUTO AS PR 
ON PR.id_produto = IP.id_produto
ORDER BY P.id_pedido;

-- EX 4: JOIN COM CATEGORIA
-- PRODUTO E NOME DE SUA CATEGORIA

SELECT PR.NOME AS PRODUTO, C.NOME AS CATEGORIA, PR.PRECO FROM PRODUTO AS PR
INNER JOIN CATEGORIA AS C
ON C.id_categoria = PR.id_categoria
ORDER BY C.nome, PR.nome;

-- EX 5: AGREGAÇÃO + JOIN 
-- QUANTIDADE DE PRODUTOS POR CATEGORIA

SELECT C.NOME AS CATEGORIA, COUNT(PR.ID_PRODUTO) AS QTDE_PRODUTOS
FROM CATEGORIA AS C
LEFT JOIN produto AS PR
ON PR.id_categoria = C.id_categoria
GROUP BY C.id_categoria, C.nome
ORDER BY QTDE_PRODUTOS DESC;

-- TOTAL COMPRADO POR CLIENTE COM STATUS
SELECT C.NOME AS CLIENTE, COUNT(P.ID_PEDIDO) AS QTDE_PEDIDOS, SUM(P.VALOR_TOTAL) AS TOTAL_COMPRADO
FROM cliente AS C
INNER JOIN PEDIDO AS P
ON P.id_cliente = C.id_cliente
WHERE P.status_pedido = 'PREPARANDO'
GROUP BY C.id_cliente, C.nome
ORDER BY TOTAL_COMPRADO DESC;

-- EX 6: RELATÓRIO COMPLETO DO PEDIDO
SELECT P.ID_PEDIDO, DATE_FORMAT(P.DATA_PEDIDO, '%d %m %Y %H:%i') AS DATA, C.NOME AS CLIENTE, PR.NOME AS PRODUTO, IP.QUANTIDADE, IP.PRECO_UNITARIO, QUANTIDADE * PRECO_UNITARIO AS SUBTOTAL
FROM pedido AS P
INNER JOIN cliente AS C
ON C.id_cliente = P.id_cliente
INNER JOIN item_pedido AS IP
ON IP.id_pedido = P.id_pedido
INNER JOIN produto AS PR
ON PR.id_produto = IP.id_produto
ORDER BY P.id_pedido, PR.nome;
