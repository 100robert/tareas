def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius


try:
    temperatura = float(input("Ingresa la temperatura: "))
    unidad = input("Ingresa la unidad (C para Celsius, F para Fahrenheit): ").upper()

    if unidad == 'C':
        fahrenheit = celsius_to_fahrenheit(temperatura)
        print(f"{temperatura}°C equivale a {fahrenheit:.2f}°F")
    elif unidad == 'F':
        celsius = fahrenheit_to_celsius(temperatura)
        print(f"{temperatura}°F equivale a {celsius:.2f}°C")
    else:
        print("Unidad no reconocida. Por favor, ingresa 'C' o 'F'.")

except ValueError:
    print("Entrada inválida. Asegúrate de ingresar un número válido para la temperatura.")