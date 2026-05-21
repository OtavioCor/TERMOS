#TKINTER

# Componentes widgets
# tk - Tk() #Janela
# 1b - Label() # Rótulo
# bt - Button() # Botão
# et - Entry() # Caixa de texto

import tkinter as tk
from tkinter import messagebox

# 1 - Criar a janela principal
janela = tk.Tk()
janela.title("Minha primeira janela GUI") # Título na janela
janela.configure(bg="#E7FF9E") # Cor de fundo
janela.geometry("400x200") # Largura e altura

# 2 - Criar a função do botão (evento)
def mostrar_mensagem():
    messagebox.showinfo("Sucesso!", "Você clicou no botão")     #Se paertar o botão, acontecerá isso

# 3 - Criar os componentes
lbl_titulo = tk.Label(janela, text="Bem vindo a nossa aula de Tkinter",     # Título
bg="#E7FF9E", font=("Arial", 14, "bold"))
btn_clique=tk.Button(janela, text="Clique Aqui", font=("Arial", 11),  # Botão Clique aqui
bg="#7E8C54", fg="white", command=mostrar_mensagem)
btn_close = tk.Button(janela, text="Fechar", font= ("Arial", 14, "bold"),   # Botão fechar
bg="#7E8C54", fg="white", command=janela.destroy)       # destroy - fechar

# 4 - Posicionar Componentes
lbl_titulo.pack(pady=10) # 'pady' adiciona um espaçamento vertical
btn_clique.pack(pady=10)
btn_close.pack(pady=5)

# 5 Rodar o loop interface
janela.mainloop()

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

import tkinter as tk
from tkinter import messagebox

def saudar_usuario():
    # .get() serve para buscar o texto que vamos digitar

    nome = campo_nome.get()

    if nome == "":
        messagebox.showwarning("Aviso", "Por favor, digite seu nome!")
    else:
        messagebox.showinfo("Saudades Alunos", f"olá, {nome}! Seja bem-vindo ao mundo das interfaces gráficas")

# Configurações da janela
app = tk.Tk()
app.title("Exemplo 1")
app.geometry("350x200")

# Componentes
lbl_instrucao = tk.Label(app, text="Digite seu nome abaixo: ")
lbl_instrucao.pack(pady=10)

campo_nome = tk.Entry(app, font=("Arial", 12))      #Para escrever
campo_nome.pack(pady=5)

btn_enviar = tk.Button(app, text="Enviar", command=saudar_usuario)
btn_enviar.pack(pady=15)

app.mainloop()

# Crie uma interface gráfica que calcule a média de três notas digitadas pelo usuário. 
# A interface deve conter campos para o usuário inserir as notas e um botão para calcular a média.
# Ao clicarno botão, a média deve ser exibida em uma mensagem