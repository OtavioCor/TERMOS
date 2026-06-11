# Revisão Tkinter

import tkinter as tk
from tkinter import messagebox, ttk

# DEF funções em bloco
def cadastrar_usuario():
    #.get
    usuario = ent_nome_usuario.get()
    curso = ent_curso.get()
    nome_escola = cmb_nome_escola.get()

    if usuario == "" and curso == "" and nome_escola == "":
        messagebox.showwarning("Bem-Vindo", "Digite seu nome, seu curso e escolha sua escola")
    else:
        messagebox.showinfo("Bem-Vindo", f"Olá {usuario}! Seu curso é {curso} e sua escola é o {nome_escola}")

# 0 - Etapa Janela

janela = tk.Tk()
janela.title("Revisão Tkinter")
janela.geometry("400x400")
janela.configure(bg="blue")

# 1 - Etapa  Componentes

# print = Label
# input = Entry

lbl_nome_usuario = tk.Label(janela, text = "Digite seu nome:",
                            font = ("Arial", 14), fg = "green", bg = "pink")
lbl_nome_usuario.grid(row = 0, column = 0, pady = 10, padx = 10) # row = linha 

ent_nome_usuario = tk.Entry(janela,
                            font = ("Arial", 14), width = 10) #width = largura
ent_nome_usuario.grid(row = 0, column = 1, pady = 10, padx = 10)

lbl_curso = tk.Label(janela, text = "Digite seu curso:",
                            font = ("Arial", 14), fg = "green", bg = "pink")
lbl_curso.grid(row = 1, column = 0, pady = 10, padx = 10)

ent_curso = tk.Entry(janela,
                            font = ("Arial", 14), width = 10) 
ent_curso.grid(row = 1, column = 1, pady = 10, padx = 10)

# ComboBox = Caixa de seleção
lbl_nome_escola = tk.Label(janela, text = "Digite sua escola:",
                            font = ("Arial", 14), fg = "green", bg = "pink")
lbl_nome_escola.grid(row = 2, column = 0, pady = 10, padx = 10)

cmb_nome_escola = ttk.Combobox(janela, values = ["SESI408", "SESI005"],
                               width = 10, font = ("Arial", 14), state = "readonly") # state = "readonly" == Para não poder escrever na caixa, apenas selecionar
cmb_nome_escola.grid(row = 2 ,column = 1, pady = 10, padx = 10)

# Botões
btn_realizar_cadastro = tk.Button(janela, text = "Cadastrar",
                                  font = ("Arial", 14), fg = "green", command = cadastrar_usuario)
btn_realizar_cadastro.grid(row = 3 ,column = 1, pady = 10, padx = 10)
btn_fechar_janela = tk.Button(janela, text = "Fechar", font = ("Arial", 14), command = janela.destroy)
btn_fechar_janela.grid(row  = 4, column = 1, pady = 10, padx = 10)
# 4 = Etapa Loop

janela.mainloop()


