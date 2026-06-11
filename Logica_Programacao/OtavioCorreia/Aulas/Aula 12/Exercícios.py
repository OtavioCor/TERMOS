# Exercício - Crie uma aplicação que faça o calculo de idade de pessoas
# Deve perguntar o nome da pessoa e o ano de nascimento

import tkinter as tk
from tkinter import messagebox, ttk

janela = tk.Tk()
janela.title("Calculo de idade")
janela.geometry("450x150")
janela.configure(bg ="#7E8C54")

def calculo():
    try:
        nome = ent_nome.get()
        ano = int(ent_ano.get())

        if nome == "":
            messagebox.showwarning("Bem-Vindo", "Digite seu nome e sua idade")
        else:
            messagebox.showinfo("Bem-Vindo", f"Olá {nome}! Você tem {2026 - ano} anos")
    except ValueError:
        messagebox.showwarning("Bem-Vindo", "Digite seu nome e sua idade")
        
        

lbl_nome = tk.Label(janela, text = "Digite seu nome:", font = ("Arial", 14))
lbl_nome.grid(row = 0, column = 0, pady = 10, padx = 10)

ent_nome = tk.Entry(janela, font = ("Arial", 14))
ent_nome.grid(row = 0, column = 1, pady = 10, padx = 10)

lbl_ano = tk.Label(janela, text = "Ano de nascimento:", font = ("Arial", 14))
lbl_ano.grid(row = 1, column = 0, pady = 10, padx = 10)

ent_ano = tk.Entry(janela, font = ("Arial", 14))
ent_ano.grid(row = 1, column = 1, pady = 10, padx = 10)

btn_calculo = tk.Button(janela, text = "Calcular", font = ("Arial", 14), command=calculo)
btn_calculo.grid(row = 2, column = 1, pady = 10, padx = 10)

janela.mainloop()