import tkinter as tk
from tkinter import PhotoImage, ttk
from calculater_func_second import second_function
import os

pastcalc = os.path.dirname(__file__)

#criando instâncias
win = tk.Tk()
win.resizable(False,False)
win.geometry('400x600')
win.iconbitmap(r"imagens/icon.ico")


# adicionando título da GUI
win.title("Calculadora de raízes")

# funções de callback dos botões
def calcular():
    #instancia da classe de segundo grau
    app = second_function(coefA.get(),coefB.get(),coefC.get())
    r1 = app.raiz1()
    r2 = app.raiz2()
    if coefA.get() > 0:
        raiz1.configure(text=str(r1))
        raiz2.configure(text=str(r2))
        resultadosConcavidades.configure(image=cima)
    else:
        raiz1.configure(text=str(r1))
        raiz2.configure(text=str(r2))
        resultadosConcavidades.configure(image=baixo)
        

def reset():
    raiz1.configure(text="***")
    raiz2.configure(text="***")
    resultadosConcavidades.configure(image=vazio)
    

    

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
coeficientes = ttk.LabelFrame(win,text="Valores dos coeficientes",borderwidth=1,relief="solid")
coeficientes.grid(column=0,row=2)
#Coeficiente A
ttk.Label(coeficientes,text="Coeficiente A:").grid(column=0,row=0,padx=10)
cfA = ttk.Entry(coeficientes,width=12,textvariable=coefA)
cfA.grid(column=1,row=0)
#Coeficiente B
ttk.Label(coeficientes,text="Coeficiente B:").grid(column=0,row=1)
cfB = ttk.Entry(coeficientes,width=12,textvariable=coefB)
cfB.grid(column=1,row=1,padx=5,pady=5)
#Coeficiente C
ttk.Label(coeficientes,text="Coeficiente C:").grid(column=0,row=2)
cfC = ttk.Entry(coeficientes,width=12,textvariable=coefC)
cfC.grid(column=1,row=2)


#BOTÕES
#Calcular
ttk.Button(win,text="Calcular",command=calcular).grid(column=0,row=3,pady=10)
#reset
ttk.Button(win,text="Reset",command=reset).grid(column=0,row=4)


#raizes
raizes = ttk.LabelFrame(win,text="Valores das raízes")
raizes.grid(column=0,row=5,pady=5)
#raiz1
ttk.Label(raizes, text="R1:",foreground="Green").grid(column=0,row=0,padx=10)
raiz1 = ttk.Label(raizes, text="***",foreground="Green")
raiz1.grid(column=1,row=0,padx=5)
#raiz2
ttk.Label(raizes, text="R2:",foreground="Green").grid(column=0,row=1)
raiz2 = ttk.Label(raizes, text="***",foreground="Green")
raiz2.grid(column=1,row=1)

#imagens
#caminho das imagens
baixo = PhotoImage(file=pastcalc+"\\imagens/concavidade-para-baixo.gif")
cima = PhotoImage(file=pastcalc+"\\imagens/concavidade-para-cima.gif")
vazio = tk.PhotoImage(file=pastcalc+"\\imagens/empty_state.gif")
convavidade= ttk.LabelFrame(win,text="Concavidade da Curva")
convavidade.grid(column=0,row=6,padx=30)
resultadosConcavidades = ttk.Label(convavidade,image=vazio)
resultadosConcavidades.grid(column=0,row=0)
#iniciando a GUI 
win.mainloop()

