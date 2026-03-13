# Inventario de la ferretería
inventario = {}

def mostrar_inventario():
    if not inventario:
        print("\nEl inventario está vacío.\n")
        return
    
    print("\n--- INVENTARIO ---")
    for serie, datos in inventario.items():
        print(f"""
Número de Serie: {serie}
Nombre: {datos['nombre']}
Cantidad: {datos['cantidad']}
Precio: ${datos['precio']}
--------------------------""")

def agregar_producto():
    serie = input("Número de serie: ")
    if serie in inventario:
        print("Ese número de serie ya existe.")
        return
    
    nombre = input("Nombre del producto: ")
    cantidad = int(input("Cantidad: "))
    precio = float(input("Precio: "))
    
    inventario[serie] = {
        "nombre": nombre,
        "cantidad": cantidad,
        "precio": precio
    }
    
    print("Producto agregado correctamente.")

def vender_producto():
    serie = input("Número de serie del producto a vender: ")
    
    if serie not in inventario:
        print("Producto no encontrado.")
        return
    
    cantidad_vender = int(input("Cantidad a vender: "))
    
    if inventario[serie]["cantidad"] >= cantidad_vender:
        inventario[serie]["cantidad"] -= cantidad_vender
        total = cantidad_vender * inventario[serie]["precio"]
        print(f"Venta realizada. Total a pagar: ${total}")
    else:
        print("No hay suficiente cantidad en inventario.")

def eliminar_producto():
    serie = input("Número de serie a eliminar: ")
    
    if serie in inventario:
        del inventario[serie]
        print("Producto eliminado.")
    else:
        print("Producto no encontrado.")

def actualizar_producto():
    serie = input("Número de serie a actualizar: ")
    
    if serie not in inventario:
        print("Producto no encontrado.")
        return
    
    nombre = input("Nuevo nombre: ")
    cantidad = int(input("Nueva cantidad: "))
    precio = float(input("Nuevo precio: "))
    
    inventario[serie] = {
        "nombre": nombre,
        "cantidad": cantidad,
        "precio": precio
    }
    
    print("Producto actualizado correctamente.")

def menu():
    while True:
        print("""
--- SISTEMA FERRETERÍA ---
1. Mostrar inventario
2. Agregar producto
3. Vender producto
4. Eliminar producto
5. Actualizar producto
6. Salir
""")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            mostrar_inventario()
        elif opcion == "2":
            agregar_producto()
        elif opcion == "3":
            vender_producto()
        elif opcion == "4":
            eliminar_producto()
        elif opcion == "5":
            actualizar_producto()
        elif opcion == "6":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida.")

# Ejecutar el programa
menu()