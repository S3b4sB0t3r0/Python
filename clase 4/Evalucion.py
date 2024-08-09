import tkinter as tk

def click_button(value):
    if value == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif value == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, value)

root = tk.Tk()
root.title("Calculadora")

entry = tk.Entry(root, width=16, font=('Arial', 24))
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

for i, button in enumerate(buttons):
    row = (i // 4) + 1
    col = i % 4
    tk.Button(root, text=button, width=4, height=2,
              command=lambda btn=button: click_button(btn)).grid(row=row, column=col)

root.mainloop()
