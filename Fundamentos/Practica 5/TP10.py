#Inicializar
rTotal = 0 
ct = 0
sEspecConDesc = 0
stotal=0

#Entrada
espec = int(input('Ingrese cantidad de espectadores'))
while espec <= -1:
    espec = int(input('El numero es invalido, ingrese un entero positivo'))

#Proceso

while espec !=0:
    diaDesc = int(input('Ingrese 1 para dia con descuento y 2 para dia sin descuento'))
    if diaDesc == 2:
        rTotal = rTotal + (espec * 5000)
    elif diaDesc == 1:
        rTotal = rTotal + (espec * 3500)
        sEspecConDesc = sEspecConDesc + espec
    ct = ct + 1 
    stotal = stotal + espec
    espec = int(input('Ingrese cantidad de espectadores'))
#Salida
descPorcent = (sEspecConDesc/stotal) * 100

print('Recaudacion total =',rTotal)
print('Suma de espectadores con descuento =',sEspecConDesc)
print('Porcetaje de espectadores con descuento por funcion =', descPorcent)

