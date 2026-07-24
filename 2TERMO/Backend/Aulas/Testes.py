
numeros = [12, 5, 8, 21, 14, 3, 10, 7]
pares = []

for num in numeros:
    if num % 2 == 0:
        pares.append(num)
    
media = sum(pares) / len(pares) # len conta quantos números tem na lista ## sum para somar os números da lista
qtd = len(pares)
print("Pares:", pares)
print("Quantidade de numéros pares: ",qtd)
print("Média: ", media)
