nroCliente = int(input('Ingrese numero de cliente'))
totalFactura = int(input('Ingrese total factura'))

if 200 < (totalFactura * 0.02):
    primeros10 = totalFactura - (totalFactura * 0.02)
else:
    primeros10 = totalFactura - 200

if 350 > (totalFactura * 0.1):
    post20 = totalFactura + 350
else:
    post20 + totalFactura + (totalFactura * 0.1)
    
print("Informe de pago para el cliente", nroCliente)
print("Importe a pagar si paga dentro de los primeros 10 días:", primeros10)
print("Importe a pagar si paga entre el día 11 y el día 20:", totalFactura)
print("Importe a pagar si paga después del día 20:", post20)
    