#!/usr/bin/env python3
import tkinter as tk
from tkinter import messagebox


def calculate():
    op = operation.get()
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
    except ValueError:
        messagebox.showerror("Entrada inválida", "Ingresa números válidos.")
        return

    if op == "sum":
        result = a + b
    elif op == "sub":
        result = a - b
    elif op == "mul":
        result = a * b
    elif op == "div":
        if b == 0:
            messagebox.showerror("Error", "No se puede dividir por cero.")
            return
        result = a / b
    else:
        messagebox.showerror("Operación inválida", "Selecciona una operación.")
        return

    result_label.config(text=f"Resultado: {result}")


root = tk.Tk()
root.title("Calculadora aritmética")
root.resizable(False, False)

# Blue theme
BG = '#eaf4ff'
CARD = '#d5eaff'
PRIMARY = '#1e90ff'
PRIMARY_FG = '#ffffff'

root.configure(bg=BG)
frame = tk.Frame(root, padx=16, pady=16, bg=CARD)
frame.pack(padx=20, pady=20)

label_a = tk.Label(frame, text="Primer número / función f(x):", bg=CARD, fg='#03304a')
label_a.grid(row=0, column=0, sticky="w")
entry_a = tk.Entry(frame, width=20)
entry_a.grid(row=0, column=1, pady=4)

label_b = tk.Label(frame, text="Segundo número:", bg=CARD, fg='#03304a')
label_b.grid(row=1, column=0, sticky="w")
entry_b = tk.Entry(frame, width=20)
entry_b.grid(row=1, column=1, pady=4)

operation = tk.StringVar(value="sum")

label_op = tk.Label(frame, text="Operación:", bg=CARD, fg='#03304a')
label_op.grid(row=3, column=0, sticky="w")

options_frame = tk.Frame(frame, bg=CARD)
options_frame.grid(row=3, column=1, pady=4, sticky="w")

radio_sum = tk.Radiobutton(options_frame, text="Sumar", variable=operation, value="sum", bg=CARD, selectcolor=CARD)
radio_sum.pack(anchor="w")
radio_sub = tk.Radiobutton(options_frame, text="Restar", variable=operation, value="sub", bg=CARD, selectcolor=CARD)
radio_sub.pack(anchor="w")
radio_mul = tk.Radiobutton(options_frame, text="Multiplicar", variable=operation, value="mul", bg=CARD, selectcolor=CARD)
radio_mul.pack(anchor="w")
radio_div = tk.Radiobutton(options_frame, text="Dividir", variable=operation, value="div", bg=CARD, selectcolor=CARD)
radio_div.pack(anchor="w")

button_calc = tk.Button(frame, text="Calcular", command=calculate, width=18, bg=PRIMARY, fg=PRIMARY_FG, activebackground=PRIMARY)
button_calc.grid(row=5, column=0, columnspan=2, pady=8)

result_label = tk.Label(frame, text="Resultado:", font=(None, 12, "bold"), bg=CARD, fg=PRIMARY)
result_label.grid(row=6, column=0, columnspan=2, pady=8)

root.mainloop()
