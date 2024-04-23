# Leer el número entero EQC
nroE = int(input("Ingrese un número entero: "))

#Inicializar
nroInvert = 0
esNegativo = False


#Validar EQC
if nroE < 0:
    esNegativo = True
    nroE *= -1  # Convertir número negativo a positivo


#Proceso
while nroE > 0:
    resto = nroE % 10
    nroE //= 10
    nroInvert = nroInvert * 10 + resto

# Si el número original era negativo, invertimos el signo del número invertido
if esNegativo:
    nroInvert *= -1

# Salida
print("El número invertido es:", nroInvert)