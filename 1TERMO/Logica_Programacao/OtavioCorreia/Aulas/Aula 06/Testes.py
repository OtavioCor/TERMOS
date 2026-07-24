
p1 = float(input("Pressão atual: "))
p2 = int(input("Horas de uso: "))

if p1 > 100 or p2 > 10000:
      print("PARADA IMEDIATA: Risco de falha catastrófica")
if p1 > 80 and p1 < 100:
      print("MANUTENÇÃO AGENDADA: Pressão acido do ideal.")
if p2 > 8000 and p2 < 10000:
      print("AVISO: Máquina aproximando-se da revisão de 10k horas.")
else:
      print("SISTEMA OPERAL: Todos os parâmetros dentro da normalidade")