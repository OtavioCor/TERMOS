# Atividade 7: Cálculo de Eficiência (OEE)
# ● Peça a quantidade de peças produzidas e a quantidade de peças defeituosas. Calcule
# e exiba a taxa de aproveitamento (peças boas / total).

print("Descubra a taxa de aproveitamento de sua produção!")
total = int(input("Digite a quantidade de peças produzidas: "))
ruim = int(input("Digite a quantidade de peças defeituosas: "))
taxa= ruim / total
print(f"De {total} peças, {ruim} foram defeituosas.")
print("A taxa proporcional é: ",taxa)
