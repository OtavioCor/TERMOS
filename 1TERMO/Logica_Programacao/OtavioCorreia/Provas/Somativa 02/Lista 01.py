
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
        messagebox.showwarning("Aviso", "Digite a quantidade de peças produzidas em 1 hora, para descobrir quantas serão produzidas em 8 horas.")
    else:
        messagebox.showinfo("Calculo de Produção", f"Em 8 horas serão produzidas: {peca* 8}")


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
        messagebox.showwarning("Calculo de Produção", "Digite a pressão em Bar para converter para PSI.")
    else:
        psi = bar * 14.5
        messagebox.showinfo("Calculo de Produção", f"A pressão convertida para PSI é: {psi:.2f} PSI")
        
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
        messagebox.showwarning("Resultado", "Baixa carga")
    elif 40 <= temperatura <= 70:
        messagebox.showinfo("Resultado", "Normal")
    else:
        messagebox.showwarning("Resultado", "ALERTA: Resfriamento Ativado!")

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

janela = tk.Tk()
janela.title("Classificador de Lote") 
janela.configure(bg="#E7FF9E") 
janela.geometry("400x250")

def registro():
    codigo = ent_cod.get()


    if codigo.upper().startswith("A"):
        messagebox.showinfo("Classificador de Lotes", "Alimento")
    elif codigo.upper().startswith("E"):
        messagebox.showinfo("Classificador de Lotes", "Eletrônicos")
    else:
        messagebox.showinfo("Classificador de Lotes", "Desconhecido")

lbl_codigo = tk.Label(janela, text="Insira o código do produto", font = ("Arial", 14))
lbl_codigo.grid(row = 0, column = 0, pady = 10, padx = 10)

ent_cod = tk.Entry(janela, font=("Arial", 10))
ent_cod.grid(row = 1, column = 0, pady = 10, padx = 14)

btn_calculo = tk.Button(janela, text = "Registro", font = ("Arial", 14), command=registro)
btn_calculo.grid(row = 2, column = 0, pady = 10, padx = 10)

janela.mainloop()

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

#7. Segurança de Operação: A máquina só liga se o sensor_porta == "fechada" E o botao_emergencia == "desligado". Peça esses dois inputs e diga se a máquina pode iniciar.

import tkinter as tk
from tkinter import messagebox, ttk 

janela = tk.Tk()
janela.title("Segurança de Operação") 
janela.configure(bg="#E7FF9E") 
janela.geometry("400x250")

def iniciar():
    sensor = cmb_sensor.get()
    botao = cmb_botao.get()
    if sensor == "Fechada" and botao == "Desligado":
        messagebox.showinfo("Segurança de Operação", "A máquina pode iniciar.")
    else:
        messagebox.showwarning("Segurança de Operação", "A máquina não pode iniciar.")



lbl_sensor = tk.Label(janela, text = "Porta do sensor",
                            font = ("Arial", 14))
lbl_sensor.grid(row = 0, column = 0, pady = 10, padx = 10)

cmb_sensor = ttk.Combobox(janela, values = ["Aberto", "Fechada"],
                               width = 10, font = ("Arial", 14), state = "readonly") 
cmb_sensor.grid(row = 0 ,column = 1, pady = 10, padx = 10)

lbl_botao = tk.Label(janela, text = "Botão de emergência",
                            font = ("Arial", 14))
lbl_botao.grid(row = 1, column = 0, pady = 10, padx = 10)

cmb_botao = ttk.Combobox(janela, values = ["Ligado", "Desligado"],
                               width = 10, font = ("Arial", 14), state = "readonly") 
cmb_botao.grid(row = 1 ,column = 1, pady = 10, padx = 10)

btn_seguranca = tk.Button(janela, text = "Verificar",
                                  font = ("Arial", 14), fg = "green", command = iniciar)
btn_seguranca.grid(row = 3 ,column = 1, pady = 10, padx = 10)


janela.mainloop()

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# 8. Cálculo de Descarte: Peça o total de peças produzidas e o total de defeituosas. 
# Se o descarte for maior que 5% do total, exiba "Revisar Processo", caso contrário, "Processo Otimizado".

import tkinter as tk
from tkinter import messagebox, ttk 

janela = tk.Tk()
janela.title("Cálculo de Descarte") 
janela.configure(bg="#E7FF9E") 
janela.geometry("400x250")

def iniciar():
    produzidas = int(ent_peca.get())
    defeituosas = int(ent_def.get())
    
    descarte_percentual = (defeituosas / produzidas) * 100
    if descarte_percentual > 5:
        messagebox.showwarning("Cálculo de Descarte", "Revisar Processo")
    else:
        messagebox.showinfo("Cálculo de Descarte", f"Processo Otimizado\nDescarte percentual: {descarte_percentual:.2f}%")

lbl_peca = tk.Label(janela, text = "Digite o total de peças produzidas",
                            font = ("Arial", 14))
lbl_peca.grid(row = 0, column = 0, pady = 10, padx = 10)

ent_peca = tk.Entry(janela, font=("Arial", 14))
ent_peca.grid(row = 1, column = 0, pady = 10, padx = 14)

lbl_def = tk.Label(janela, text = "Digite o total de peças defeituosas",
                            font = ("Arial", 14))
lbl_def.grid(row = 2, column = 0, pady = 10, padx = 10)

ent_def = tk.Entry(janela, font=("Arial", 14))
ent_def.grid(row = 3, column = 0, pady = 10, padx = 14)


btn_verificacao = tk.Button(janela, text = "Verificar",
                                  font = ("Arial", 14), fg = "green", command = iniciar)
btn_verificacao.grid(row = 4 ,column = 0, pady = 10, padx = 10)

janela.mainloop()

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# 9. Validação de Medida: Uma peça deve ter entre 9.8mm e 10.2mm. Peça a medida e diga se está dentro da tolerância, acima ou abaixo.

import tkinter as tk
from tkinter import messagebox, ttk 

janela = tk.Tk()
janela.title("Validação de Medida") 
janela.configure(bg="#E7FF9E") 
janela.geometry("400x250")

def iniciar():
    produzidas = float(ent_peca.get())

    if produzidas < 9.8:
        messagebox.showwarning("Validação de Medida","A peça está abaixo da tolerância.")
    elif produzidas > 10.2:
        messagebox.showwarning("Validação de Medida","A peça está acima da tolerância.")
    else:
        messagebox.showinfo("Validação de Medida","A peça está dentro da tolerância.")

lbl_peca = tk.Label(janela, text = "Digite a medida da peça",
                            font = ("Arial", 14))
lbl_peca.grid(row = 0, column = 0, pady = 10, padx = 10)

ent_peca = tk.Entry(janela, font=("Arial", 14))
ent_peca.grid(row = 1, column = 0, pady = 10, padx = 14)

btn_verificacao = tk.Button(janela, text = "Verificar",
                                  font = ("Arial", 14), fg = "green", command = iniciar)
btn_verificacao.grid(row = 2 ,column = 0, pady = 10, padx = 10)

janela.mainloop()

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# 10.Contagem Regressiva de Setup: Use um for para fazer uma contagem regressiva de 10 até 1 para o início de uma prensa, e finalize com "Prensa Ativada!".

import tkinter as tk
from tkinter import messagebox, ttk 

janela = tk.Tk()
janela.title("Contagem Regressiva de Setup") 
janela.configure(bg="#E7FF9E") 
janela.geometry("400x250")

def iniciar():
    for contagem in range(10, 0, -1):
        messagebox.showinfo("Contagem Regressiva", f"{contagem}")
    messagebox.showinfo("Contagem Regressiva", "Prensa Ativada")

btn_verificacao = tk.Button(janela, text = "Iniciar Contagem Regressiva",
                                  font = ("Arial", 17), fg = "green", command = iniciar)
btn_verificacao.grid(row = 2 ,column = 0, pady = 10, padx = 10)

janela.mainloop()

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# 11.Soma de Produção (Acumulador): Use um while para pedir o peso de várias caixas.
# O loop para quando o usuário digitar 0. No fim, mostre o peso total acumulado.

import tkinter as tk
from tkinter import messagebox

janela = tk.Tk()
janela.title("Soma de Produção") 
janela.configure(bg="#E7FF9E") 
janela.geometry("450x300")

peso_total = 0.0

def adicionar_peso():
    global peso_total  
    
    try:
        peso = float(ent_peso.get())
        
        if peso == 0:
            messagebox.showinfo("Produção Finalizada", f"Peso total acumulado: {peso_total:.2f}kg")
            janela.destroy() 
            return
        
        peso_total += peso
        lbl_resultado.config(text=f"Total Atual: {peso_total:.2f}kg", fg="green")
        
        ent_peso.delete(0, tk.END)
        
    except ValueError:
        messagebox.showerror("Erro", "Por favor, digite um número válido!")

lbl_instrucao = tk.Label(janela, text="Digite o peso da caixa:", font=("Arial", 14), bg="#E7FF9E")
lbl_instrucao.pack(pady=10)

ent_peso = tk.Entry(janela, font=("Arial", 14), justify="center")
ent_peso.pack(pady=5)

btn_adicionar = tk.Button(janela, text="Adicionar Caixa", font=("Arial", 12, "bold"), command=adicionar_peso)
btn_adicionar.pack(pady=10)

lbl_aviso = tk.Label(janela, text="(Digite 0 para encerrar a produção)", font=("Arial", 10, "italic"), bg="#E7FF9E", fg="gray")
lbl_aviso.pack(pady=2)

lbl_resultado = tk.Label(janela, text="Total Atual: 0.00kg", font=("Arial", 14, "bold"), bg="#E7FF9E")
lbl_resultado.pack(pady=15)

janela.mainloop()

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# 12.Múltiplas Leituras: Use um for para pedir a temperatura de 5 sensores diferentes. Ao final, mostre qual foi a maior temperatura lida.

import tkinter as tk
from tkinter import messagebox

janela = tk.Tk()
janela.title("Leitura de Sensores")
janela.configure(bg="#D1F2A5")
janela.geometry("450x300")

contador = 1
maior_temperatura = float('-inf')  

def ler_temperatura():
    global contador, maior_temperatura
    
    try:
        temp_atual = float(ent_temp.get())
        
        if temp_atual > maior_temperatura:
            maior_temperatura = temp_atual
            
        ent_temp.delete(0, tk.END)
        
        contador += 1
        
        if contador <= 5:
            lbl_instrucao.config(text=f"Digite a temperatura do Sensor {contador}:")
        else:
            messagebox.showinfo("Resultado Final", f"A maior temperatura lida foi: {maior_temperatura:.1f}°C")
            janela.destroy() 
            
    except ValueError:
        messagebox.showerror("Erro", "Por favor, digite um número válido para a temperatura!")

lbl_instrucao = tk.Label(janela, text=f"Digite a temperatura do Sensor {contador}:", 
                         font=("Arial", 14), bg="#D1F2A5")
lbl_instrucao.pack(pady=20)

ent_temp = tk.Entry(janela, font=("Arial", 14), justify="center")
ent_temp.pack(pady=10)

btn_enviar = tk.Button(janela, text="Registrar Temperatura", 
                        font=("Arial", 12, "bold"), command=ler_temperatura)
btn_enviar.pack(pady=20)

janela.mainloop()

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

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

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# 14.Simulador de Estoque: Comece com estoque = 100. Crie um menu (while) onde o usuário pode: (1) Adicionar itens, (2) Remover itens ou (3) Sair. Se o estoque ficar
# abaixo de 10, avise: "Estoque Crítico!".

import tkinter as tk
from tkinter import messagebox

janela = tk.Tk()
janela.title("Simulador de Estoque")
janela.geometry("350x300")
janela.configure(bg="#E7FF9E")

estoque = 100


def adicionar():
    global estoque
    
    quantidade = int(ent_qtd.get())
    estoque = estoque + quantidade
   
    lbl_resultado.config(text=f"Estoque Atual: {estoque}")
    
  
    if estoque >= 10:
        lbl_aviso.config(text="")

def remover():
    global estoque

    quantidade = int(ent_qtd.get())
    estoque = estoque - quantidade
    
    lbl_resultado.config(text=f"Estoque Atual: {estoque}")
    
    if estoque < 10:
        lbl_aviso.config(text="ESTOQUE CRÍTICO!", fg="red")

def sair():
    janela.destroy() 


lbl_resultado = tk.Label(janela, text=f"Estoque Atual: {estoque}", font=("Arial", 16, "bold"), bg="#E7FF9E")
lbl_resultado.pack(pady=15)

lbl_texto = tk.Label(janela, text="Digite a quantidade:", font=("Arial", 12), bg="#E7FF9E")
lbl_texto.pack()

ent_qtd = tk.Entry(janela, font=("Arial", 12))
ent_qtd.pack(pady=5)

btn_add = tk.Button(janela, text="(1) Adicionar Itens", command=adicionar)
btn_add.pack(pady=5)

btn_rem = tk.Button(janela, text="(2) Remover Itens", command=remover)
btn_rem.pack(pady=5)

btn_sair = tk.Button(janela, text="(3) Sair", command=sair)
btn_sair.pack(pady=5)

lbl_aviso = tk.Label(janela, text="", font=("Arial", 12, "bold"), bg="#E7FF9E")
lbl_aviso.pack(pady=10)

janela.mainloop()

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# 15.Relatório de Turno Completo: Use um for para processar 5 peças. Para cada peça, peça o diâmetro. 
# Se a peça for aprovada (entre 19.9 e 20.1), conte-a. 
# No final do loop, exiba o total de peças aprovadas e a porcentagem de eficiência do lote.

import tkinter as tk

janela = tk.Tk()
janela.title("Relatório de Turno")
janela.geometry("400x350")
janela.configure(bg="#E7FF9E")

peca_atual = 1
aprovadas = 0

def processar_peca():
    global peca_atual, aprovadas
    
    diametro = float(ent_diametro.get())
    
    if 19.9 <= diametro <= 20.1:
        aprovadas = aprovadas + 1
        
    ent_diametro.delete(0, tk.END)
    
    peca_atual = peca_atual + 1
    

    if peca_atual <= 5:
        lbl_instrucao.config(text=f"Digite o diâmetro da Peça {peca_atual}:")
    else:
        eficiencia = (aprovadas / 5) * 100
        
        lbl_instrucao.config(text="Lote Finalizado!", fg="blue")
        lbl_resultado.config(text=f"Peças Aprovadas: {aprovadas} de 5\nEficiência: {eficiencia}%")
        
        btn_enviar.config(state="disabled")

lbl_instrucao = tk.Label(janela, text=f"Digite o diâmetro da Peça {peca_atual}:", font=("Arial", 12, "bold"), bg="#E7FF9E")
lbl_instrucao.pack(pady=20)

ent_diametro = tk.Entry(janela, font=("Arial", 14), justify="center")
ent_diametro.pack(pady=5)

btn_enviar = tk.Button(janela, text="Registrar Peça", font=("Arial", 11), command=processar_peca)
btn_enviar.pack(pady=20)

lbl_resultado = tk.Label(janela, text="", font=("Arial", 14, "bold"), bg="#E7FF9E", fg="green")
lbl_resultado.pack(pady=20)

janela.mainloop()