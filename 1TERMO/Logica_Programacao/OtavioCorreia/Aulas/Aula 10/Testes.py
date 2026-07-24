
import tkinter as tk
from tkinter import messagebox
from time import sleep

janela = tk.Tk()
janela.title("Gerenciamento de status de conformidade") 
janela.configure(bg="#E7FF9E") 
janela.geometry("400x450") 

cadastro = tk.Tk()
cadastro.title("Gerenciamento de status de conformidade") 
cadastro.configure(bg="#E7FF9E") 
cadastro.geometry("400x450") 

funcionarios = []
def registro():
    # Nome caixa
    caixa_nome = tk.Label(cadastro, text="Digite seu nome",     
    bg="#E7FF9E", font=("Arial", 10))
    caixa_nome.pack(pady=7)

    # Nome info

    nome = tk.Entry(cadastro, font=("Arial", 10))

    caixa_setor = tk.Label(cadastro, text="Digite seu setor",     
    bg="#E7FF9E", font=("Arial", 10))
    caixa_setor.pack(pady=7)
   
    setor = tk.Entry(cadastro, font=("Arial", 10))

    caixa_status = tk.Label(cadastro, text="Digite seu status dos treinamentos (NR-10, NR-35 e brigada",     
    bg="#E7FF9E", font=("Arial", 10))
    caixa_status.pack(pady=7)

    status = tk.Entry(cadastro, font=("Arial", 10))

    caixa_ano = tk.Label(cadastro, text="Digite o ano do último treinamento da Brigada de Incêndio",     
    bg="#E7FF9E", font=("Arial", 10, "bold"))
    caixa_ano.pack(pady=7)

    anos = tk.Entry(cadastro, font=("Arial", 10))
    
    dados = registro()
    funcionarios.append(dados)
    return nome, setor, status


def relatorio():
    if not funcionarios:
        print("Nenhum registro encontrado.")
        sleep(1.2)
    else:
        for f in funcionarios:
            print(f"Nome: {f[0]} | Setor: {f[1]} | Status: {f[2]}")
            sleep(1.2)
  
        
lbl_titulo = tk.Label(janela, text="Menu",     
bg="#E7FF9E", font=("Arial", 10, "bold"))
lbl_titulo.pack(pady=10)

btn_cadastro = tk.Button(janela, text="Cadastro de funcionario", font= ("Arial", 10),   
bg="#7E8C54", fg="white", command=registro) 
btn_cadastro.pack(pady=10)

btn_relatorio = tk.Button(janela, text="Relatório dos funcionários", font= ("Arial", 10),   
bg="#7E8C54", fg="white", command=relatorio) 
btn_relatorio.pack(pady=10)

btn_fechar = tk.Button(janela, text="Fechar", font= ("Arial", 10),   
bg="#7E8C54", fg="white", command=janela.destroy) 
btn_fechar.pack(pady=10)

janela.mainloop()