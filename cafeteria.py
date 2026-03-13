print("Bienvenida la cafeteria ")
print("1.cafe ")
print("2.Te")
print("3.jugo ")
orden = int(input(" que desea ordenar ?"))
cantidad = int (input("cuantos desea ordenar?"))
if orden == 1:
    cafe=4000*cantidad
    print("total a pagar es ",cafe)
elif orden == 2:
    Te=3500*cantidad
    print("total a pagar es ",Te)
elif orden ==3:
    jugo=5000*cantidad
    print("total a pagar es ", jugo)
else :
    print("esa bebida no esta disponible ")