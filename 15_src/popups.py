from tkinter import *
from tkinter import messagebox as MessageBox
from tkinter import colorchooser as ColorChooser
from tkinter import filedialog as FileDialog

# Configuración de la raíz.
root = Tk()

def test():
    # MessageBox.showinfo('Hola!', 'Hola mundo!')
    # MessageBox.showwarning('Alerta!', 'Sección solo para administradores.')
    # MessageBox.showerror('Error!', 'Ha ocurrido un error inesperado.')
    # resultado = MessageBox.askquestion('Salir', '¿Estás seguro que quieres salir sin guardar?')
    # if resultado == 'yes':
    #     root.destroy()
    # resultado = MessageBox.askokcancel('Salir', '¿Sobreescribir el fichero actual?')
    # resultado = MessageBox.askyesno('Salir', '¿Estás seguro que quieres salir sin guardar?')
    # if resultado:
    #     root.destroy()
    # resultado = MessageBox.askretrycancel('Reintentar', 'No se puede conectar.')
    # if resultado:
    #     root.destroy()
    # color = ColorChooser.askcolor(title='Elige un color.')
    # print(color)
    # ruta = FileDialog.askopenfilename(title='Abrir un fichero', initialdir='/',
    #     filetypes=(('Ficheros de texto', '*.txt'),
    #     ('Todos los ficheros', '*.*')))
    # print(ruta)
    # Equivale a open('path', 'w')
    fichero = FileDialog.asksaveasfile(title='Guardar un fichero', mode='w', defaultextension='.txt')
    if fichero is not None:
        fichero.write('Hola!')
        fichero.close()

Button(root, text='Clícame', command=test).pack()

root.mainloop()
