"""Item3: Elabora un programa que, ingresando todas las notas, entregue la nota de presentación."""

#Solicitamos al usuario las tres notas de laboratorio

lab1 = float (input("Ingrese nota de lab 1: "))
lab2 = float (input("Ingrese nota de lab 2: "))
lab3 = float (input("Ingrese nota de lab 3: "))

#Calcula el promedio, pero aún no lo muestra
promediolab = (lab1 + lab2 + lab3) / 3

#Solicitamos al usuario las tres notas de tarea

tarea1 = float (input ("Ingrese nota de tarea 1: "))
tarea2 = float (input ("Ingrese nota de tarea 2: "))
tarea3 = float (input ("Ingrese nota de tarea 3: "))

#Calcula el promedio, pero aún no lo muestra

promediotarea = (tarea1 + tarea2 + tarea3) / 3

#Solicitamos al usuario las 2 notas solemnes

solemne1 = float (input ("Ingrese nota solemne 1: "))
solemne2 = float (input ("Ingrese nota solemne 2: "))

#Muestra los dos promedios y notas solemnes, antes de entregar nota de presentación

print (f"Promedio lab: {promediolab:.2f}")#Resultados en f string, para acortar decimales a dos cifras

print (f"Promedio tarea: {promediotarea:.2f}")#Resultados en f string, para acortar decimales a dos cifras

print ("Nota solemne 1:", solemne1)
print ("Nota solemne 2:", solemne2)

#Realizamos el cálculo correspondiente para sacar los porcentajes y mostrar la nota de presentación

presentación = promediolab * 0.15 + promediotarea * 0.15 + solemne1 * 0.35 + solemne2 * 0.35

#Finalmente mosstramos la nota de presentación

print (f"La nota de presentación es: {presentación:.1f}") #Resultados en f string, para acortar decimales a una cifra
