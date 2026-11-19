DROP DATABASE IF EXISTS smartcoffee_procedures_otavio;
CREATE DATABASE smartcoffee_procedures_otavio;
USE smartcoffee_procedures_otavio;

-- AULA 13 - ATIVIDADE STORED PROCEDURES
-- Aluno: Otavio Correia
-- Turma: 2DEVIS

-- 1. listar_clientes_ativos()
DELIMITER $$
CREATE PROCEDURE LISTAR_CLIENTE_ATIVOS()
BEGIN
    SELECT NOME
    FROM cliente
    WHERE ATIVO = TRUE;
END $$

CALL `LISTAR_CLIENTE_ATIVOS`

-- 2. buscar_produto_por_nome(IN p_busca VARCHAR(100))

DELIMITER $$
CREATE PROCEDURE BUSCAR_PRODUTO_POR_NOME(IN P_BUSCA VARCHAR(100))
BEGIN
    SELECT NOME
    FROM produto
    WHERE NOME = P_BUSCA;
END $$

CALL BUSCAR_PRODUTO_POR_NOME('Suco de Laranja');


-- 3. produtos_por_categoria(IN p_id_categoria INT)

DELIMITER $$
CREATE PROCEDURE PRODUTOS_POR_CATEGORIA(IN P_ID_CATEGORIA INT)
BEGIN
    SELECT NOME, PRECO
    FROM PRODUTO
    WHERE id_CATEGORIA = P_ID_CATEGORIA;
END$$

CALL `PRODUTOS_POR_CATEGORIA`(1);

-- 4. total_clientes(OUT p_total INT)
DELIMITER $$
CREATE PROCEDURE TOTAL_CLIENTES(OUT P_TOTAL INT)
BEGIN 
    SELECT COUNT(*)
    INTO P_TOTAL
    FROM cliente;
END $$

CALL `TOTAL_CLIENTES`(@total);
SELECT @total;
-- 5. consultar_estoque(IN p_id_produto INT) usando variável local
DELIMITER $$
CREATE PROCEDURE CONSULTAR_ESTOQUE(IN P_ID_PRODUTO INT)
BEGIN 
    SELECT QUANTIDADE
    FROM ESTOQUE
    WHERE ID_PRODUTO = P_ID_PRODUTO;
END $$

CALL `CONSULTAR_ESTOQUE`(2); 
-- 6. classificar estoque: 0 SEM ESTOQUE / <=5 BAIXO / >5 NORMAL
DELIMITER $$
CREATE PROCEDURE CLASSIFICAR_ESTOQUE ( IN P_ID_PRODUTO INT )
BEGIN
    DECLARE V_QUANTIDADE INT;

    SELECT QUANTIDADE
    INTO V_QUANTIDADE
    FROM ESTOQUE
    WHERE ID_PRODUTO = P_ID_PRODUTO;

    IF V_QUANTIDADE = 0 THEN
        SELECT 'SEM ESTOQUE' AS SITUAÇÃO;
    ELSEIF V_QUANTIDADE <= 5 THEN
        SELECT 'ESTOQUE BAIXO' AS SITUAÇÃO;
    ELSE
        SELECT 'ESTOQUE NORMAL' AS SITUAÇÃO;
    END IF;
END $$

CALL `CLASSIFICAR_ESTOQUE`(2);
-- 7. cadastrar_cliente(...) com três parâmetros IN
DELIMITER $$

CREATE PROCEDURE CADASTRAR_CLIENTE (
    IN P_NOME VARCHAR (100),
    IN P_EMAIL VARCHAR (120),
    IN P_TELEFONE VARCHAR (20)
)
BEGIN
    INSERT INTO CLIENTE (NOME, EMAIL, TELEFONE, ATIVO)
    VALUES (P_NOME, P_EMAIL, P_TELEFONE, TRUE);
END $$
CALL CADASTRAR_CLIENTE ( 'BRUNO AUGUSTO', 'BRUNO@EMAIL.COM', '1999999999' );

-- 8. alterar_preco(...) impedindo valor <= 0
DELIMITER $$
CREATE PROCEDURE ATUALIZAR_PRECO_PRODUTO (
    IN P_ID_PRODUTO INT,
    IN P_NOVO_PRECO DECIMAL(10,2)
)
BEGIN
    IF P_NOVO_PRECO > 0 THEN
        UPDATE PRODUTO
        SET PRECO = P_NOVO_PRECO
        WHERE ID_PRODUTO = P_ID_PRODUTO;

        SELECT 'PREÇO ATUALIZADO' AS MENSAGEM;
    ELSE
        SELECT 'PREÇO INVÁLIDO' AS MENSAGEM;
    END IF;
END $$

CALL ATUALIZAR_PRECO_PRODUTO(2,12);

SELECT * FROM produto;
-- 9. criar_pedido(IN p_id_cliente INT, OUT p_id_pedido INT)
DELIMITER $$

CREATE PROCEDURE criar_pedido (
    IN p_id_cliente INT,
    OUT p_id_pedido INT
)
BEGIN
    INSERT INTO PEDIDO (
        ID_CLIENTE,
        DATA_PEDIDO,
        STATUS_PEDIDO
    )
    VALUES (
        p_id_cliente,
        NOW(),
        'ABERTO'
    );

    -- 10. devolver ID com LAST_INSERT_ID()
    SET p_id_pedido = LAST_INSERT_ID();
END $$

-- 10. devolver ID com LAST_INSERT_ID()


-- 11. adicionar_item_pedido(...) buscando o preço atual

-- 12. Faça uma chamada inválida e explique o resultado.

-- 13. Use SHOW CREATE PROCEDURE.

-- 14. Remova uma procedure com DROP PROCEDURE IF EXISTS e recrie-a.

-- DESAFIO FINAL:
-- Crie uma procedure de negócio com:
-- - pelo menos 2 parâmetros;
-- - variável local;
-- - IF;
-- - pelo menos uma alteração no banco.