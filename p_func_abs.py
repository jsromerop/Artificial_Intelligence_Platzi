print('Escoge un método para raíz cuadrada: 1- Búqueda Binaria/ 2- Aproximación/ 3- Enumeración')
metodo = int(input('Digita el número del método: '))
objetivo = int(input('Escoge un número: '))

if metodo == 1:

    epsilon = 0.001
    bajo = 0.0
    alto = max(1.0, objetivo)
    respuesta = (alto + bajo) / 2

    while abs(respuesta**2 - objetivo) >= epsilon:
        if respuesta**2 < objetivo:
            bajo = respuesta
        else:
            alto = respuesta
        respuesta = (alto + bajo) / 2
    print(f'La raíz cuadrada de {objetivo} es {respuesta}')

elif metodo == 2:
    epsilon = 0.0001
    paso = epsilon**2
    respuesta = 0.0
    while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
        respuesta += paso
    if abs(respuesta**2 - objetivo) >= epsilon:
        print(f'No se encontró la raíz cuadrada de {objetivo}')
    else:
        print(f'La raíz cuadrada de {objetivo} es {respuesta}')

elif metodo == 3:
    respuesta = 0
    while respuesta**2 < objetivo:
        respuesta += 1
    if respuesta**2 == objetivo:
        print(f'La raíz cuadrada de {objetivo} es {respuesta}')
    else:
        print(f'{objetivo} no tiene una raíz cuadrada exacta')
else:
    print('El dato no es válido')
