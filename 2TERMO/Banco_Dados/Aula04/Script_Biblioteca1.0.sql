-- COMANDO PARA CRIAR BANCO DE DADOS
create database Biblioteca_Sugiro;
create database Biblioteca_Sugiro2;

-- COMANDO PARA APAGAR BANCO DE DADOS
drop database biblioteca_sugiro2;

-- COMANDO PARA ATIVAR BANCO DE DADOS
use Biblioteca_Sugiro;

-- COMANDO PARA CRIAR TABELAS
create table Clientes (
ID_CLIENTES int auto_increment primary key,
Nome varchar(60) not null,
Idade int not null,
Data_cadastro timestamp default current_timestamp,
Telefone varchar(14),
Email varchar(60),
CPF varchar(14) not null unique
);

create table Funcionarios (
ID_FUNCIONARIOS int auto_increment primary key,
Nome varchar(50) not null,
Cargo varchar(50) not null,
Turno varchar(100) not null,
Matricula varchar(100) not null unique,
Horario_Entrada_Saida datetime not null
);

create table Emprestimo (
ID_EMPRESTIMO int auto_increment primary key,
Observacao varchar(500),
Data_Emprestimo date not null,
Quantidade_dias int not null,
Data_Devolucao date not null,
Status_Emprestimo varchar(20) default "Ativo"
);

create table Compra (
ID_COMPRA int auto_increment primary key,
Data_Compra date not null,
Status_Compra varchar(20),
Preco decimal not null,
Data_Entrega date not null,
Forma_Pagamento varchar(20) not null default "Pix"
);

create table Livro (
ID_LIVRO int auto_increment primary key,
Titulo varchar(100) not null,
ISBN bigint not null unique,
Estoque varchar(100),
Ano_Publicacao date,
Autor varchar(100),
Editora varchar(100) not null
);
