# Solicitar el mensaje y el desplazamiento al usuario
mensaje_original = input("Ingrese el mensaje a cifrar: ")
desplazamiento = 1

alfabeto_mayusculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alfabeto_minusculas = 'abcdefghijklmnopqrstuvwxyz'

mensaje_cifrado = ""
for letra in mensaje_original:
    if letra.isupper():
        indice_actual = alfabeto_mayusculas.index(letra)
        nuevo_indice = (indice_actual + desplazamiento) % 26
        nueva_letra = alfabeto_mayusculas[nuevo_indice]
    elif letra.islower():
        indice_actual = alfabeto_minusculas.index(letra)
        nuevo_indice = (indice_actual + desplazamiento) % 26
        nueva_letra = alfabeto_minusculas[nuevo_indice]
    else:
        nueva_letra = letra

    mensaje_cifrado += nueva_letra

# Mostrar el resultado
print("Mensaje original:", mensaje_original)
print("Mensaje cifrado:", mensaje_cifrado)
