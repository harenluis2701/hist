# Pedimos el nombre del módulo al inicio
nombre_modulo = input("Ingrese el nombre del módulo: ")

# Variables para guardar los totales del resumen final
total_coders = 0
suma_promedios = 0
cantidad_reprobados = 0
cantidad_regulares = 0
cantidad_excelentes = 0

# Variables para saber quién fue el mejor de la clase
mejor_promedio = -1
mejor_coder = ""

# Esta variable nos ayudará a controlar el ciclo while
continuar = "si"

print("\n--- Inicio del registro de Coders ---")

# El sistema debe permitir ingresar varios coders usando un while
while continuar.lower() == "si":
    nombre_coder = input("\nIngrese el nombre del coder: ")
    
    # 1. Pedir y validar la nota de Desarrollo de Software (debe estar entre 0 y 100)
    nota_software = -1
    while nota_software < 0 or nota_software > 100:
        nota_software = float(input("Nota de Desarrollo de Software (0-100): "))
        if nota_software < 0 or nota_software > 100:
            print("Error: La nota debe estar entre 0 y 100.")
            
    # 2. Pedir y validar la nota de Habilidades Socioemocionales
    nota_habilidades = -1
    while nota_habilidades < 0 or nota_habilidades > 100:
        nota_habilidades = float(input("Nota de Habilidades Socioemocionales (0-100): "))
        if nota_habilidades < 0 or nota_habilidades > 100:
            print("Error: La nota debe estar entre 0 y 100.")
            
    # 3. Pedir y validar la nota de Inglés
    nota_ingles = -1
    while nota_ingles < 0 or nota_ingles > 100:
        nota_ingles = float(input("Nota de Inglés (0-100): "))
        if nota_ingles < 0 or nota_ingles > 100:
            print("Error: La nota debe estar entre 0 y 100.")
            
    # Calcular el promedio usando los porcentajes (60%, 20%, 20%)
    promedio = (nota_software * 0.60) + (nota_habilidades * 0.20) + (nota_ingles * 0.20)
    
    # Determinar en qué clasificación quedó
    clasificacion = ""
    if promedio <= 49:
        clasificacion = "Reprobado"
        cantidad_reprobados = cantidad_reprobados + 1
    elif promedio <= 79:
        clasificacion = "Regular"
        cantidad_regulares = cantidad_regulares + 1
    else:
        clasificacion = "Excelente"
        cantidad_excelentes = cantidad_excelentes + 1
        
    # Mostrar los resultados de este coder en particular
    print("\n--- Resultados de", nombre_coder, "---")
    print("Módulo:", nombre_modulo)
    print("Promedio final:", round(promedio, 2))
    print("Clasificación:", clasificacion)
    
    # Observación especial si le fue mal en Software
    if nota_software < 50:
        print("Observación: Debe reforzar el frente técnico principal.")
        
    # Actualizar los datos generales para el resumen del final
    total_coders = total_coders + 1
    suma_promedios = suma_promedios + promedio
    
    # Revisar si este coder es el mejor hasta ahora
    if promedio > mejor_promedio:
        mejor_promedio = promedio
        mejor_coder = nombre_coder
        
    # Preguntar si queremos registrar a alguien más o salir
    continuar = input("\n¿Desea registrar otro coder? (si/no): ")

# --- FIN DEL CICLO, MOSTRAR RESUMEN FINAL ---

if total_coders > 0:
    # Calcular el promedio de todo el grupo
    promedio_general = suma_promedios / total_coders
    
    print("\n=========================================")
    print("        RESUMEN FINAL DEL MÓDULO         ")
    print("=========================================")
    print("Nombre del módulo:", nombre_modulo)
    print("Total de coders registrados:", total_coders)
    print("Promedio general del grupo:", round(promedio_general, 2))
    print("Cantidad de reprobados:", cantidad_reprobados)
    print("Cantidad de regulares:", cantidad_regulares)
    print("Cantidad de excelentes:", cantidad_excelentes)
    print("Coder con mejor promedio:", mejor_coder, "con", round(mejor_promedio, 2))
else:
    print("\nNo se registraron coders en el sistema.")