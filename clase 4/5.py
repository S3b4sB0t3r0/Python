import tkinter as tk
from tkinter.messagebox import askyesno, showinfo


preguntas = [
    ("¿El cielo es azul?", True),
    ("¿2+2 es igual a 5?", False),
    ("¿La tierra es plana?", False),
    ("¿El fuego es frío?", False),
    ("¿Python es un lenguaje de programación?", True)
]


correctas = 0


def hacer_pregunta(indice):
    global correctas
    if indice < len(preguntas):
        pregunta, respuesta_correcta = preguntas[indice]
        respuesta = askyesno(title=f"Pregunta {indice + 1}", message=pregunta)
        if respuesta == respuesta_correcta:
            correctas += 1
        hacer_pregunta(indice + 1)
    else:
        showinfo(title="Resultados", message=f"Respuestas correctas: {correctas} de {len(preguntas)}")
        ventana.destroy()


ventana = tk.Tk()
ventana.title("Cuestionario Verdadero/Falso")

hacer_pregunta(0)

ventana.mainloop()
