#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# Contador de Produção {for}
# Uma esteira procesa 10 peças por ciclo. Crie um programa que use um for para contar de 1 a 10 e, para cada número
# Imprima: "Peça nº X processada com sucesso". 
# No final, exiba "Ciclo de produção concluído"

for x in range(1, 11):
    print(f"Peça nº {x} processada com sucesso")
print("Ciclo de produção concluído")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# Imagine a produção de frutas em uma feira. 
# Desejo apresentar as frutas: banana, manga, melancia, abacaxi. 
# Com uma quantidade de 10 bananas, 5 mangas, 10 melancias e 13 abacaxi
# Apresente o total de frutas

frutas = {"10 bananas", "5 mangas", "10 melancias", "13 abacaxis"}

for i in frutas:
    print(f"Quantidade de frutas: {i}")
print ("A quantidade total de frutas é: ", 10 + 10 + 13 + 5)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# Montar uma tabuada inicialmente pode ser usado por um valor fixo e depois usar a pergunta

print("Descubra a tabuada do 5:\n")
for num in range(11):
    print(f"5 * {num} é igual à:", 5 * num)

print("Digite um número para descobrir sua tabuada:\n")
x1 = int(input("Digite o número: "))
for num1 in range(11):
    print(f"{x1} * {num1} é igual à:", x1 * num1)


for i in range(1, 11):
    print(f"\nTabuada do {i}:")
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# Criar um menu de oções com 4 itens 
#Exemplo: Escolher séries, aprensente sua escolha da séries das outras três
# Qualquer opção diferente sair do menu

opção = ""
print("Assista um filme!")
print("Drama = 1")
print("Suspense = 2")
print("Ação = 3")
print("Romance = 4")

while opção !="sair":
    opção = input("Digite o genêro desejado ou 'sair' para fechar: ").lower()
    if opção != "1":
        print(f"Dado '{opção}', carregando filmes de drama")
    if opção != "sair":
        print(f"Dado '{opção}' registrado no banco de dados")

print("Sistema encerrado.")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

opção = ""
print("Assista um filme!")
print("Drama = 1")
print("Suspense = 2")
print("Ação = 3")
print("Romance = 4")

while opção != "sair" and "1" and "2" and "3" and "4":
    opção = input("Digite o genêro desejado ou 'sair' para fechar: ").lower()
    if opção == "1":
        print(f"Dado '{opção}', carregando filmes de drama")
        break
    elif opção == "2":
        print(f"Dado '{opção}', carregando filmes de suspense")
        break
    elif opção == "3":
        print(f"Dado '{opção}', carregando filmes de ação")
        break
    elif opção == "4":
        print(f"Dado '{opção}', carregando filmes de romance")
        break
    elif opção == "sair":
        print(f"Dado '{opção}' registrado no banco de dados")
print("Sistema encerrado.")
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
