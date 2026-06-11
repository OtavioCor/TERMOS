# Atividade 10: Desafio - Mini Relatório
# Crie um script que imprima um pequeno relatório. Use print() várias vezes para formatar a
# saída de forma organizada.
# ● Exemplo de saída:

# ==========================
# Relatório de Vendas
# ==========================
# Produto: Notebook Gamer
# Quantidade vendida: 15
# Preço unitário: R$ 5499.50
# Total de vendas: R$ 82492.50
# ==========================


print ("Inicie seu relatório: ")
p = input("Digite o nome do produto: ")
q = int(input("Digite a quantidade vendida: "))
c = int(input("Digite o preço unitário: "))

print("===============================".center(31))
print("Relatório de vendas".center(31))
print("===============================".center(31))
print(f" Produto: {p}".center(31))
print(f" Quantidade vendida: {q}".center(31))
print(f" Preço unitário: R${c}".center(31))
print(f" Total de vendas: R${q * c}".center(31))
print("===============================".center(31))

