
tipo_mascota = input("Ingresa el tipo de mascota (perro, gato, conejo): ").lower()

if tipo_mascota == "perro":
    print(" Te Recomiendo: Croquetas para perros adultos o cachorros según la edad.")
elif tipo_mascota == "gato":
    print("Te Recomiendo: Alimento balanceado para gatos y golosinas especiales.")
elif tipo_mascota == "conejo":
    print("Te Recomiendo: Heno fresco, pellets y verduras frescas.")
else:
    print("No tenemos recomendaciones para ese tipo de mascota.")