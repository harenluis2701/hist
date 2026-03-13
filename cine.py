print("Bienvenido al cine")
orden = int(input("¿Cuántas entradas desea ordenar? "))

if orden <= 0:
    print("No se han ordenado entradas.")
else:

    total_general = 0 


    for i in range(orden):

        print(f"\n--- Datos para la entrada {i + 1} ---") 
        
        edad = int(input("¿Cuál es la edad de esta persona? "))
        
        if edad < 12:
            precio_entrada = 8000
        elif edad >= 12 and edad <= 59:
            precio_entrada = 12000
        elif edad >= 60:
            precio_entrada = 9000
            

        print("El precio de esta entrada es:", precio_entrada)
        

        total_general = total_general + precio_entrada
        

    print("\n===============================")
    print("El TOTAL a pagar por todas las entradas es:", total_general)


