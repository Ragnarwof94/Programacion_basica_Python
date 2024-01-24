""" Item 1: Confecciona un programa que reciba la temperatura en grados Celsius, y la traspase a grados Fahrenheit"""

#Solicitamos al usuario ingresar grados en celsius

celcius = float(input("ingrese grados Celsius y luego presione ENTER: "))

#Realizamos la conversión con la formula de Celsius a Fahrenheit

fahrenheit = (celcius * 1.8) + 32 #es igual a decir Fahrenheit = 9/5 * C° + 32

#Mostramos el resultado en pantalla

print ("El resultado convertido de Celsius a Fahrenheit es:", fahrenheit,"°F ")