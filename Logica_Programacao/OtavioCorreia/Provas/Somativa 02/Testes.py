#6. Classificador de Lotes: O usuário insere o código do produto. Se começar com "A", exiba "Alimentos". Se "E", "Eletrônicos". Para qualquer outro, "Desconhecido".

import tkinter as tk
from tkinter import messagebox      

janela = tk.Tk()
janela.title("Termostato Inteligente") 
janela.configure(bg="#E7FF9E") 
janela.geometry("400x250")

lbl