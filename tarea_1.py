num = int(input("introdusca un numero: "))
contador = 0
apoyo = 1

for i in range(num):
    espon = contador + apoyo
    contador = apoyo
    apoyo = espon
    print(apoyo)