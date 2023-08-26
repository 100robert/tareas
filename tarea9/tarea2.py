def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        raise ValueError("No es posible dividir por cero.")


try:
    numero1 = float(input("Ingresa el primer número: "))
    numero2 = float(input("Ingresa el segundo número: "))
    operacion = input("Selecciona la operación (+, -, *, /): ")

    if operacion == "+":
        resultado = suma(numero1, numero2)
    elif operacion == "-":
        resultado = resta(numero1, numero2)
    elif operacion == "*":
        resultado = multiplicacion(numero1, numero2)
    elif operacion == "/":
        resultado = division(numero1, numero2)
    else:
        print("Operación no reconocida. Por favor, ingresa '+', '-', '*', o '/'.")

    print(f"Resultado: {resultado}")

except ValueError:
    print("Entrada inválida. Asegúrate de ingresar números válidos.")

except Exception as e:
    print(f"Error: {e}")