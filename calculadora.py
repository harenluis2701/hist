num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))
operacion = input("Introduce la operación a realizar (+, -, *, /): ")           
if operacion == "+":    
    resultado = num1 + num2
elif operacion == "-":
    resultado = num1 - num2
elif operacion == "*":
    
    resultado = num1 * num2
elif operacion == "/":
    resultado = num1 / num2

print("El resultado es: ", resultado)  
