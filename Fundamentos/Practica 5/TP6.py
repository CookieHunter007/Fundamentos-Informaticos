nroE = int(input('Por favor ingresa un numero Entero'))
ct = 0

if nroE < 0:
    nroE = nroE * -1
elif nroE == 0:
    print('Ingreso 0')

while nroE  > 0:
    nroE = nroE // 10
    ct = ct + 1

print('La cantidad de digitos del entero es:', ct)