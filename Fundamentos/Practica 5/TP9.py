n = int(input('Ingresa un numero entero: '))
stotalI = 0
while n <= 0:
    n = int(input('Por favor ingresa un numero entero positivo'))


for ct in range(1, n + 1):
    if ct % 2 != 0:
        print('numero:', ct)
        stotalI = stotalI + ct
        
print('Suma total:',stotalI)
