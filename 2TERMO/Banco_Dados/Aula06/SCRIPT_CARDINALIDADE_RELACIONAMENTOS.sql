-- Geração de Modelo físico
-- Sql ANSI 2003 - brModelo.



CREATE TABLE Cliente (
ID_Cliente Int auto_increment primary key PRIMARY KEY,
Nome_Cliente Varchar(50) not null
)

CREATE TABLE Pedido (
ID_Pedido Int auto_increment primary key PRIMARY KEY,
Data_Pedido Datetime not null,
ID_Cliente Int auto_increment primary key,
FOREIGN KEY(ID_Cliente) REFERENCES Cliente (ID_Cliente)
)

CREATE TABLE Estoque (
Nome_Produto Varchar(50) not null,
ID_Produto Int auto_increment primary key,
ID_Estoque Int auto_increment primary key,
Quantidade Int not null,
PRIMARY KEY(ID_Produto,ID_Estoque)
)

CREATE TABLE Produto (
ID_Produto Int auto_increment primary key PRIMARY KEY,
Nome_Produto Varchar (100) not null
)

CREATE TABLE Fornecedor (
Razao_Social Varchar (100) not null,
ID_Fornecedor Int auto_increment primary key PRIMARY KEY
)

CREATE TABLE Item_Produto (
ID_Produto Int not null,
ID_Fornecedor Int not null,
ID_Item Int auto_increment primary key PRIMARY KEY,
Valor Decimal(10,2)
)
