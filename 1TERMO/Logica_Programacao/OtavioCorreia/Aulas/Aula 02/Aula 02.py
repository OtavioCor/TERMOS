# Funções

#Variáveis são formas de armazenar informação
a = 1  # a é uma variável
b = 2
c = a + b 
print('O valor de A e B é:', c)

#Função Input
#Irá permitir inserir informações
input("Qual é seu nome?")

# Operações matematicas
# + = soma
# - = subtração
# * = multiplicação
# / = divisão

# '' = srt
# "" = numeros

#\n = Manda para linha de baixo / quebra a linha

#Exemplo 1
v1 = input("Digite o primeiro valor: \n")
v2 = input("Digite o segundo valor: \n")
vtotal = v1 + v2
print("Qual é o resultado?", vtotal)

# - Para números inteiros: int
# - Para números decimais: float

#Exemplo 2
x1 = int(input('Digite o primeiro valor da subtração: \n'))
x2 = int(input('Digite o segundo valor da subtração: \n'))
xtotal= x1 - x2
print('Qual é o valor do X: \n', xtotal)

#Exemplo 3 e 4 (Multiplicação e divisão)
y1 = int(input('Digite o primeiro valor da multiplicação: \n'))
y2 = int(input('Digite o segundo valor da multiplicação: \n'))
ytotal= y1 * y2
print('Qual é o valor do X: \n', ytotal)

z1 = int(input('Digite o primeiro valor da divisão: \n'))
z2 = int(input('Digite o segundo valor da divisão: \n'))
ztotal= z1 / z2
print('Qual é o valor do X: \n', ztotal)

print(' Vamos dividir \n')
d1 = float(input(" Digite o primeiro valor desejado \n"))
d2 = float(input(" Digite o segundo valor desejado \n"))
dtotal = d1 /d2
print("Sua divisão é: \n", dtotal)

#Concatenar
print('eu gosto de programar \n' + '\n Python \n')
