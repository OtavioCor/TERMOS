create database Oficina_Otavio;
use Oficina;

create table Clientes (
ID_Clientes int auto_increment primary key,
Nome varchar(50) not null,
Telefone varchar(15),
Email varchar(60),
CPF varchar(14) not null unique,
Data_Cadastro timestamp default current_timestamp not null);

create table Servicos (
ID_Servicos int auto_increment primary key,
Nome varchar(50) not null,
Telefone varchar(14),
Email varchar(60),
Tipo text not null,
Data_Cadastro timestamp default current_timestamp not null);

create table Funcionarios (
ID_Funcionarios int auto_increment primary key,
Nome varchar(50) not null,
Turno varchar(50),
Email varchar(60),
CPF varchar(14) not null unique,
Cargo varchar(50));

create table Pecas (
ID_Pecas int auto_increment primary key,
Nome varchar(50) not null,
Quantidade int,
Preco decimal,
OrigemFabricacao varchar(50),
Data_Compra timestamp default current_timestamp not null);

create table Fornecedores (
ID_Fornecedores int auto_increment primary key,
Nome varchar(50) not null,
Empresa varchar(50),
Quantidade int,
CNPJ bigint not null,
Data_Fornecimento timestamp default current_timestamp not null);

create table OrdemServico (
ID_OrdemServico int auto_increment primary key,
Nome varchar(50) not null,
Preco decimal,
Status_Servico varchar(50),
Registro text not null,
Data_Servico timestamp default current_timestamp not null);

create table Pagamento (
ID_Pagamento int auto_increment primary key,
Pix varchar(10),
Credito varchar(10),
Debito varchar(10),
Valor decimal not null,
Data_Pagamento timestamp default current_timestamp not null);

create table Veiculos (
ID_Veiculos int auto_increment primary key,
Nome varchar(50) not null,
Placa varchar(8),
Motor varchar(20),
Tipo varchar(50) ,
Documentacao text not null);

create table Marcas (
ID_Marcas int auto_increment primary key,
Nome varchar(50) not null,
Pais varchar(20),
Ano year,
Categoria varchar(20),
Email varchar(50));

create table Modelos (
ID_Modelos int auto_increment primary key,
Garantia varchar(50),
Cor varchar(20),
Nome varchar(50) not null,
Observacao text,
Ano year not null);

alter table Clientes add novo_campo varchar(60);
alter table Fornecedores add novo_campo varchar(60);
alter table Funcionarios add novo_campo varchar(60);
alter table Marcas add novo_campo varchar(60);
alter table Modelos add novo_campo varchar(60);
alter table OrdemServico add novo_campo varchar(60);
alter table Pagamento add novo_campo varchar(60);
alter table Pecas add novo_campo varchar(60);
alter table Servicos add novo_campo varchar(60);
alter table Veiculos add novo_campo varchar(60);

alter table Clientes drop column novo_campo;
alter table Fornecedores drop column novo_campo;
alter table Funcionarios drop column novo_campo;
alter table Marcas drop column novo_campo;
alter table Modelos drop column novo_campo;
alter table OrdemServico drop column novo_campo;
alter table Pagamento drop column novo_campo;
alter table Pecas drop column novo_campo;
alter table Servicos drop column novo_campo;
alter table Veiculos drop column novo_campo;

rename table Modelos to modelos_fab;
