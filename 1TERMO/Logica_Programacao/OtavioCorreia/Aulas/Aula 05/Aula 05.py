# O laço 'for' (Repetições Determinadas)
# Use o 'for' Quando você sabe exatamente quantas vezes algo deve acontecer (como ler 10 sensores ou precessar uma lista de peças).

# Relatório de Produção Diária
# Imagine que você tem uma meta de produzir 5 lotes e quer numerar cada um:

# Exemplo 1
for lote in range(1, 6):
    print(f"Processando lote número {lote}...")
    print("Qualidade verificada. [OK]")
    print("Produção do dia finalizada!")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

#  Imagine que você queira armazanar 10 carros
for carros in range(10):
    print(f"Quantidade de carros {carros}")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# Exemplo 2
for i in range(5):
    print(i)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    
# Exemplo 3
peças = {"Engrenagem", "Eixo", "Rolamento", "Parafuso"}
maquinas = ["Máquina 1", "Máquina 2"]

for item in peças:
    print(f"Item em estoque: {item}")
    for maq in maquinas:
        print(f"Máquinas que temos {maq}")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# O laço while (Repetições Indeterminadas)
# Use o while quando você não sabe quando vai parar. Ele deoende de uma condição (como um sensor de segurança ou um botão de emergência)
# Monitor da Temperatura (Loop Infinito Controlado)

# Repete enquanto a temperatura estiver segura
temperatura = 25
while temperatura < 40:
    print(f"Temperatura atual: {temperatura}°C. Sistema operando...")
    temperatura += 3 #Simulando o aquecimento da máquina
print("ALERTA! Temperatura atingiu o limite. Desligando motor...")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# Menu de Interação
opção = ""

while opção !="sair":
    opção = input("Digite a leitura do sensor ou 'sair' para fechar: ").lower()
    if opção != "sair":
        print(f"Dado '{opção}' registrado no banco de dados")
print("Sistema encerrado.")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

