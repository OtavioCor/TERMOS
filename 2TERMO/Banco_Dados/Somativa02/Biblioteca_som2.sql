-- Active: 1788435098023@@127.0.0.1@3306@biblioteca_som2

-- 1. Criação do banco — 3 pts
-- Crie o banco biblioteca_som2 e selecione-o.
create database if not exists biblioteca_som2;

use biblioteca_som2;

-- 2. Tabela USUARIO — 6 pts
-- Crie a tabela respeitando RN01, RN02 e RN03.

create table if not exists Usuario (
id_usuario int auto_increment primary key,
nome VARCHAR(100) not null,
email VARCHAR(120) not null unique,
telefone VARCHAR(20),
ativo BOOLEAN DEFAULT TRUE
);

-- 3. Tabela LIVRO — 6 pts
-- Crie a tabela e utilize CHECK para impedir quantidade negativa.

create table if not exists Livro (
id_livro int auto_increment primary key,
titulo VARCHAR(150) not null,
autor VARCHAR(120) not null,
isbn CHAR(13) not null unique,
ano_publicacao INT,
quantidade_disponivel INT DEFAULT 0,
CONSTRAINT ck_quantidade_disponivel CHECK (quantidade_disponivel >= 0)
);


-- 4. Tabela EMPRESTIMO — 7 pts
-- Crie PK, duas FKs, DEFAULTs e CHECK de status. As FKs devem impedir
-- exclusão de usuário ou livro com histórico.

create table if not exists Emprestimo (
id_emprestimo int auto_increment primary key,
data_emprestimo datetime default current_timestamp,
data_prevista date not null,
data_devolucao date,
status_emprestimo VARCHAR(20) DEFAULT 'ABERTO',
CONSTRAINT ck_status_emprestimo CHECK (status_emprestimo = 'ABERTO'),

id_usuario INT,
FOREIGN KEY (id_usuario) REFERENCES Usuario (id_usuario),

id_livro INT,
FOREIGN KEY (id_livro) REFERENCES livro (id_livro)
);

-- TABELAS ADICIONAIS

create table if not exists Funcionarios (
id_funcionario int auto_increment primary key,
Nome varchar(50) not null,
Cargo varchar(50) not null,
Turno varchar(100) not null,
Matricula varchar(100) not null unique,
Horario_Entrada_Saida datetime not null
);

create table if not exists Compra (
id_compra int auto_increment primary key,
Data_Compra date not null,
Status_Compra varchar(20),
Preco decimal not null,
Data_Entrega date not null,
Forma_Pagamento varchar(20) not null default "Pix"
);

-- 5. ALTER TABLE — 3 pts
-- Adicione editora VARCHAR(100) à tabela LIVRO.

alter table livro add editora varchar(100);

-- 6. INSERT de usuários — 4 pts
-- Cadastre pelo menos 4 usuários; um deles deve ter telefone NULL.
SELECT * FROM usuario

insert into usuario (nome, email, telefone, ativo) VALUES 
('Bruno', 'labubu@gmail.com', '19676767676', TRUE),
('Celso', 'celsius@gmail.com', '19988362891', TRUE),
('Samira', 'sami@gmail.com', '19999835202', TRUE),
('Mathes', 'poste@gmail.com', NULL, TRUE);

-- 7. INSERT de livros — 5 pts
-- Cadastre pelo menos 6 livros com autores, ISBNs, anos e quantidades diferentes.

SELECT * FROM livro

insert into livro (titulo, autor, isbn, ano_publicacao, quantidade_disponivel, editora) VALUES 
('Dom Casmurro', 'Machado de Assis', '9788535932591', 1899, 15, 'Companhia das Letras'),
('1984', 'George Orwell', '9788535914849', 1949, 8, 'Companhia das Letras'),
('O Pequeno Príncipe', 'Antoine de Saint-Exupéry', '9788522031412', 1943, 23, 'HarperCollins Brasil'),
('Sapiens: Uma Breve História da Humanidade', 'Yuval Noah Harari', '9788525059208', 2011, 5, 'L&PM Editores'),
('O Alquimista', 'Paulo Coelho', '9788575427583', 1988, 12, 'Paralela'),
('Torto Arado', 'Itamar Vieira Junior', '9788511003117', 2019, 19 , 'Todavia');

-- 8. INSERT de empréstimos — 4 pts
-- Cadastre pelo menos 3 empréstimos ABERTOS para usuários e livros existentes.

SELECT * FROM emprestimo;

insert into emprestimo (data_emprestimo, data_prevista, data_devolucao, status_emprestimo, id_usuario, id_livro) VALUES 
(NOW(), '2026-10-26', NULL, DEFAULT, 3, 5),
(NOW(), '2026-10-30', NULL, DEFAULT, 1, 3),
(NOW(), '2026-10-28', NULL, DEFAULT, 2, 1);

-- 9. UPDATE — 4 pts
-- Localize um usuário com SELECT e depois altere seu telefone com UPDATE.

SELECT *
FROM usuario 
WHERE id_usuario = 4;

UPDATE usuario 
SET telefone = '19998628801'
WHERE id_usuario = 4;

-- 10. Atualização em lote — 4 pts
-- Acrescente 2 exemplares a todos os livros publicados a partir de 2020.

SELECT * FROM livro;

UPDATE livro
SET quantidade_disponivel = quantidade_disponivel + 2
WHERE ano_publicacao >= 2020;


-- 11. DELETE e integridade — 4 pts
-- Crie e exclua um usuário sem empréstimos. Depois tente excluir um usuário que possua empréstimo e explique o resultado.

SELECT * FROM usuario

insert into usuario (nome, email, telefone, ativo) VALUES 
('Otavio', 'ota@gmail.com', '19758442634', TRUE);

DELETE FROM usuario
WHERE id_usuario = 5;

-- Usuario com emprestimo
DELETE FROM usuario
WHERE id_usuario = 2;

-- Resultado = Cannot delete
-- Não é possível apagar por conta da FK, que está relacionando os dados entre as tabelas, fazendo com que caso apague afetará outros dados

-- 12. SELECT básico — 2 pts
-- Liste título, autor e quantidade disponível de todos os livros.

SELECT titulo, autor, quantidade_disponivel
FROM livro;


-- 13. WHERE + ORDER BY — 3 pts
-- Liste livros com quantidade maior que 2, do maior para o menor estoque.

SELECT *
FROM livro
WHERE quantidade_disponivel > 2
ORDER BY quantidade_disponivel DESC;

-- 14. LIKE — 3 pts
-- Pesquise livros cujo título contenha uma palavra escolhida por você.

SELECT *
FROM livro
WHERE titulo LIKE '%pequeno%';

-- 15. BETWEEN — 3 pts
-- Liste livros publicados entre 2015 e 2025.

SELECT *
FROM livro
WHERE ano_publicacao BETWEEN 2015 and 2025;

-- 16. Funções agregadas — 4 pts
-- Mostre COUNT, SUM, AVG, MIN e MAX sobre a quantidade disponível.

SELECT COUNT(quantidade_disponivel) AS Registros, SUM(quantidade_disponivel) AS Soma, ROUND(AVG(quantidade_disponivel),2) AS Média, MIN(quantidade_disponivel) AS Menor_Valor, MAX(quantidade_disponivel) AS Maior_Valor
FROM livro;


-- 17. INNER JOIN — 4 pts
-- Liste ID do empréstimo, usuário, livro, data e status.

SELECT P.ID_PEDIDO, P.DATA_PEDIDO, C.NOME AS CLIENTE, P.VALOR_TOTAL FROM PEDIDO AS P
INNER JOIN cliente AS C

-- 18. JOIN + WHERE — 3 pts
-- Mostre apenas os empréstimos ABERTOS.

-- 19. GROUP BY — 4 pts
-- Mostre cada usuário e sua quantidade de empréstimos, do maior para o menor.

-- 20. LEFT JOIN — 4 pts
-- Liste todos os usuários, inclusive os que nunca fizeram empréstimo, com a
-- quantidade de empréstimos de cada um.

