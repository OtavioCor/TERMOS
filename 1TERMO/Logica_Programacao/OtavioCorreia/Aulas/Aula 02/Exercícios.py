
# Apresente as mensagens
# O programa deve permitir que você digite seu nome, seu curso e sua idade e também seu hobbie

x1 = input("Qual seu nome? \n")
x2 = input("Qual seu curso? \n")
x3 = float(input("Qual sua idade? \n"))
x4 = input("Qual seu hobbie? \n")
print("\n Seu nome é", x1 + "\n Você cursa", x2 + "\n Você tem", x3, "anos" + "\n Você tem", x4, "como hobbie")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# Calculadora de IMC (Potência e Divisão)
# O índice de Massa Corporal (IMC) é calculado dividindo peso pela altura ao quadrado
print("\nSeja bem vindo a nossa Calculadora de IMC")
peso = float(input("Digite seu peso\n"))
altura = float(input("Digite sua altura\n"))
IMC = peso / altura**2
print("Seu IMC é:", IMC)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

n1 = float(input("\nDigite o primeiro número:"))
n2 = float(input("Digite o segundo número:"))
adição = n1 + n2
subtração = n1 - n2
multiplicação = n1 * n2
divisão = n1 / n2
print("\n A soma resultou:", str(adição) + "\n A subtração resultou:", str(subtração) + "\n A multiplicação resultou:", str(multiplicação) + "\n A divisão resultou:", str(divisão))

#Converter em sring
#adição = n1 + n2
#print("A some é", str(adição))

z1 = float(input("\nDigite o primeiro número:"))
z2 = float(input("Digite o segundo número:"))
print(" A soma resultou:", z1 + z2)
print(" A subtração resultou:", z1 - z2) 
print(" A multiplicação resultou:", z1 * z2) 
print(" A divisão resultou:", z1 / z2)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# Sugiro Supermarket
#O mercado deve registrar venda de itens e um relatório de cupom fiscal no fim da compra

print("\n Bem vindo ao Sugiro Supermarket")
c = str(input("Digite a compra:"))
p = float(input("Digite o preço:"))
q = float(input("Digite a quantidade:"))
print("Sua compra foi: ", c)
print("Quantidade: ", q)
print("Total: ", p * q)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# Tabuada

p1 = float(input("\nDigite o primeiro valor para multiplicar: "))
p2 = float(input("Digite o segundo valor para multiplicar: "))
print("O resultado é:", p1* p2)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#