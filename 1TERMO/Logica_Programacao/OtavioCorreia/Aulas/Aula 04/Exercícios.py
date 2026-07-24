#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# Criar um algoritmo para calcular a média e com base em notas
# Podemos inserir duas notas e apresente a média porem a nota base de 50 é aprovado e menor que esse valor será reprovado

print("Descubra se você foi aprovado ou reprovado\n")
p1 = float(input("Digite sua primeira nota formativa: "))
p2 = float(input("Digite sua segunda nota formativa: "))
c1 = (p1+p2)/2
if c1 >= 50:
    print("Você foi:\nAPROVADO")
else:
    print("Você foi:\nREPROVADO")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

#Criar um algoritmo para desmontar a sinalização de um semaforo
print("Escolha a cor do semaforo\n")
print("1 = Verde")
print("2 = Amarelo")
print("3 = Vermelho")
s1 = float(input("Digite o número: "))
if s1 == 1:
    print("1 = A cor do semaforo é verde")
elif s1 == 2:
    print("2 = A cor do semaforo é amarelo")
elif s1 == 3:
    print("3 = A cor do semaforo é vermelho")
else:
    print("Você não escolheu nenhuma opçao")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# Criar um algoritmo para aplicação de descontos para produtos como sapatos, aplicar 10%, para produtos como roupas, 5% e perfumes 2%
print("Bem vindo a Carlo's loja\n")
print("Escolha o produto: \n")
print("1 = Sapato")
print("2 = Roupas")
print("3 = Perfumes")
d1 = int(input("Digite o produto desejado: "))
if d1 == 1:
    print("\n1 = O produto desejado é sapato")
    print("Você recebeu 10% de desconto")
    c1 = int(input("Digite o valor da compra:\n"))
    q1 = int(input("Digite a quantidade:\n"))
    produto = q1 * c1
    desconto = produto * 10 / 100
    print("Valor bruto:", produto)
    print("Valor líquido:", produto - desconto)
elif d1 == 2:
    print("\n2 = O produto desejado é roupas")
    print("Você recebeu 5% de desconto")
    c1 = int(input("Digite o valor da compra:\n"))
    q1 = int(input("Digite a quantidade:\n"))
    produto = q1 * c1
    desconto = produto * 5 / 100
    print("Valor bruto:", produto)
    print("Valor líquido:", produto - desconto)
elif d1 == 3:
    print("\n3 = O produto desejado é perfume")
    print("Você recebeu 2% de desconto")
    c1 = int(input("Digite o valor da compra:\n"))
    q1 = int(input("Digite a quantidade:\n"))
    produto = q1 * c1
    desconto = produto * 2 / 100
    print("Valor bruto:", produto)
    print("Valor líquido:", produto - desconto)
else:
    print("Você não escolheu nenhuma opção")
print("Obrigado pela compra!")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# Criar um algoritmo para calcular a média e com base em notar, podemos inserir duas notas e apresente a média
# Porém a nota 0 a 100 para ser aprovado será acima de 70 e menor que 50 esse valor será reprovado
# Porém vamos acrescentar uma nova condição que entre 50 e 70 recuperação


print("Descubra se você foi aprovado ou reprovado\n")
p1 = float(input("Digite sua primeira nota formativa: "))
p2 = float(input("Digite sua segunda nota formativa: "))
c1 = (p1+p2)/2
print("Sua média foi: c1")
if c1 >= 70:
    print("Você foi:\nAPROVADO")
elif c1 >= 50:
    print("Você foi:\nRECUPERAÇÃO")
else:
    print("Você foi:\nREPROVADO")
