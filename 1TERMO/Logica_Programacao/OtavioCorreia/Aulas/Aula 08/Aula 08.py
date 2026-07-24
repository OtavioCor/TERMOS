
# Tratamento de erros com python
# Erros comuns:
# - ZeroDivisionError: Divisão por zero
# - ValueError: Conversão de tipo inválida
# - IndexError: Acesso a índice fora do limite
# - KeyError: Acesso a chave inexistente em dicionário

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# - ZeroDivisionError: Divisão por zero
print("Exemplo de tratamento de erros")
try:
    num1 = int(input("Digite o primeiro número... "))
    num2 = int(input("Digite o segundo número... "))
    resultado = num1 / num2
    print(f"O resultado da divisão é: {resultado:.2f}")

except ZeroDivisionError:
    print("Erro: Não é possível dividir por zero")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# - ValueError: Conversão de tipo inválida
print("Exemplo de tratamento de erros")
try:
    num1 = int(input("Digite o primeiro número... "))
    num2 = int(input("Digite o segundo número... "))
    resultado = num1 / num2
    print(f"O resultado da divisão é: {resultado:.2f}")

except ValueError:
    print("Erro: Entrada inválida. Por favor, digite um número inteiro")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# - IndexError: Acesso a índice fora do limite
print("Exemplo de tratamento de erros")
try:
    num1 = int(input("Digite o primeiro número... "))
    num2 = int(input("Digite o segundo número... "))
    resultado = num1 / num2
    print(f"O resultado da divisão é: {resultado:.2f}")

except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

print("Exemplo de tratamento de erros")
try:
    num1 = int(input("Digite o primeiro número... "))
    num2 = int(input("Digite o segundo número... "))
    resultado = num1 / num2
    print(f"O resultado da divisão é: {resultado:.2f}")

except ZeroDivisionError:
    print("Erro: Não é possível dividir por zero")
    
except ValueError:
    print("Erro: Entrada inválida. Por favor, digite um número inteiro")

except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")

if num1 > 100:
    print("O número digitado é maior que 100.")
    for i in range(1, 6):
        print(f"{num1} x {i} = {num1 * i}")
        if num1 * i > 1000:
            print("O resultado da multiplicação é maior que 1000.")
            try:
                pass
            except Exception as e:
                print(f"Ocorreu um erro inesperado: {e}")
else:
    print("O número digitado é menor ou igual a 100.")
