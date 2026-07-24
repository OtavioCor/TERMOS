#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# Tente criar um código que conte de 1 a 10, mas use o continue para não imprimir o número 5
# (Simulando uma falha de sensor específica no item 5).

print("Contando de 1 a 10")
for num in range(1, 11):
    if num != 5:
         print(f"Número: {num}")
         continue
    print("Número 5 não detectado")

###

print("Contando de 1 a 10")
from time import sleep
for i in range(1, 11):
     if i == 5:
          print(f"Falha ao leo o nº {i}")
          sleep(1.8)
          continue
     print(i)
     sleep(0.7)
print("Acabou")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# Simule um semáforo com parada prar cada cor.
# Determine um tempo que deseja para que quando mudar para tal cor ele represente uma pausa

from time import sleep
print("Escolha a cor do semaforo\n")
print("1 = Verde")
print("2 = Amarelo")
print("3 = Vermelho")
s1 = float(input("Digite o número: "))
if s1 == 1:
        print("Cor verde acessa")
        for i in range(1, 10):
             print(i)    
             sleep(1)
        print("Cor verde apagada")
if s1 == 2:
        print("Cor amarela acessa")
        for i in range(1, 6):
             print(i)    
             sleep(1)
        print("Cor amarela apagada")
if s1 == 3:
        print("Cor vermelha acessa")
        for i in range(1, 8):
             print(i)    
             sleep(1)
        print("Cor vermelha apagada")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# Soma de Cargas de energia (for)
# Uma fábrica tem 5 máquinas. Peça ao usuário (via input dentro do loop) o consumo em kWh de cada uma das 5 máquinas. 
# Ao final do loop, o programa deve exibir o consumo total da fábrica.
total = 0
for maq in range(1, 6):
    print(f"{maq}ª máquina:")
    consumo = int(input("Digite seu consumo em kWh: "))
    total += consumo

print("O consumo total: ", total)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# Percorra uma lista de medidas de peças:
# medidas = [50.1, 49.8, 52.0, 50.0, 48,5].
# O padrão de qualidade aceita apenas peças com exatamente 50.0 ou mais.
# Use um for para ler a lista e, para cada peça, diga se ela está "Aprovada" ou "Rejeitada".

medidas = [50.1, 49.8, 52.0, 50.0, 48.5]
for med in medidas:
      if med >= 50:
            print(f"Peça com medida {med} Aprovada")
      else:
            print(f"Peça com medida {med} Reprovada")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# Uma balança industrial está pesando um lote de 6 sacos de insumos. 
# O peso ideal de cada saco é 50kg, mas o sistema aceita variações.

for saco in range(1, 7):
    print(f"\n{saco}ª saco de insumo:")
    peso = int(input("\nDigite o peso em Kg: "))
    if peso > 50:
          print(f"{peso}Kg, está com {peso - 50}Kg a mais")
    if peso < 50:
          print(f"{peso}Kg, está com {50 - peso}Kg a menos")
    if peso == 50:
          print(f"{peso}Kg, está com o peso ideal")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# Sistema inteligente de manutenção
# Crie um programa que receba dois dados: a pressão atual (float) e as horas de uso acumuladas (int) de uma turbina.
# O programa deve classificar o estado da máquina seguindo esta hierarquia
# Crítico (Prioridade 1): Se a pressão for maior que 100 OU as horas de uso forem maiores que 10.000
# Mensagem: "PARADA IMEDIATA: Risco de falha catastrófica"
# Alerta (Prioridade 2): Se a pressão estiver entre 80 e 100(inclusive).
# Mensagem: "MANUTENÇÃO AGENDADA: Pressão acido do ideal."
# Monitoramento (Prioridade 3): Se as horas de uso forem entre 8.000 e 10.000.
# Mensagem: "AVISO: Máquina aproximando-se da revisão de 10k horas."
# Normal: Para qualquer outro caso que não se encaixe nos acima.
# Mensagem: "SISTEMA OPERAL: Todos os parâmetros dentro da normalidade"

p1 = float(input("Pressão atual: "))
p2 = int(input("Horas de uso: "))

if p1 > 100 or p2 > 10000:
      print("PARADA IMEDIATA: Risco de falha catastrófica")
elif p1 > 80 and p1 < 100:
      print("MANUTENÇÃO AGENDADA: Pressão acido do ideal.")
elif p2 > 8000 and p2 < 10000:
      print("AVISO: Máquina aproximando-se da revisão de 10k horas.")
else:
      print("SISTEMA OPERAL: Todos os parâmetros dentro da normalidade")