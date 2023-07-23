# Solicitar el mensaje y el desplazamiento al usuario
mensaje_original = input("Ingrese el mensaje a cifrar: ")
desplazamiento = 1

mensaje_cifrado = ""
for letra in mensaje_original:
    # Verificar si la letra es una letra del alfabeto
    if letra.isalpha():
        # Obtener el código ASCII de la letra
        codigo_ascii = ord(letra)
        # Verificar si es una letra mayúscula o minúscula y calcular el desplazamiento en el alfabeto
        if letra.isupper():
            nueva_letra = chr((codigo_ascii - 65 + desplazamiento) % 26 + 65)
        else:
            nueva_letra = chr((codigo_ascii - 97 + desplazamiento) % 26 + 97)
        mensaje_cifrado += nueva_letra
    else:
        mensaje_cifrado += letra

# Mostrar el resultado
print("Mensaje original:", mensaje_original)
print("Mensaje cifrado:", mensaje_cifrado)
