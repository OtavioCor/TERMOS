-- Geração de Modelo físico
-- Sql ANSI 2003 - brModelo.

CREATE TABLE Pedidos(
Id_Pedidos int auto_increment primary key,
Presencial varchar(100),
Delivery varchar(100),
Status_pedidos varchar(50),
Tipo_pedido varchar(10)
Valor_total decimal(10,2) not null,
Data_hora_pedido datetime not null,
PRIMARY KEY(Id_Pedidos)
)

CREATE TABLE Pagamento (
Status_pagamento varchar(20),
Id_Pagamento int auto_increment primary key,
Valor_pago decimal(10,2) not null,
Data_hora_pagamento datetime not null,
Pix decima(10,2),
Cartao decima(10,2),
Dinheiro decima(10,2),
Forma_pagamento varchar(8),
PRIMARY KEY(Id_Pagamento)
)

CREATE TABLE Produtos(
Id_Produto int auto_increment primary key,
Nome_produto varchar(50) not null,
Descricao_produto text
Preco_unitario decimal(10,2)
Categoria varchar(20)
PRIMARY KEY(Id_Produto)
)

CREATE TABLE Categoria (
Descricao_categoria text,
Nome_categoria varchar(50) not null,
Status_categoria varchar(20),
Id_Categorias int auto_increment primary key,
Data_Criacao datetime,
Setor varchar(50) not null,
PRIMARY KEY(Id_Categorias)
)

CREATE TABLE Fornecedor (
Id_Fornecedor int auto_increment primary key PRIMARY KEY,
Nome varchar(50) not null,
Empresa varchar(100),
CNPJ bigint not null,
Data_fornecedor datetime,
Quantidade int,
Id_Estoque int
)

CREATE TABLE Estoque (
Id_Estoque int auto_increment primary key PRIMARY KEY,
Nome_insumo varchar(50) not null,
Quantidade_atual decimal(10,2),
Quantidade_minima decimal(10,2),
kg varchar(10),
ml varchar(10),
un varchar(10)
)

CREATE TABLE Programa de fidelidade (
Id_Fidelidade int auto_increment primary key,
Saldo_pontos int,
Data_ultima_atualizacao datetime
PRIMARY KEY(Id_Fidelidade)
)

CREATE TABLE Clientes (
Id_Cliente int auto_increment primary key,
Nome_cliente varchar(50) not null,
CPF_cliente varchar(20) not null,
E-mail_cliente varchar(100),
Telefone_cliente varchar(10),
Data_Cadastro_cliente datetime,
PRIMARY KEY(Id_Cliente)
)

CREATE TABLE  Delivery (
Id_Delivery int auto_increment primary key PRIMARY KEY,
Data_hora_saida datetime,
Status_entrega varchar(50),
Taxa_entrega decima(10,2),
Endereco_entrega varchar(50),
Id_Pedidos int,
FOREIGN KEY (Id_Pagamento) REFERENCES Pagamento (Id_Pagamento)
FOREIGN KEY (Id_Pedidos) REFERENCES Pedidos (Id_Pedidos)
)

CREATE TABLE Funcionarios (
Id_Funcionario int auto_increment primary key PRIMARY KEY,
Salario decimal(10,2) ,
Cargo varchar(50),
Data_admissao datetime not null,
Nome_funcionario varchar(50) not null,
CPF_funcionario varchar(20) not null
)

CREATE TABLE Entrega (
Id_Delivery int,
Id_Funcionario int ,
FOREIGN KEY(Id_Funcionario) REFERENCES Funcionarios (Id_Funcionario)
)

CREATE TABLE Atende (
Id_Pagamento int,
Id_Pedidos int ,
Id_Funcionario int ,
FOREIGN KEY(Id_Pagamento) REFERENCES Pagamento (Id_Pagamento),
FOREIGN KEY(Id_Funcionario) REFERENCES Funcionarios (Id_Funcionario)
FOREIGN KEY(Id_Pedidos) REFERENCES Pedidos (Id_Pedidos)
)

CREATE TABLE Realiza (
Id_Pagamento int,
Id_Pedidos int ,
Id_Cliente int ,
FOREIGN KEY(Id_Pedidos) REFERENCES Pedidos (Id_Pedidos),
FOREIGN KEY(Id_Pagamento) REFERENCES Pagamento (Id_Pagamento),
FOREIGN KEY(Id_Fidelidade) REFERENCES Programa de fidelidade (Id_Fidelidade),
FOREIGN KEY(Id_Cliente) REFERENCES Clientes (Id_Cliente)
)

CREATE TABLE Contem (
Id_Pagamento int,
Id_Pedidos int,
Id_Categorias int,
Id_Produto int,
FOREIGN KEY(Id_Pedidos) REFERENCES Pedidos (Id_Pedidos),
FOREIGN KEY(Id_Pagamento) REFERENCES Pagamento (Id_Pagamento),
FOREIGN KEY(Id_Categorias) REFERENCES Categoria (Id_Categorias),
FOREIGN KEY(Id_Produto) REFERENCES Produtos (Id_Produto)
)

CREATE TABLE Consome  (
Id_Estoque int,
Id_Categorias int,
Id_Produto int,
FOREIGN KEY(Id_Estoque) REFERENCES Estoque (Id_Estoque),
FOREIGN KEY(Id_Categorias) REFERENCES Categoria (Id_Categorias),
FOREIGN KEY(Id_Produto) REFERENCES Produtos (Id_Produto)
)

