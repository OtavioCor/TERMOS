-- PROJETO SMART COFFEE OTAVIO
create database Smartcoffee;
use Smartcoffee;

create table Clientes (
ID_Clientes int auto_increment primary key,
Nome varchar(60) not null,
Telefone varchar(14),
Email varchar(60),
CPF varchar(14) not null unique,
Data_Cadastro date not null);

create table Pedidos (
ID_Pedidos int auto_increment primary key,
Data_Cadastro date not null,
Desconto varchar(4),
Quantidade int not null,
Preco int not null,
Status enum ('Em Processamento','Enviado', 'Saiu para entrega', 'entregue')default 'Em Processamento',
);

create table Produtos (
ID_Produtos int auto_increment primary key,
Descricao varchar(3000),
Nome varchar(60) not null,
Preco int not null,
Status_Produto enum ('Ativo', 'Inativo')default'Ativo');

create table Estoque (
ID_Estoque int auto_increment primary key,
Localizacao varchar(3000),
Nome varchar(60) not null,
Quantidade_Atual int not null,
Limite int not null,
Quantidade_Minima int not null);

create table Fornecedor (
ID_Fornecedor int auto_increment primary key,
Nome varchar(60) not null,
Empresa varchar(60)
CNPJ int not null,
Data_Fornecedor date,
Quantidade int not null);

create table Programa_FIdelidade (
ID_Programa int auto_increment primary key,
Nome varchar(60) not null,
CPF varchar(14) not null unique,
Email varchar(60),
Data_Programa date);

create table Categoria (
ID_Categorias int auto_increment primary key,
Nome varchar(60) not null,
Status_Categoria enum ('Ativo', 'Inativo')default'Ativo',
Setor varchar(60),
Data_Criacao date,
Descricao varchar(3000));

create table Pagamento (
ID_Pagamento int auto_increment primary key,
Data_Pagamento date,
Pix varchar(60) not null,
Crédito int,
Debito int,
Valor int);

create table Delivery (
ID_Delivery int auto_increment primary key,
Nome varchar(60) not null,
Endereco varchar(200) not null,
Pagamento enum ('Crédito', 'Pix', 'Débito')default'Pix',
Telefone varchar(14),
Status_Delivery enum ('Ativo', 'Inativo')default'Ativo');

create table Funcionarios (
ID_Funcionarios int auto_increment primary key,
Nome varchar(60) not null,
Turno varchar(60) not null,
CPF varchar(14) not null unique,
Cargo varchar(50),
Email varchar(60));

