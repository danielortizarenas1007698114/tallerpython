import random
numeros = []
tamaño = int(input("ingrese la cantidad de numeros aleatorios que desea guardar en su lista"))
for i in range(0,tamaño):
     n = random.randint(0, 50)
     numeros.append(n)
     
print(numeros)
