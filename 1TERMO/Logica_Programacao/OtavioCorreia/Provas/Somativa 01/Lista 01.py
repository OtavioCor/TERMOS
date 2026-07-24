#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# Atividade 01
# Registro de Operador: Peça o nome do operador e o turno (A, B ou C). Exiba:
# "Operador [Nome] registrado no Turno [Turno]. Boa jornada!"

print("Registro de Operador")
n1 = input("Digite seu nome: ")
n2 = input("Digite seu turno: ")
print(f"Operador {n1} registrado no Turno {n2}.\nBoa jornada!")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# Atividade 02
# Cálculo de Produção: Peça a quantidade de peças produzidas em 1 hora. Calcule e
# exiba quantas peças serão produzidas em um turno de 8 horas.

print("Cálculo de Produção")
p1 = int(input("Digite a quantidade de peças produzidas em 1 hora: "))
print(f"Se em 1 hora foi produzido {p1} peças\nEm 8 horas será produzido {p1 * 8} peças")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# Atividade 03
# Conversor de Unidade: O sistema lê uma pressão em Bar. Converta para PSI (1 Bar
# ≈ 14.5 PSI) e exiba com duas casas decimais.
print("Conversor de Bar para PSI")
b1 = float(input("Digite o valor da pressão em Bar: "))
psi = b1 * 14.5
print(f"A pressão {b1}Bar em PSI será: {round(psi,2)}PSI")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# Atividade 04
# Média de Qualidade: Peça 3 notas de inspeção de uma peça (0 a 10). Exiba a média
# aritmética simples delas.
print("Média de Qualidade")
a = int(input("Digite a nota entre 0 a 10 da primeira inspeção: "))
b = int(input("Digite a nota entre 0 a 10 da segunda inspeção: "))
c = int(input("Digite a nota entre 0 a 10 da terceira inspeção: "))

print("A média das notas das inspeções é: ", (a + b + c) / 3)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# Atividade 05
# Termostato Inteligente: Peça a temperatura de um motor.
# ● Abaixo de 40°C: "Baixa carga".
# ● Entre 40°C e 70°C: "Normal".
# ● Acima de 70°C: "ALERTA: Resfriamento Ativado!".
print("Termostato Inteligente")
temp = int(input("Digite o valor da temperatura do motor: "))

if temp < 40:
    print("Baixa carga")
if temp >= 40 and temp <=70:
    print("Normal")
if temp > 70:
    print("ALERTA: Resfriamento Ativado!")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# Atividade 06
# Classificador de Lotes: O usuário insere o código do produto. Se começar com "A",
# exiba "Alimentos". Se "E", "Eletrônicos". Para qualquer outro, "Desconhecido".
print("Classificador de Lotes")
print("Eletrônicos = E")
print("Alimentos = A")
c = input("Insira o código do produto: ")
if c == "E":
    print("Produto classificado como eletrônico")
elif c == "A":
    print("Produto classificado como alimentos")
else:
    print("Desconhecido")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# Atividade 07
# Segurança de Operação: A máquina só liga se o sensor_porta == "fechada" E o
# botao_emergencia == "desligado". Peça esses dois inputs e diga se a máquina pode
# iniciar.
print("Segurança de Operação")
print("Digite apenas SIM ou NÃO")
sp = (input("O sensor da porta está fechado? "))
be = (input("O botão de emergência está desligado? "))
if sp == "SIM" and be == "SIM":
    print("Máquina pronta para iniciar")
elif sp == "SIM" and be == "NÃO":
    print("Desligue o botão de emergência para a máquina poder iniciar")
elif sp == "NÃO" and be == "SIM":
    print("Feche o sensor da porta para a máquina poder iniciar")
else:
    print("Desconhecido")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# Atividade 08
# Cálculo de Descarte: Peça o total de peças produzidas e o total de defeituosas. 
# Se o descarte for maior que 5% do total, exiba "Revisar Processo", caso contrário,
# "Processo Otimizado".

print("Cálculo de Descarte")
pt = int(input("Digite o total de peças produzidas: "))
pd = int(input("Digite o total de peças defeituosas: "))

if pd > (pt * 5 / 100):
    print("Revisar Processo")
else:
    print("Processo Otimizado")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# Atividade 09
# Validação de Medida: Uma peça deve ter entre 9.8mm e 10.2mm. Peça a medida e
# diga se está dentro da tolerância, acima ou abaixo.

print("Validação de Medida")
t = float(input("Digite a medida da peça: "))
if t >= 9.8 and t <= 10.2:
    print("Dentro da tolerância")
elif t < 9.8:
    print("Abaixo da tolerância")
elif t > 10.2:
    print("Acima da tolerância")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# Atividade 10
# Contagem Regressiva de Setup: Use um for para fazer uma contagem regressiva
# de 10 até 1 para o início de uma prensa, e finalize com "Prensa Ativada!".
import time
for num in range (10, 0, -1):
    print(num)
    time.sleep(1.0)
print("Prensa Ativada!")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# Atividade 11
# Soma de Produção (Acumulador): Use um while para pedir o peso de várias caixas.
# O loop para quando o usuário digitar 0. No fim, mostre o peso total acumulado.

print("Soma de produção")
es = 0

while True:
    ps = int(input("Digite o peso em Kg da caixa: "))
    if ps > 0:
        es += ps
    else:
        break

print (f"{es}Kg é o peso total acumulado de todas as caixas")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# Atividade 12
# Múltiplas Leituras: Use um for para pedir a temperatura de 5 sensores diferentes.
# Ao final, mostre qual foi a maior temperatura lida.

total = 0
for temp in range (1, 6):
    a = int(input(f"Digite a temperatura do {temp}º sensor: "))
    if a > total:
        total = a
print(f"{total}°C foi a maior temperatura registrada")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# Atividade 13
# Painel de Login: Crie um while que peça a senha do supervisor ("admin123").
# Enquanto ele errar, o programa diz "Acesso Negado". Ele tem apenas 3 tentativas.
# Se esgotar, exiba "Painel Bloqueado".
senha1 = 0
while senha1 < 3:
    senha = input("Digite a senha: ")
    if senha == "admin123":
        print("Acesso aprovado")
        break
    elif senha != "admin123":
        print("Acesso Negado")
        senha1 += 1
    if senha1 == 3:
        print("Painel Bloqueado")
        break

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# Atividade 14
# Simulador de Estoque: Comece com estoque = 100. Crie um menu (while) onde o
# usuário pode: (1) Adicionar itens, (2) Remover itens ou (3) Sair. Se o estoque ficar
# abaixo de 10, avise: "Estoque Crítico!".

print("Estoque")
estoque = 100
print("MENU")
print("(1) Adicionar itens")
print("(2) Remover itens")
print("(3) Sair")
while True:
    a = input("Digite a opção desejada: ")
    if a == "1":
        v1 = int(input("Digite quanto deseja adicionar: "))
        estoque += v1
    if a == "2":
        v2 = int(input("Digite quanto deseja remover: "))
        estoque -= v2
    if a == "3":
        print ("Sair")
        break 
    if estoque < 10:
        print("Estoque Crítico!")


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# Atividade 15
# Relatório de Turno Completo: Use um for para processar 5 peças. Para cada peça,
# peça o diâmetro. Se a peça for aprovada (entre 19.9 e 20.1), conte-a. No final do
# loop, exiba o total de peças aprovadas e a porcentagem de eficiência do lote.

aprovadas = 0

for peç in range(1, 6):
    a = float(input(f"Digite o diametro da {peç}ª peça: "))
    if a >= 19.9 and a <= 20.1:
        aprovadas += 1

print (f"{aprovadas} peças foram aprovadas no total")
print ("porcentagem de eficiência do estoque: ", aprovadas * 100 / 5)

