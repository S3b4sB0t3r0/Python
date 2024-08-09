import tkinter as tk

ventana = tk.Tk()
etiqueta = tk.Label(ventana, text="Hola Mundo gráfico")
etiqueta.pack()
ventana.title("Aplicación GUI con Tkinter")
ventana.geometry("800x600+150+50")
ventana.resizable(False, True)
ventana.attributes("-alpha", 0.9)
ventana.mainloop()