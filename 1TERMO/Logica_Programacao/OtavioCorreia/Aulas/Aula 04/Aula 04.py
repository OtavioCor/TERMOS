#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# if: "Se" a condição for verdadeira.
# elif: "Senão, se" (usado para múltiplas condições)
# else "senão" (executa se nenhuma das anteriores for verdadeira)

print("Expressões lógicas")
idade = int(input("\nDigite sua idade:"))

if idade >= 18:
    print("Você é maior de idade.")
    print("Pode tirar carta de motorista.")
elif idade >= 16:
    print("Você ainda não é de maior, mas já pode votar.")
else:
    print("Você é menor de idade")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
  
print("Escolha sua modalidade?")
print("Opção 1: TI")
print("Opção 2: Humanas")
print("Opção 3: Exatas")
modalidade = input("Digite sua opção de modalidade por números")
if modalidade == 1:
    print("Você escolheu TI")
elif modalidade == 2:
    print("Você escolheu Humanas")
else:
    print("Você escolheu Exatas")
    
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

print("Categoria de Series e Fimes")
print("Escolha uma categoria")
print("Séries = S")
print("Filmes = F")
categoria = input("Digite sua categoria: ")
if categoria == "S":
    print("Sua escolha for para Séries")
elif categoria == "F":
    print("Sua escolha foi para Filmes")
else:
    print("Você não escolheu nenhuma das categorias")
    
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

print("Calculadora com condições")
print("Escolha como quer calcular")
print("1 = Soma")
print("2 = Subtração")
print("3 = Multiplicação")
print("4 = Divisão")
calculadora = float(input("Digite sua opção para calcular \n"))
if calculadora == 1:
    print("1 = Você escolheu soma")
    soma1 = int(input("Digite o primeiro valor: \n"))
    soma2 = int(input("Digite o segundo valor: \n"))
    print("O resultado é:")
    print(soma1+soma2)
elif calculadora == 2:
    print("2 = Você escolheu subtração")
    sub1 = int(input("Digite o primeiro valor: \n"))
    sub2 = int(input("Digite o segundo valor: \n"))
    print("O resultado é:")
    print(sub1-sub2)
elif calculadora == 3:
    print("3 = Você escolheu Multiplicação")
    mult1 = int(input("Digite o primeiro valor: \n"))
    mult2 = int(input("Digite o segundo valor: \n"))
    print("O resultado é:")
    print(mult1*mult2)
elif calculadora == 4:
    print("4 = Você escolheu Divisão")
    div1 = int(input("Digite o primeiro valor: \n"))
    div2 = int(input("Digite o segundo valor: \n"))
    print("O resultado é:")
    print(div1/div2)
else:
    print("Você não escolheu nenhuma opçao")
    print("Sair do programa")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
