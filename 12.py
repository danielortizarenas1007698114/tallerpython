clientes = { #new diccionary
}
op = 0
while op != 6:

    op = int(input("""
(1) Añadir cliente
(2) Eliminar cliente
(3) Mostrar cliente
(4) Listar clientes
(5) Listar clientes preferentes
(6) Terminar
Elige una opción: """))

    if op == 1:
        nif = input("ingrese NIF : ")
        nombre = input("ingrese el nombre del cliente: ")
        direccion = input('ingrese la dirección del cliente: ')
        telefono = input('ingrese el teléfono del cliente: ')
        email = input('ingrese el correo electrónico del cliente: ') 
        vip = int(input("¿Es un cliente preferente? 1 para si, 0 para no"))

        cliente = {
'nombre':nombre ,
'dirección':direccion ,
'teléfono':telefono ,
'email':email,
'preferente':bool([vip])
        } 
        clientes[nif] = cliente
    if op == 2:
        nif2 = input('ingrese NIF del cliente: ')
        if nif2 in clientes:
            del clientes[nif2] 
        else:
            print('no existe el ', nif2)
    if op == 3: 
        nif3 = input('ingrese NIF del cliente: ')
        if nif3 in clientes:
            print('NIF:', nif3)
            for key, value in clientes[nif].items():
                print(key.title() ,':', value) 
            else: 
                print('lo sentimos no existe el cliente con el nif', nif3) 
    if op == 4:
        print('Lista de clientes')
        for key, value in clientes.items():
            print(key, value['nombre']) 
    if op == 5:
        print('Lista de clientes preferentes')
            for key, value in clients.items():
            if value['preferente']:
                  print(key, value['nombre'])
    



print("")
print("fin.")
