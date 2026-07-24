#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# Crie um script que mostre o caminho da pasta atual
import os
print(os.getcwd())

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# Liste os arquivos da pasta atual
print(os.listdir()) 

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

#Crie uma pasta chamada "projetos" e depois renomeie para "meus_projetos". Por fim, exclua a pasta

os.mkdir("projetos")
# # # Renomear pasta
os.rename("projetos", "meus_projetos")
# # # Excluir pasta
os.rmdir("meus_projetos")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# Crie um arquivo chamado "log.txt" e escreva a mensagem "Log de atividades". Depois, leia o conteúdo do arquivo e exiba na tela

# Escrevendo
with open("log.txt", "w") as arquivo: 
    arquivo.write("Log de atividades")
with open("log.txt", "r") as arquivo:  
    conteudo = arquivo.read()
    print(conteudo)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# Crie um dicionário com informações sobre uma pessoa e acesse um valor usando uma chave
pessoa = {
    "nome": "Alice",
    "idade": 30,
    "cidade": "São Paulo",
    "profissão": "Engenharia"
}
pessoa2 = {
    "nome": "Otavio",
    "idade": 16,
    "cidade": "São Paulo",
    "profissão": "Designer"
}
print(pessoa["nome"], pessoa["idade"], pessoa["profissão"] )
print(pessoa2["nome"], pessoa2["cidade"])

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# Desligar o PC (comando para Windows)
with open("desliga.bat", "w") as desligar: # .bat para criar um novo file executável
    desligar.write("shutdown -s -t 3600 -c \"Desligamento programado para daqui a 1 hora. Salve ser trabalho!\"")
    # Comando -s para desligar
    # Comando -t tempo definir
    # Comando -a cancela desligamento
with open("desliga.bat", "r") as desligar:  
    conteudo = desligar.read()
    print(conteudo)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# Criar um arquivo de backup
# Escreva um script que crie um arquivo de backup do arquivo "notas.txt" com o nome "notas_backup.txt".
# O script deve ler o conteúdo de "notas.txt" e escrever no novo arquivo

with open("notas.txt", "r") as notas: 
    conteudo = notas.read()
with open("notas_backup.txt", "w") as backup:  
    backup.write(conteudo)
    print("Backup realizado com sucesso")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# Criar um script de limpeza de arquivos
# Escreva um script que liste os arquivos de uma pasta e exclua os arquivos com extensão ".tmp". 
# O script deve exibir uma mensagem para cada arquivo excluído.
pasta = os.listdir()
for arquivo in pasta:
    if arquivo.endswith(".txt"): #endswith = Termina com 
        os.remove(arquivo)
        print(f"Arquivo {arquivo} excluído.")
print("Limpeza de arquivos concluída")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# Criar um script de monitoramento de temperatura
# Escreva um script que monitora a temperatura de um motor. 
# O script deve ler a temperatura de um arquivo "temperatura.txt" e exibir uma mensagem de alerta se a temperatura estiver acima de 70°C

with open("temperatura.txt", "r") as arquivo: 
    temperatura = arquivo.read() 
    if temperatura > "70":
        print(f"ALERTA {temperatura}°")

