#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# Desafio 1: Condicionais e Operações (O Aluguel de Carro)
# Enunciado em Python: Escreva um programa em Python que receba o número
# de dias que um carro foi alugado e a quantidade de Km rodados.
# - O aluguel custa R$ 90,00 por dia.
# - Se o cliente rodou até 100 km no total, paga R$ 0,20 por Km rodado.
# - Se rodou mais de 100 km, paga R$ 0,15 por Km rodado.
# Exiba o valor total a pagar formatado com duas casas decimais.
# - O que avalia no aluno: Variáveis, conversão de tipos (float/int), condicionais
# (if/else) e cálculos matemáticos.

print("Calculo do aluguel")
dia = int(input("Digite quantos dias o carro será alugado: "))
km = float(input("Digite a quantidade de Km rodados: "))

if km > 100:
    total = (90 * dia) + (km * 0.15)
else:
    total = (90 * dia) + (km * 0.20)

print(f"Valor total: {total:.2f}")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

#Desafio 2: Repetição e Listas (O Filtro de Pares)
# Enunciado em Python: Dado o seguinte código inicial com uma lista de
# números:
# numeros = [12, 5, 8, 21, 14, 3, 10, 7]
# Escreva um programa que:
# 1. Percorra a lista e crie uma nova lista contendo apenas os números pares.
# 2. Calcule e exiba a média desses números pares.
# - O que avalia no aluno: Laços de repetição (for), listas, método .append(),
# acúmulo de valores e o operador de resto de divisão %.

numeros = [12, 5, 8, 21, 14, 3, 10, 7]
pares = []

for num in numeros:
    if num % 2 == 0:
        pares.append(num)
    
media = sum(pares) / len(pares) # len conta quantos números tem na lista ## sum para somar os números da lista
qtd = len(pares)
print("Pares:", pares)
print("Quantidade de numéros pares: ",qtd)
print("Média: ", media)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# Desafio 3: Funções e Dicionários (O Desconto no Produto)
# Enunciado em Python: Crie um dicionário representando um produto: produto =
# {"nome": "Teclado Mecânico", "preco": 200.0, "estoque": 15}
# 1. Crie uma função chamada aplicar_desconto que receba o dicionário do
# produto
# e a porcentagem de desconto (ex: 10 para 10%).
# 2. A função deve atualizar o preço do produto dentro do dicionário e exibir a
# mensagem: "O produto [NOME] agora custa R$ [NOVO_PRECO]!”

produto = {"nome": "Teclado Mecânico", "preco": 200.0, "estoque": 15, "categora": "Periféricos"}

def aplicar_desconto(item, porcentagem):
    item["preco"] -= item["preco"]  * (porcentagem / 100)
    print(f"O produto {item['nome']} agora custa R$ {item['preco']:.2f}! E a categoria {item['categoria']}")

aplicar_desconto(produto, 10)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#