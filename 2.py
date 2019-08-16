

tamaño = int(input("ingrese el tamaño que desee para el ciclo: "))

print("") #salto en linea
contador = 0
for i in range(0,tamaño) :
    numero = int(input(i, ".ingrese numero "))
    contador += numero 

if tamaño > 1:
    print("la suma de todos esos ",tamaño," numeros es: ",contador)
else :
    print("apenas ingreso UN Solo numero. el: ",contador)
