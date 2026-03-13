#Leer compra
compra = float (input("Ingrese el monto de la compra: "))
#Calcular descuento
if compra > 1000:
    descuento = compra * 0.10
    pago= compra - descuento


#Calcular total a pagar                     
print("El total a pagar es: ", pago)    
#finsi