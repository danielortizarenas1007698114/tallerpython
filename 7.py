peso = float(input("ingrese su peso"))
altura = float(input("ingrese su altura(estatura)"))
imc = peso/(altura*altura)
if imc < 15:
    r = "Delgadez muy severa"
if imc > 15 and imc <15.9:
    r = "delgadez severa"
if imc > 16 and imc < 18.4:
    r = "Delgadez"
if imc > 18.5 and imc < 24.9:
    r = "Peso saludable"
if imc > 25 and imc < 29.9:
    r = "Sobrepeso"
if imc > 30 and imc < 34.9:
    r = "Obesidad Severa"
if imc >= 40:
    r = "Obesidad mórbica"
    
print(r)
