#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# Escreva um programa que solicite ao usuário um número inteiro e calcule a média de uma lista de números. 
# O programa deve tratar os seguintes erros:
# ValueError: Se o usuário digitar um valor que não seja um número inteiro

print("Calculadora de média")
numero = int(input("Quantos numeros você deseja? "))
soma = 0
try:
    for i in range(numero):
        i = int(input(f"Digite o {i+1}° número: "))
        soma += i
    print(f"A média calculada é: {soma/numero:.1f}")

except ValueError:
    print("Erro: Entrada inválida. Por favor, digite um número inteiro.")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# Escreva um programa que solicite ao usuário uma lista de palavras e conte quantas vezes cada palavra aparece na lista. 
# O programa deve tratar os seguintes erros:
# - ValueError: Se o usuário digitar um valor que não seja uma string.

print("Lista de palavras")
num = int(input("Digite quantas palavras: "))
lista = []
qnt = 0
try:
    for palavra in range(num):
        lista = input(f"Digite a {palavra+1}° palavra: ")
        qnt += (lista.strip().count("python"))
except ValueError:
    print("Erro: Entrada inválida. Por favor, digite apenas palavras.")
    print(f"A palavra 'python' foi apresentada {qnt} vezes, em uma lista de {num} palavras")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

try:
    palavras = input("Digite uma lista de palavras separadas por espaço... ").split()
    contagem = {}
    for palavra in palavras:
        if palavra in contagem:
            contagem[palavra] += 1
        else:
            contagem[palavra] = 1
    print("Contagem de palavras")
    for palavra, contagem in contagem.items():
        print(f"{palavra}: {contagem}")
except ValueError:
    print("Erro: Entrada inválida. Por favor, digite uma lista de palavras separadas por espaço")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# Escrever um programa mais simples com testes de tratamento de erros, como por exemplo, solicitar ao usuário um número.
# O programa deve tratar os seguintes erros:
# - ValueError: se o usuário digitar um valor que não seja um número.
# - ZeroDivisorError: se o usuário digitar zero como divisor

print("Testes de tratamento para erros")
try:
    a = int(input("Digite o 1º número: "))
    b = int(input("Digite o 2º número: "))
    resultado = a / b
    print (resultado)
except ValueError:
    print("Erro: Entrada inválida. Por favor, digite um valor que seja número inteiro.")
except ZeroDivisionError:
    print("Erro: Não é possível dividir por zero.")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

