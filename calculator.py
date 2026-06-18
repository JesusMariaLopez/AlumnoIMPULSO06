#!/usr/bin/env python3

def get_number(prompt):
    while True:
        value = input(prompt).strip()
        try:
            return float(value)
        except ValueError:
            print("Entrada inválida. Por favor ingresa un número.")


def main():
    print("Calculadora aritmética básica")
    print("Operaciones disponibles: 1) Sumar 2) Restar 3) Multiplicar 4) Dividir 5) Salir")

    while True:
        choice = input("Elige una operación (1-5): ").strip()
        if choice == "5":
            print("Adiós.")
            break

        if choice not in {"1", "2", "3", "4"}:
            print("Opción inválida. Intenta de nuevo.")
            continue

        a = get_number("Ingresa el primer número: ")
        b = get_number("Ingresa el segundo número: ")

        if choice == "1":
            result = a + b
            op_name = "suma"
        elif choice == "2":
            result = a - b
            op_name = "resta"
        elif choice == "3":
            result = a * b
            op_name = "multiplicación"
        else:
            op_name = "división"
            if b == 0:
                print("Error: no se puede dividir por cero.")
                continue
            result = a / b

        print(f"Resultado de la {op_name}: {result}\n")


if __name__ == "__main__":
    main()
