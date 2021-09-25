import tkinter as tk
from tkinter import ttk



#criando instâncias
win = tk.Tk()
win.resizable(False,False)
win.geometry('300x500')


# adicionando título da GUI
win.title("Calculadora de raízes")

# funções de callback dos botões

#Componentes
#Exemplo da equação de segundo grau
modelo = ttk.LabelFrame(win,text="Modelo da equação")
modelo.grid(column=0,row=0,padx=95,pady=25)
ttk.Label(modelo, text="(A)x**2 + (B)x + (C)",foreground="Blue").grid(column=0,row=0)

# Label com as entradas das Entrada das variáveis
#variáveis que guardam os valores de entrada do usuário
coefA = tk.DoubleVar()
coefB = tk.DoubleVar()
coefC = tk.DoubleVar()

#Label das entradas
#Container dos coeficientes
coeficientes = ttk.LabelFrame(win,text="Valores dos coeficientes")
coeficientes.grid(column=0,row=3)
#Coeficiente A
ttk.Label(coeficientes,text="Coeficiente A:").grid(column=0,row=0)
cfA = ttk.Entry(coeficientes,width=12,textvariable=coefA)
cfA.grid(column=1,row=0)
#Coeficiente B
ttk.Label(coeficientes,text="Coeficiente B:").grid(column=0,row=1)
cfA = ttk.Entry(coeficientes,width=12,textvariable=coefA)
cfA.grid(column=1,row=1,)
#Coeficiente C
ttk.Label(coeficientes,text="Coeficiente C:").grid(column=0,row=2)
cfA = ttk.Entry(coeficientes,width=12,textvariable=coefA)
cfA.grid(column=1,row=2)


#iniciando a GUI 
win.mainloop()

