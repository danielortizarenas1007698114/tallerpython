frutas = {
    'platano': 1.35,
    'manzana': 0.80,
    'pera': 0.85,
    'naranja': 0.70
}

print("""tenemos:

platano
manzana
pera
naranja
""")

try:
    fruta = input("fruta? ")
    nkilos = int(input("numero de kilos: "))

    def fruts():
        total = nkilos * frutas[fruta]
        return total

#print(frutas[fruta])
    print("el total es: ",fruts())
except:
    print("esa fruta no existe")
