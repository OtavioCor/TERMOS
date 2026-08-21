-- COMANDO PARA CRIAR DB
-- 1
create database biblioteca_otavio;
-- CASO NÃO EXISTA, CRIE A PASTA
create database if not exists biblioteca_otavio;

-- ATIVAR O BANCO DE DADOS
-- 2 
use biblioteca_otavio;

-- TABELAS
-- 3
create table if not exists Clientes (
ID_CLIENTES int auto_increment primary key,
Nome varchar(60) not null,
Idade int not null,
Telefone varchar(14),
CPF varchar(14) not null unique,
Convenio enum ('SIM','NÃO')default 'SIM',
Data_cadastro timestamp default current_timestamp
);

create table if not exists Estacionamento (
ID_VAGAS int auto_increment primary key,
Veiculo varchar(50),
Quantidade_Vaga int not null,
Vaga_Preferencial enum ('SIM','NÃO')default 'SIM',
Placa varchar(8) not null
);

create table if not exists Compra (
ID_COMPRA int auto_increment primary key,
Data_Compra date not null,
Status_Compra varchar(20),
Preco decimal (5, 2) default 0.00,
Data_Entrega date not null,
Forma_Pagamento varchar(20) not null default "Pix"
);


-- VIZUALIZAR TABELAS
-- 4
show tables;

-- EM CASO DE NECESSIDADE --
-- APAGAR BANCO DE DADOS
drop database biblioteca_otavio;
-- APAGAR TABELAS
drop table Clientes;

-- CASO TENHA ESQUECIDO DE ALGO NA TABELA
-- INSETIR CAMPOS
alter table Clientes add email varchar(60);

-- ALTERAR TIPO DE DADOS
alter table Clientes modify Telefone int;

-- APAGAR COLUNA OU ATRIBUTO
alter table Clientes drop column Telefone;

-- RENOMEAR TABELAS
rename table Clientes to Cadastro;

-- APAGAR DADOS DE UMA TABELA
truncate table Cadastro;
truncate table Compra;

-- INSERINDO DADOS NA TABELA
insert into Compra (ID_COMPRA, Data_Compra, Status_Compra, Preco, Data_Entrega, Forma_Pagamento)
values(default ,'26-08-24', 'Entrega', 35.00, '2026-08-29', default), (default ,'2026-09-03', 'Verificação', 70.50, '2026-09-08', 'Débito');

-- CONSULTAR DADOS EM UMA TABELA
select * from Compra;

insert into Estacionamento (ID_VAGAS, veiculo, quantidade_vaga, vaga_preferencial, placa)
values(default, 'Carro', 59, 'não', 'ABC 1A23'), (default, 'Moto', 58, 'não', 'DEF 1A23'), (default, 'Carro', 57, 'sim', 'LFA 3K90'), (default, 'Carro', 56, 'não', 'OFA 1P53'), (default, 'Vã', 55, 'sim', 'PFG 1A67');

select * from Estacionamento;

truncate table Estacionamento;


