
lista = []
for i in range(1,10):
    n = int(input("ingese numero a la lista. "))
    lista.append(n)
    n = 0
    
max = 0
total = 0
promedio = 0
c5 = 0

print("resulado final: ")
for i in lista:
    print(i)  #todos   
    if i > max:
        max = i  #maximo
    total = total + i #promedio
    if i == 5:
        c5 = c5 + 1 #cantidad de 5

promedio = total / 10
print("el promedio es: ",promedio)
print("el numero maximo es: ",max)
print("la cantidad de 5 son: ",c5)
