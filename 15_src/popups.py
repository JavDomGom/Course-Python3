from tkinter import *
from tkinter import messagebox as MessageBox

# Configuración de la raíz.
root = Tk()

def test():
    MessageBox.showinfo('Hola!', 'Hola mundo!')

Button(root, text='Clícame', command=test).pack()

root.mainloop()
