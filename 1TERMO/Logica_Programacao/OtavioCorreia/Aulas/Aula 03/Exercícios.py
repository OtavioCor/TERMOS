#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# Calculo de notas por semestre onde terá duas notas formativas e uma somativa para encerrar o semestre

p1 = float(input("Digite sua primeira nota formativa: "))
p2 = float(input("Digite sua segunda nota formativa: "))
p3 = float(input("Digite sua primeira nota somativa: "))
c1 = (p1+p2+p3)/3
print("\nSua nota final é:", c1)

q1 = float(input("\nDigite sua primeira nota formativa: "))
q2 = float(input("Digite sua segunda nota formativa: "))
q3 = float(input("Digite sua primeira nota somativa: "))
c2 = (q1+q2+q3)/3
print("\nSua nota final é:", c2)

print("\nMédia do primeiro semestre:\n", round(c1,2))
print("Média do segundo semstre:\n", round(c2,2))

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# Calculo de idade
# Deve apresentar o nome, curso, data de nascimento e apresentar a idade sua no final

nome = input("Digite seu nome: ")
curso = input("Digite seu curso: ")
nasc = float(input("Digite seu ano de nascimento: "))
print("Seu nome é", nome,", cursando", curso,", com", float(2026 - nasc),"anos")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# Calcular gorjetas 
#Receba o valor da conta de um restaurante e retorne o valor da gorjeta (considerando 10% do valor da conta)

print("Bem vindo ao Sugiro Restaurant\n")
valor = float(input("Digite o valor total: "))
gorjeta = valor * 10 / 100
print("O valor total é: ", valor + gorjeta)
print("Gorjeta:", gorjeta)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# Criar um sistema para calcular o sucessor e antecessor de um valor

print("Digite um número para descobrir seu sucessor e antecessor:\n")
n1 = float(input("Digite o valor: "))
print("Sucessor:", n1 + 1 ,"\nAntecessor:", n1 - 1)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

#Criar um algoritmo para calcular a venda de livros e que toda venda apresente um desconto fixo de 5%

print("Bem vindo à Livraria do Carlos\n")
p1 = float(input("Digite o preço do livro: "))
desc = p1 * 5 / 100
print("Preço total: ", p1 - desc)
print("Desconto: ", desc)
