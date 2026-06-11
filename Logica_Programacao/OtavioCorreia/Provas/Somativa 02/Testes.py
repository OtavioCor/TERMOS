# 13.Painel de Login: Crie um while que peça a senha do supervisor ("admin123").
# Enquanto ele errar, o programa diz "Acesso Negado". Ele tem apenas 3 tentativas.
# Se esgotar, exiba "Painel Bloqueado".

import tkinter as tk
from tkinter import messagebox

janela = tk.Tk()
janela.title("Painel de Login - Supervisor")
janela.configure(bg="#ECEFF1")  
janela.geometry("400x250")

SENHA_CORRETA = "admin123"
tentativas = 0
MAX_TENTATIVAS = 3

def verificar_login():
    global tentativas
    
    senha_digitada = ent_senha.get()
    
    if senha_digitada == SENHA_CORRETA:
        messagebox.showinfo("Acesso Concedido", "Bem-vindo, Supervisor!\nPainel Liberado.")
        janela.destroy()  
    else:
        tentativas += 1
        restantes = MAX_TENTATIVAS - tentativas
        
        if tentativas < MAX_TENTATIVAS:
            messagebox.showwarning("Acesso Negado", f"Senha incorreta!\nVocê tem mais {restantes} tentativa(s).")
            ent_senha.delete(0, tk.END)  
        else:
            messagebox.showerror("Bloqueado", "Painel Bloqueado!\nNúmero de tentativas esgotado.")
            janela.destroy()  

lbl_titulo = tk.Label(janela, text="Controle de Acesso", font=("Arial", 16, "bold"), bg="#ECEFF1", fg="#37474F")
lbl_titulo.pack(pady=15)

lbl_instrucao = tk.Label(janela, text="Digite a senha do supervisor:", font=("Arial", 11), bg="#ECEFF1")
lbl_instrucao.pack(pady=5)

ent_senha = tk.Entry(janela, font=("Arial", 12), show="*", justify="center")
ent_senha.pack(pady=5)

btn_login = tk.Button(janela, text="Entrar", font=("Arial", 11, "bold"), 
                      bg="#26A69A", fg="white", width=15, command=verificar_login)
btn_login.pack(pady=20)

janela.bind('<Return>', lambda event: verificar_login())

janela.mainloop()