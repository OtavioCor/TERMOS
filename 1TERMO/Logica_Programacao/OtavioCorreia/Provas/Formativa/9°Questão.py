# Atividade 9: Orçamento de Viagem (Cálculo com float)
# Imagine que você está planejando uma viagem. O custo do hotel é de R$ 250.50 por noite e
# o custo da passagem é R$ 412.00. Calcule e exiba o custo total para uma viagem por noites.
# ● Ex: Fórmula: (custo_hotel * 3) + custo_passagem

print("Descubra o orçamento de sua viagem!")
custo = int(input("Digite quanto custa a diária: "))
noites = int(input("Digite quantas noites você ficará hospedado: "))
passag = int(input("Digite quanto custa a passagem: "))
print(f"Sua passagem custa {passag} reais, você ficará {noites} noites, com o custo de {custo} reais por noite.")
print("Custo total de sua viagem: R$", passag + (noites * custo))