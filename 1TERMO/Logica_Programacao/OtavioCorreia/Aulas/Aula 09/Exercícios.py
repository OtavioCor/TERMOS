# Projeto Cancela Automática
# Criar um algoritmo que consiga gerenciar entrada e saída de veículos, inserindo valores por hora permanecida.
# A forma de entrafa e saída deve ser especificada e permitir o usuário inserir os dados necessários para registro do veículo

# 1 - Pressionar botão, imprimiu um ticket
# Calcular tempo de permanência
# Pagar o tecket
# Devolver ticket na saída
# Liberar e fechar cancelas

# 2 - Acesso por TAGs (Sem parar, Connect Car...)
# Calcular tempo de permanência
# Gerar pagamento em fatura
# Liberar e fechar cancelas

# Erros 
# Verificar sinal de transmissão da TAG
# Verificar acesso por ticket ou tag ao mesmo tempo
# Perdeu ticket (levantar informações)
# Problemas com cancela
from time import sleep
while True:
    print("😁 Bem vindo ao Sugiro Shopping 😁")
    print("R$ 4,50 por hora 💸")
    print("1 = Ticket 🎟️")
    print("2 = TAG 🛜")
    opcao = int(input("Digite o que deseja: "))
    if opcao == 1:
        Horario_entrada = float(input("Digite o horário de entrada: "))
        print("Ticket liberado...")
        sleep(0.7)
        print("Cancela aberta...")
        sleep(0.7)
        print("Carro passando...")
        sleep(1.7)
        print("Cancela fechada...")
        while True:
            perda = str(input("Ocorreu a perda do ticket? (Sim ou Não): "))
            if perda == "Não":
                print("Inserir ticket...")
                sleep(0.5)
                Horario_saida = float(input("Digite o horário de saída: "))
                Total = Horario_saida - Horario_entrada
                print("Processando relatório...")
                sleep(2.0)
                print("========================================".center(40))
                print("Relatório".center(40))
                print("========================================".center(40))
                print(f"Permanência no estacionamento: {Total:.2f} horas".center(40))
                print(f"Custo total: {Total * 4.50:.2f}".center(40))
                print("========================================".center(40))
                break
            elif perda == "Sim":
                print("Registre")
                str(input("Nome Completo: "))
                int(input("Idade: "))
                int(input("CPF: "))
                str(input("Documenção do carro: "))
                sleep(0.5)
                Horario_saida = float(input("Digite o horário de saída: "))
                Total = Horario_saida - Horario_entrada
                print("Processando relatório...")
                sleep(2.0)
                print("========================================".center(40))
                print("Relatório".center(40))
                print("========================================".center(40))
                print(f"Permanência no estacionamento: {Total:.2f} horas".center(40))
                print("Multa: R$50.00".center(40))
                print(f"Custo total: R${Total * 4.50 + 50:.2f}".center(40))
                print("========================================".center(40))
                break
            else:
                print("Opção não encontrada, digite novamente")
        sleep(0.7)
        print("Volte sempre 😊")
        sleep(1.8)
        print("Cancela aberta")
        sleep(0.7)
        print("Carro passando...")
        sleep(1.7)
        print("Cancela fechada\n")
        sleep(3.0)
    elif opcao == 2:
        Horario_entrada = float(input("Digite o horário de entrada: "))
        print("Cancela aberta")
        sleep(0.7)
        print("Carro passando...")
        sleep(1.7)
        print("Cancela fechada")
        Horario_saida = float(input("Digite o horário de saída: "))
        Total = Horario_saida - Horario_entrada
        print("Processando relatório...")
        sleep(2.0)
        print("========================================".center(40))
        print("Relatório".center(40))
        print("========================================".center(40))
        print(f"Permanência no estacionamento: {Total:.2f} horas".center(40))
        print(f"Custo total: {Total * 4.50:.2f}".center(40))
        print("========================================".center(40))
        sleep(0.7)
        print("Volte sempre 😊")
        sleep(1.8)
        print("Cancela aberta")
        sleep(0.7)
        print("Carro passando...")
        sleep(1.7)
        print("Cancela fechada\n")
        sleep(3.0)
    else:
        print("Problema com cancela 😒")
        print("Pague manualmente")
        break
