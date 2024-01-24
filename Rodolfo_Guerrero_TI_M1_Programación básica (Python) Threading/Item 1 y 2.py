#permite que una aplicación ejecute simultáneamente varias operaciones en el mismo espacio de proceso
import threading 

#Print para reconocer el código
print("\n====Código Item 1, ingrese la temperatura en grados Celsius y se traspasará a grados Fahrenheit====\n")

#Función para ejecutar el script 1
def run_script1():
    
    """Item 1: Confecciona un programa que reciba la temperatura en grados Celsius, y la traspase a grados Fahrenheit"""

    #Solicitamos al usuario ingresar grados en celsius
    celcius = float(input("ingrese grados Celsius y luego presione ENTER: "))

    #Realizamos la conversión con la formula de Celsius a Fahrenheit

    fahrenheit = (celcius * 1.8) + 32 #es igual a decir Fahrenheit = 9/5 * C° + 32

    #Mostramos el resultado en pantalla

    print ("El resultado convertido de Celsius a Fahrenheit es:", fahrenheit,"°F ")
    #Declaramos paso al siguiente código
    pass

    #Print para reconocer el código y/o salto de página para iniciar el segundo código
    print("\n====Código Item 2, Escriba tres números por teclado y calcularé su promedio====\n")

## Función para ejecutar el script 2
def run_script2(): 

    """Ítem 2: Realiza un programa que reciba tres números por teclado y calcule su promedio."""
    
    #Solicitamos al usuario los tres números
    
    num1 = float(input("ingrese número 1: "))
    num2 = float(input("ingrese número 2: "))
    num3 = float(input("ingrese número 3: "))

    #Realizamos la fórmula matemática según su jerarquía

    promedio = (num1 + num2 + num3) / 3

    #Entregamos el resultado del promedio
    #Resultado en f string para acortar decimales a dos cifras
    print (f"El resultado de este promedio es: {promedio:.2f}") 
    pass

#Se crean los hilos (Threads)
t1 = threading.Thread(target=run_script1)
t2 = threading.Thread(target=run_script2)

#Inicia los hilos
t1.start()
t2.start()

#Espera que ambos hilos terminen
t1.join()
t2.join()