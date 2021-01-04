nombre_1 = input('Escriba nombre de usuario 1: ')
nombre_2 = input('Escriba nombre de usuario 2: ')
edad_1 = int(input('Escriba edad de usuario 1: '))
edad_2 = int(input('Escriba edad de usuario 2: '))
if edad_1 > edad_2:
    print(f'{nombre_1} es mayor que {nombre_2}')
elif edad_2 < edad_1:
    print(f'{nombre_2} es mayor que {nombre_1}')
else:
    print(f'las edades de {nombre_1} y {nombre_2} son iguales')
