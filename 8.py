tamaño = int(input("tamaño"))
n = 0
for i in range(tamaño):
    if n % 3 == 0:
        print(n," fizz")
    elif n % 5 == 0:
        print(n," buzz")
    else if n % 3 and n % 5:
        print(n," fizzbuzz")
    n+=1
    
