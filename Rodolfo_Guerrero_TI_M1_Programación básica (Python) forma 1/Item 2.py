"""Ítem 2: Realiza un programa que reciba tres números por teclado y calcule su promedio."""

#Solicitamos al usuario los tres números

num1 = float(input("ingrese número 1: "))
num2 = float(input("ingrese número 2: "))
num3 = float(input("ingrese número 3: "))

#Realizamos la fórmula matemática según su jerarquía

promedio = (num1 + num2 + num3) / 3

#Entregamos el resultado del promedio

print (f"El resultado de este promedio es: {promedio:.2f}") #Resultado en f string para acortar decimales a dos cifras
