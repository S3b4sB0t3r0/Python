import tkinter as tk
from tkinter.messagebox import showinfo
from tkinter.messagebox import showerror
from tkinter.messagebox import showwarning

ventana = tk.Tk()
ventana.title("showinfo")
showinfo(title="Mensaje", message="Bienvenido")
showerror(title="Error", message="Se detectó virus en su equipo")
showwarning(title="Advertencia", message="Puedo estar equivocado\nValide con soporte técnico")
ventana.mainloop()