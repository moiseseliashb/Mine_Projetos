from tkinter import *
from time import time
root = Tk()
root.title('Contador de Clicks')
root.geometry('250x300')
ini = time()
global t
t = 0
#Funções
def timer(tempo):
    global t
    tempo = int(tempo - ini)
    test1 = tempo - t == 0
    test2 = tempo - t == 1
    t = tempo
    if test1 or test2:
        return True
    return False

def contar():
    cont = count.get()
    if timer(time()):
        cont += 1
        if cont > 5:
            cont = 0
    else:
        cont += 2
        if cont > 5:
            cont = 0
    count.set(cont)

#----------------------------
count = IntVar()
label1 = Label(root, textvariable=count)
label1.pack()
#botão contar
btnContador = Button(root, text='Contar', command=contar)
btnContador.pack()
root.mainloop()