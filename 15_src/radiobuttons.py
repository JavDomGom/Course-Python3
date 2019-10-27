from tkinter import *

def seleccionar():
    monitor.config(text='{}'.format(opcion.get()))

def reset():
    opcion.set(None)
    monitor.config(text='')

# Configuración de la raíz.
root = Tk()
root.title('Test tk')
root.resizable(1,1)
root.iconbitmap('@/home/jdg/git/Course-Python3/15_src/hola.xbm')

opcion = IntVar()


Radiobutton(root, text='Opción 1', variable=opcion, value=1, command=seleccionar).pack()
Radiobutton(root, text='Opción 2', variable=opcion, value=2, command=seleccionar).pack()
Radiobutton(root, text='Opción 3', variable=opcion, value=3, command=seleccionar).pack()

monitor = Label(root)
monitor.pack()

Button(root, text='Reiniciar', command=reset).pack()

root.mainloop()
