# Crie uma interface gráfica que calcule a média de três notas digitadas pelo usuário. 
# A interface deve conter campos para o usuário inserir as notas e um botão para calcular a média.
# Ao clicar no botão, a média deve ser exibida em uma mensagem

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

    messagebox.showinfo("Resultado", (num1 + num2 + num3) / 3) 
     
# Primeira nota
lbl_calculo = tk.Label(janela, text="Digite a 1ª nota: ", bg="#E7FF9E")
lbl_calculo.pack(pady=7)
primeira_media = tk.Entry(janela, font=("Arial", 10))
primeira_media.pack(pady=2)

# Segunda nota
lbl_calculo = tk.Label(janela, text="Digite a 2ª nota: ", bg="#E7FF9E")
lbl_calculo.pack(pady=7)
segunda_media = tk.Entry(janela, font=("Arial", 10))
segunda_media.pack(pady=2)

# Terceira nota
lbl_calculo = tk.Label(janela, text="Digite a 3ª nota: ", bg="#E7FF9E")
lbl_calculo.pack(pady=7)
terceira_media = tk.Entry(janela, font=("Arial", 10))
terceira_media.pack(pady=2)

# Botão calcular
btn_calcular=tk.Button(janela, text="Calcular", font=("Arial", 11),  
bg="#7E8C54", fg="white", command=calculo)
btn_calcular.pack(pady=17)

janela.mainloop()
