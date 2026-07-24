#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def saudação(nome):
    return f"Olá, {nome}!"
mensagem = saudação("Sugiro")
print(mensagem)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

nome = input("Seu nome: ")
idade = int(input("Sua idade: ")) #Converte texto para inteiro
print(f"{nome} tem {idade} anos")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

#Sem round = 93.666666666666666666666666
#Com round = 93.6

def boas_vindas(nome,cargo):
    print(f"\nOlá, {nome}! Você é o novo {cargo}.")
    
boas_vindas("Ana", "desenvolvedora")
boas_vindas("Carlos", "Gerente")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def configurar_conexão(servidor, porta=8080):
    print(f"Coectando a {servidor} na porta {porta}...")

configurar_conexão("192.168.1.1")   #Usa a porta 8080
configurar_conexão("10.0.0.1",3000) #Usa a porta 3000
configurar_conexão("192.168.1.2",)
configurar_conexão("10.0.0.1",3001)