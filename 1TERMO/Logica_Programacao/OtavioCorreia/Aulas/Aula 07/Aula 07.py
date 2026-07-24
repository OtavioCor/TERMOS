# Clean Code - Aula 8
# Para que usar?
# Como usar?
print("Clean Code - Aula 8")
aula = 8
print(f"Estamos na aula {aula} de Clean Code")

# Manipulação de arquivos e Texto
# strip = Retira o espaço das aspas
# upper = Letra maiúscula
# lower = Letra minúscula

texto = " python é muito legal"
print(texto.strip().upper()) # "PYTHON É MUITO LEGAL"
print(texto.strip().lower()) # "python é muito legal"
print(texto.strip().capitalize()) # "Python é muito legal"
print(texto.strip().title()) # "Python É Muito Legal"
print(texto.strip().replace(" ", "_")) # "Python_é_muito_legal"
print(texto.strip().split()) # ['Python', 'é', 'muito', 'legal']
print(texto) # " Python "

# Escrevendo
with open("notas.txt", "w") as arquivo:  #Write = armazena informação  ## Arquivo = variável ### .txt para criar um novo file apenas de texto
    arquivo.write("Estudar Python hoje!")
    arquivo.write("\nLer sobre Clean Code")

# Lendo
with open("notas.txt", "r") as arquivo:  #Read = Escreve a informação armazenada
    conteudo = arquivo.read()
    print(conteudo)

# Execução de comandos do sistema
import os # importa o módulo os para interagir com o sistema

# Onde estou?
print(os.getcwd())

# Listar arquivos na pasta
print(os.listdir())
print(os.listdir("..")) # Lista arquivos da pasta pai
print(os.listdir("..\\..")) # Lista arquivos da pasta âvo
print(os.listdir("C:\\")) # Lista arquivos da raiz do C
print(os.listdir("C:\\Users")) # Lista arquivos da pasta Users
print(os.listdir("C:\\Users\\Public")) # Lista arquivos da pasta Public

# # Outros comandos úteis:
# # Criar pasta
os.mkdir("nova_pasta")
# # # Renomear pasta
os.rename("nova_pasta", "pasta_renomeada")
# # # Excluir pasta
os.rmdir("pasta_renomeada")
