# Ejercicio 6
import tkinter as tk
from tkinter.colorchooser import askcolor
from tkinter.messagebox import showinfo


ventana = tk.Tk()
ventana.title("Cambiar Color")

color = askcolor()
ventana["bg"] = color[1]
showinfo(message = f"El color seleccionado fue: {color[0]}")

ventana.mainloop()


#Ejercicio 7

import tkinter as tk
from tkinter import ttk

def saludar():
    print("Hola, Gracias por hacer click")

ventana = tk.Tk()
mi_boton = ttk.Button(ventana, text="Click aquí", command=saludar)
mi_boton.pack()
ventana.mainloop()

#Ejercicio 8

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

def funcion_a_ejecutar():
    showinfo(message=nombre.get())


ventana = tk.Tk()
nombre = tk.StringVar()

ttk.Entry(ventana, textvariable=nombre).pack()
ttk.Button(ventana, text="aceptar", command=funcion_a_ejecutar).pack()

ventana.mainloop()



#Ejercicio 9

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

def funcion_a_ejecutar():
    showinfo(message=nombre.get())
    showinfo(message=password.get())

ventana = tk.Tk()
nombre = tk.StringVar()
password = tk.StringVar()

ttk.Entry(ventana, textvariable=nombre).pack()
ttk.Entry(ventana, textvariable=password, show="*").pack()
ttk.Button(ventana, text="aceptar", command=funcion_a_ejecutar).pack()

ventana.mainloop()




#Ejercicio 10 

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

def funcion_a_ejecutar():
    showinfo(message="seleccionó: " + mi_variable.get())

ventana = tk.Tk()
mi_variable = tk.StringVar()

ttk.Checkbutton(ventana,
                text='acepto',
                command=funcion_a_ejecutar,
                variable=mi_variable,
                onvalue='acepto',
                offvalue='no_acepto').pack()
ventana.mainloop()


#Ejercicio 11

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

# ventana principal
ventana = tk.Tk()
ventana.geometry("300x200+400+200")
ventana.resizable(False, False)
ventana.title('Autenticación de usuario')

# variables para guardar el usuario, el password y la opción de guardar password
usuario = tk.StringVar()
password = tk.StringVar()
check = tk.StringVar()

# función que se ejecuta al dar click en el botón login
def login_click():
    mensaje = f"usuario: {usuario.get()}, password: {password.get()}.\nGuardar password: {check.get()}"
    showinfo(title='Atención', message=mensaje)

# Creando un Frame
fra_login = ttk.Frame(ventana)
fra_login.pack(padx=10, pady=10, fill='x', expand=True)

# usuario
lbl_usuario = ttk.Label(fra_login, text="usuario:")
lbl_usuario.pack(fill='x', expand=True)

txt_usuario = ttk.Entry(fra_login, textvariable=usuario)
txt_usuario.pack(fill='x', expand=True)
txt_usuario.focus()

# password
lbl_password = ttk.Label(fra_login, text="Password:")
lbl_password.pack(fill='x', expand=True)

txt_password = ttk.Entry(fra_login, textvariable=password, show="*")
txt_password.pack(fill='x', expand=True)

# checkbutton
check_guardar = ttk.Checkbutton(fra_login,
                text='guardar password',
                variable=check,
                onvalue='True',
                offvalue='False')
check_guardar.pack(fill='x', expand=True)

# button
btn_login = ttk.Button(fra_login, text="Login", command=login_click)
btn_login.pack(fill='x', expand=True, pady=10)

ventana.mainloop()


#Ejercicio 11

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

def funcion_a_ejecutar():
   etiqueta["text"] = nombre.get() + " " + apellido.get()

ventana = tk.Tk()
nombre = tk.StringVar()
apellido = tk.StringVar()

ttk.Entry(ventana, textvariable=nombre).pack(fill='x', expand=True)
ttk.Entry(ventana, textvariable=apellido).pack(fill='x', expand=True)
etiqueta = ttk.Label(ventana)
etiqueta.pack(fill='x', expand=True)
ttk.Button(ventana, text="aceptar", command=funcion_a_ejecutar).pack(fill='x', expand=True)

ventana.mainloop()




#Ejercicio 12


import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

def funcion_controladora(param):
    showinfo(message = param)

ventana = tk.Tk()
ttk.Button(ventana, text="1", command= lambda : funcion_controladora("1")).pack()
ttk.Button(ventana, text="0", command= lambda : funcion_controladora("0")).pack()

ventana.mainloop()





