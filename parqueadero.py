
# Pedimos al usuario cuántas horas estuvo el carro
while True:
    try:
        horas = int(input("Ingresa la cantidad de horas que estuvo el carro: "))
        if horas <= 0:
            print("Error: la cantidad de horas debe ser mayor a 0.")
        else:
            break
    except ValueError:
        print("Error: ingresa un número entero válido.")


precio_primera_hora = 5000
precio_hora_adicional = 3000


if horas == 1:
    total = precio_primera_hora
else:
    total = precio_primera_hora + (horas - 1) * precio_hora_adicional

# Mostramos el total a pagar
print(f"Total a pagar por {horas} hora(s): {total}")