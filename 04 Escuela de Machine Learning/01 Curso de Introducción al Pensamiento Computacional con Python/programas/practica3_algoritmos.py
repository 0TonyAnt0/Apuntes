objetivo=int(input('Escoje un entero'))
respuesta =0

while respuesta**2 < objetivo:
    respuesta +=1
if respuesta**2 == objetivo:
    print(f'La raiz cuadrada de {objetivo} es igual a {respuesta}')
else:
    print(f'{objetivo} no tiene una raíz cuadrada')