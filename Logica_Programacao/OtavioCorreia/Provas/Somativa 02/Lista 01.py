
#1. Registro de Operador: Peça o nome do operador e o turno (A, B ou C). Exiba:
#"Operador [Nome] registrado no Turno [Turno]. Boa jornada!"

import tkinter as tk
from tkinter import messagebox, ttk

janela = tk.Tk()
janela.title("Registro de Operador")
janela.geometry("400x400")
janela.configure(bg="#E7FF9E")

def operador():
    nome = ent_nome.get()
    turno = cmb_turno.get()
    if nome == "" and turno == "":
        messagebox.showwarning("Bem-Vindo", "Digite seu nome e selecione seu turno")
    else:
        messagebox.showinfo("Bem vindo", f"Operador {nome} registrado no Turno {turno}. Boa jornada!")
    

lbl_nome = tk.Label(janela, text = "Digite seu nome:",
                            font = ("Arial", 14))
lbl_nome.grid(row = 0, column = 0, pady = 10, padx = 10)

ent_nome = tk.Entry(janela,
                            font = ("Arial", 14))
ent_nome.grid(row = 0, column = 1, pady = 10, padx = 10)


lbl_turno = tk.Label(janela, text = "Selecione seu turno",
                            font = ("Arial", 14))
lbl_turno.grid(row = 2, column = 0, pady = 10, padx = 10)

cmb_turno = ttk.Combobox(janela, values = ["A", "B", "C"],
                               width = 10, font = ("Arial", 14), state = "readonly") 
cmb_turno.grid(row = 2 ,column = 1, pady = 10, padx = 10)

btn_realizar_cadastro = tk.Button(janela, text = "Cadastrar",
                                  font = ("Arial", 14), fg = "green", command = operador)
btn_realizar_cadastro.grid(row = 3 ,column = 1, pady = 10, padx = 10)

janela.mainloop()

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# 2. Cálculo de Produção: Peça a quantidade de peças produzidas em 1 hora. Calcule e
# exiba quantas peças serão produzidas em um turno de 8 horas.

import tkinter as tk
from tkinter import messagebox, ttk

janela = tk.Tk()
janela.title("Calculo de Produção")
janela.geometry("450x200")
janela.configure(bg="#E7FF9E")

def calculo():
    peca = int(ent_peca.get())
    if peca == "":
        messagebox.showwarning("Bem-Vindo", "Digite a quantidade de peças produzidas em 1 hora, para descobrir quantas serão produzidas em 8 horas.")
    else:
        messagebox.showinfo("Bem vindo", f"Em 8 horas serão produzidas: {peca* 8}")


lbl_peca = tk.Label(janela, text = "Digite quantas peças são produzidas em 1 hora",
                            font = ("Arial", 14))
lbl_peca.grid(row = 0, column = 0, pady = 10, padx = 10)

ent_peca = tk.Entry(janela,
                            font = ("Arial", 14))
ent_peca.grid(row = 1, column = 0, pady = 10, padx = 10)


btn_calculo = tk.Button(janela, text = "Calcular", font = ("Arial", 14), command=calculo)
btn_calculo.grid(row = 2, column = 0, pady = 10, padx = 10)

janela.mainloop()   

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

#3.Conversor de Unidade: O sistema lê uma pressão em Bar. Converta para PSI (1 Bar≈ 14.5 PSI) e exiba com duas casas decimais.
import tkinter as tk
from tkinter import messagebox, ttk 

janela = tk.Tk()
janela.title("Conversor de Unidade")    
janela.geometry("450x200")
janela.configure(bg="#E7FF9E")

def conversor():
    bar = float(ent_bar.get())
    if bar == "":
        messagebox.showwarning("Bem-Vindo", "Digite a pressão em Bar para converter para PSI.")
    else:
        psi = bar * 14.5
        messagebox.showinfo("Bem vindo", f"A pressão convertida para PSI é: {psi:.2f} PSI")
        
lbl_bar = tk.Label(janela, text = "Digite a pressão em Bar",
                            font = ("Arial", 14))
lbl_bar.grid(row = 0, column = 0, pady = 10, padx = 10)

ent_bar = tk.Entry(janela,
                            font = ("Arial", 14))
ent_bar.grid(row = 1, column = 0, pady = 10, padx = 10)

btn_conversor = tk.Button(janela, text = "Converter", font = ("Arial", 14), command=conversor)
btn_conversor.grid(row = 2, column = 0, pady = 10, padx = 10)

janela.mainloop()

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# 4. Média de Qualidade: Peça 3 notas de inspeção de uma peça (0 a 10). Exiba a média aritmética simples delas.

import tkinter as tk
from tkinter import messagebox
    
janela = tk.Tk()
janela.title("Calcule sua média") 
janela.configure(bg="#E7FF9E") 
janela.geometry("400x250")

def calculo():
    num1 = float(primeira_media.get())
    num2 = float(segunda_media.get())
    num3 = float(terceira_media.get())

    messagebox.showinfo("Resultado", f"A média das notas é: {(num1 + num2 + num3) / 3:.2f}") 
     

lbl_calculo = tk.Label(janela, text="Digite a 1ª nota: ", bg="#E7FF9E")
lbl_calculo.pack(pady=7)
primeira_media = tk.Entry(janela, font=("Arial", 10))
primeira_media.pack(pady=2)


lbl_calculo = tk.Label(janela, text="Digite a 2ª nota: ", bg="#E7FF9E")
lbl_calculo.pack(pady=7)
segunda_media = tk.Entry(janela, font=("Arial", 10))
segunda_media.pack(pady=2)


lbl_calculo = tk.Label(janela, text="Digite a 3ª nota: ", bg="#E7FF9E")
lbl_calculo.pack(pady=7)
terceira_media = tk.Entry(janela, font=("Arial", 10))
terceira_media.pack(pady=2)


btn_calcular=tk.Button(janela, text="Calcular", font=("Arial", 11),  
bg="#7E8C54", fg="white", command=calculo)
btn_calcular.pack(pady=17)

janela.mainloop()

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# 5. Termostato Inteligente: Peça a temperatura de um motor.
# ● Abaixo de 40°C: "Baixa carga".  
# ● Entre 40°C e 70°C: "Normal".
# ● Acima de 70°C: "ALERTA: Resfriamento Ativado!".

import tkinter as tk
from tkinter import messagebox
    
janela = tk.Tk()
janela.title("Termostato Inteligente") 
janela.configure(bg="#E7FF9E") 
janela.geometry("400x250")

def calculo(): 
    temperatura = float(ent_temperatura.get())

    if temperatura < 40:
        messagebox.showinfo("Resultado", "Baixa carga")
    elif 40 <= temperatura <= 70:
        messagebox.showinfo("Resultado", "Normal")
    else:
        messagebox.showinfo("Resultado", "ALERTA: Resfriamento Ativado!")

lbl_calculo = tk.Label(janela, text="Digite a temperatura do motor (°C): ", font = ("Arial", 14))
lbl_calculo.grid(row = 0, column = 0, pady = 10, padx = 10)

ent_temperatura = tk.Entry(janela, font=("Arial", 10))
ent_temperatura.grid(row = 1, column = 0, pady = 10, padx = 14)

btn_calculo = tk.Button(janela, text = "Calcular", font = ("Arial", 14), command=calculo)
btn_calculo.grid(row = 2, column = 0, pady = 10, padx = 10)

janela.mainloop()

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

#6. Classificador de Lotes: O usuário insere o código do produto. Se começar com "A", exiba "Alimentos". Se "E", "Eletrônicos". Para qualquer outro, "Desconhecido".

import tkinter as tk
from tkinter import messagebox      

