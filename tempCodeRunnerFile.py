
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