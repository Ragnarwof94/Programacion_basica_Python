"""Item 4: Con lo aprendido hasta el momento, realiza un programa que de manera totalmente matemática (ocupando solo lo visto hasta el momento), muestre el digito verificador de un programa."""

#Solicitar el rut al ususario

rut = input("Ingrese su RUT sin dígito verificador: ") #Ej: 18567521

#Eliminar puntos y guión para simplificar el cálculo

rut = rut.replace(".", "")
rut = rut.split("-")[0] # Elimina todos los números después del guión

total = 0
multiplicador = 2

#Recorrer el rut de derecha a izquierda y calcular el total
#Usar multiplicadores según norma chilena

for i in reversed(rut):
    total += int(i) * multiplicador
    multiplicador += 1 #Incrementa el contador
    #Si el multiplicador alcanza el valor de 8, se reinicia en 2
    if multiplicador == 8:
        multiplicador = 2

#Calcular el resto de la división 

resto = total % 11

#Determinar el dígito verificador según la norma chilema

digito_verificador_calculado = 11 - resto

if digito_verificador_calculado == 11:
    digito_verificador_calculado ="0"
elif digito_verificador_calculado == 10:
    digito_verificador_calculado ="k"

#Se entrega resultado de dígito verificador correspondiente

print("El dígito verificador es:", digito_verificador_calculado)        
