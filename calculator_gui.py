#!/usr/bin/env python3
import tkinter as tk
from tkinter import messagebox


def calculate():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
    except ValueError:
        messagebox.showerror("Entrada inválida", "Ingresa números válidos.")
        return

    op = operation.get()
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

frame = tk.Frame(root, padx=16, pady=16)
frame.pack()

label_a = tk.Label(frame, text="Primer número:")
label_a.grid(row=0, column=0, sticky="w")
entry_a = tk.Entry(frame, width=20)
entry_a.grid(row=0, column=1, pady=4)

label_b = tk.Label(frame, text="Segundo número:")
label_b.grid(row=1, column=0, sticky="w")
entry_b = tk.Entry(frame, width=20)
entry_b.grid(row=1, column=1, pady=4)

operation = tk.StringVar(value="sum")

label_op = tk.Label(frame, text="Operación:")
label_op.grid(row=2, column=0, sticky="w")

options_frame = tk.Frame(frame)
options_frame.grid(row=2, column=1, pady=4, sticky="w")

radio_sum = tk.Radiobutton(options_frame, text="Sumar", variable=operation, value="sum")
radio_sum.pack(anchor="w")
radio_sub = tk.Radiobutton(options_frame, text="Restar", variable=operation, value="sub")
radio_sub.pack(anchor="w")
radio_mul = tk.Radiobutton(options_frame, text="Multiplicar", variable=operation, value="mul")
radio_mul.pack(anchor="w")
radio_div = tk.Radiobutton(options_frame, text="Dividir", variable=operation, value="div")
radio_div.pack(anchor="w")

button_calc = tk.Button(frame, text="Calcular", command=calculate, width=18)
button_calc.grid(row=3, column=0, columnspan=2, pady=8)

result_label = tk.Label(frame, text="Resultado:", font=(None, 12, "bold"))
result_label.grid(row=4, column=0, columnspan=2, pady=8)

root.mainloop()
