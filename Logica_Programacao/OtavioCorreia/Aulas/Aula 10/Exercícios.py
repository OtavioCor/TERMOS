# Contexto
# O Serviço Especializado em Engenharia de Segurança e em Medicina do Trabalho
# (SESMT) precisa automatizar o controle de treinamentos obrigatórios (como CIPA,
# Brigada de Incêndio e NR-35) e a entrega de Equipamentos de Proteção Individual (EPIs).
# Objetivo
# Desenvolva um programa em Python que gerencie o status de conformidade dos
# funcionários de uma empresa.
# Requisitos do Programa
# 1. Cadastro de Funcionários:
# ○ Armazene o nome, setor e o status dos treinamentos (NR-10, NR-35 e
# Brigada).

# 2. Verificação de EPI (NR-6):
# ○ O sistema deve receber o setor do funcionário.
# ○ Se o setor for "Elétrica", liste a obrigatoriedade de luvas de alta tensão e
# botas dielétricas.
# ○ Se o setor for "Trabalho em Altura", liste o cinturão de segurança e
# talabarte.

# 3. Alerta de Reciclagem:
# Crie uma função que receba o ano do último treinamento da Brigada de
# Incêndio.
# ○ Se o treinamento tiver mais de 2 anos, exiba a mensagem: "Treinamento
# Vencido! Encaminhar para reciclagem."
# ○ Caso contrário, exiba: "Treinamento Válido."

from time import sleep
funcionarios = []
print("Seja bem vindo ao programa de gerenciamento de status de conformidade de funcionários")
def registro():
    nome = input("\nDigite seu nome: ")
    setor = input("Digite seu setor (Mecânica, Elétrica, Trabalho em Altura, Logistitica, DEVIS): ")
   
    status = input("Digite seu status dos treinamentos (NR-10, NR-35 e brigada): ")
    ano = int(input("Digite o ano do último treinamento da Brigada de Incêndio: "))
    if (2026 - ano) > 2:
        print("Treinamento Vencido! Encaminhar para reciclagem")
        sleep(1.2)
    else:
        print("Treinamento Válido.")
        sleep(1.2)
    if setor == "Elétrica":
        print("EPIs - Luvas de alta tensão\nBotas dielétricas")
        sleep(1.2)
    elif setor == "Trabalho em Altura":
        print("EPIs - Cinturão de segurança\nTalabarte")    
        sleep(1.2)
    return nome, setor, status


while True:
    print("Menu")
    print("1. Cadastrar funcionário")
    print("2. Visualizar relatório")
    print("3. Sair")
    escolha = input("Digite o que você deseja: ")
    if escolha == "1":
        dados = registro()
        funcionarios.append(dados)
        sleep(1.2)
    elif escolha == "2":
        if not funcionarios:
            print("Nenhum registro encontrado.")
            sleep(1.2)
        else:
            for f in funcionarios:
                print(f"Nome: {f[0]} | Setor: {f[1]} | Status: {f[2]}")
                sleep(1.2)
    elif escolha == "3":
        print("Saindo...")
        break
    else:
        print("Opção inválida!")
        sleep(1.2)