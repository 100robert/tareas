import random
def generar_contrasena(base, longitud):
    generador_caracteres = lambda conjunto: ''.join(random.choice(conjunto) for _ in range(longitud))
    return generador_caracteres(base)
caracteres = {
    'minus': 'abcdefghijklmnñopqrstuvwxyz',
    'mayus': 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ',
    'numeros': '1234567890',
    'caracteres': '!!#$%&/()?¡*@|'
}
base = ''.join(caracteres.values())
longitud = int(input("Introduzca la cantidad de caracteres que\n"
                     "tendrá su contraseña: "))
contraseña_creada = generar_contrasena(base, longitud)
print(f"La contraseña que se creó es: {contraseña_creada}")
