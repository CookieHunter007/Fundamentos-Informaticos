ct = 0
ct10 = 0 
ctBase = 0 
sValorTotal = 0 

cantidadP = int(input('Ingrese la cantidad de productos (-1 para salir): '))
precioB = int(input('Ingrese precio base: '))

while cantidadP != -1:
    if cantidadP <= 12:
        sValorTotal = sValorTotal + (precioB * cantidadP)
        ctBase = ctBase + 1 
        ct= ct + 1 
    elif cantidadP >= 13 and cantidadP <= 100:
        sValorTotal = sValorTotal + (12*precioB) +((cantidadP -12)*(precioB*0.9))
        ct = ct + 1
        ct10 = ct10 + 1
    elif cantidadP > 100:
        sValorTotal = sValorTotal + (12*precioB) + (88 *(precioB*0.9))+((cantidadP - 100)*(precioB*0.75))
        ct = ct + 1
        ct10 = ct10 + 1
    prom = sValorTotal/cantidadP
    print('El valor total de la venta es:', sValorTotal, '\nPromedio por unidad:', prom)
    cantidadP = int(input('Ingrese la cantidad de productos (-1 para salir): '))
    if cantidadP == -1:
        break
    precioB = int(input('Ingrese precio base: '))
    

print('Cantidad de ventas realizadas total:', ct)
print('Cantidad de ventas en las que se aplicó un 10% de descuento:', ct10)
print('Cantidad de ventas en las que SOLO se aplicó el precio base:', ctBase)
