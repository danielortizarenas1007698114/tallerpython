diccionario = {}
fin = False 
while fin:
    español = input("palabra por favor: ")
    ingles = input("translation please: ")
    print(español,":",ingles)
    
    diccionario[español] = ingles
    des = int(imput("continuar? 1 para si, 0 para no"))
    if des != 1:
        des = 0
    fin = bool([des])

palabra = input ("ingrese palabra para traducir")

if palabra in diccionario :
    print(diccionario[palabra])
else:
    print("esa palabra no tiene traduccion")
