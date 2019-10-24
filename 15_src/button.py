from tkinter import *

def suma():
    r.set(float(n1.get()) + float(n2.get()))
    borrar()

def resta():
    r.set(float(n1.get()) - float(n2.get()))
    borrar()

def producto():
    r.set(float(n1.get()) * float(n2.get()))
    borrar()

def borrar():
    n1.set('')
    n2.set('')

# Configuración de la raíz.
root = Tk()
root.title('Test tk')
root.resizable(1,1)
root.iconbitmap('@/home/jdg/git/Course-Python3/15_src/hola.xbm')
root.config(bd=15)

n1 = StringVar()
n2 = StringVar()
r = StringVar()

Label(root, text='Número 1').pack()
Entry(root, justify='center', textvariable=n1).pack() # Primer numero
Label(root, text='Número 2').pack()
Entry(root, justify='center', textvariable=n2).pack() # Segundo numero
Label(root, text='\nResultado').pack()
Entry(root, justify='center', textvariable=r, state='disable').pack() # Resultado
Label(root, text='').pack()

Button(root, text='Sumar', command=suma).pack(side='left')
Button(root, text='Restar', command=resta).pack(side='left')
Button(root, text='Multiplicar', command=producto).pack(side='left')

root.mainloop()
