cadena = input("introdusca una palabra: ")
contador=0
for elem in cadena:
    if elem == "a":
        contador += 1

print("tiene ", contador, " letas a")       