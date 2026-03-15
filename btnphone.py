'''
Programa que simula os teclados do telefone de botão
'''
import tkinter as tk
from time import time

#----Inicialização & configuração da tela------
root = tk.Tk()
root.resizable(False,False)
#----------Funções e algumas inicializações----
ini = time()
saida = tk.StringVar()
global contClicks, t, listap, antis
contClicks,t,listap,antis =  0,0,'',''
digitos = [['1,.','2ABC','3DEF'],
           ['4GHI','5JKL','6MNO'],
           ['7PQRS','8TUV','9WXYZ'],
           ['*','0 ','#']]
#---------------------
def timer(tempo):
    global t
    tempo = int(tempo - ini)
    test1 = tempo - t == 0
    test2 = tempo - t == 1
    t = tempo
    if test1 or test2:
        return True
    return False

def countClicks(teclas):
    global contClicks, antis
    click = contClicks
    contClicks += 1
    if antis == teclas and timer(time()):
        if contClicks < len(teclas):
            return click, True
        else:
            contClicks = 0
            return click, True
    elif antis == teclas and timer(time()) == False:
            contClicks = 0
            click = contClicks
            contClicks += 1
            return click, True
    else:
        antis = teclas
        contClicks = 0
        click = contClicks
        contClicks += 1
        return click, False 
    

def addTeclas(teclas):
    global listap
    click, ant = countClicks(teclas)
    click  = teclas[click]
    if timer(time()) == True and ant == True:
        return saida.set(listap + click)
    elif timer(time()) == True and ant == False:
        listap = saida.get()
        return saida.set(listap + click)  
    else:
        listap = saida.get()
        return saida.set(listap + click)
        
#------------------widget's---------------------
out = tk.Entry(root,
    textvariable=saida,
    font=('Arial', 16),
    state='disabled')

#--------------Inserção dos widget's------------
out.grid(row=1, columnspan=3)
for x in range(4):
    for i in range(3):
        comando = lambda tec = digitos[x][i]: addTeclas(tec)
        btns = tk.Button(root,
        text=digitos[x][i],
        width=10,
        height=2,
        command=comando)
        btns.grid(row=x+2, column=i)
        
root.mainloop()