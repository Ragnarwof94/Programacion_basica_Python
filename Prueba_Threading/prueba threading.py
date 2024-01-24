import threading

def run_script1():
    # Crear una lista vacía para almacenar los números
    numeros = []

    # Leer números hasta que el usuario ingrese 0
    while True:
        numero = int(input("Por favor, introduce un número (o 0 para terminar): "))
        
        # Si el usuario ingresa 0, terminar el bucle
        if numero == 0:
            break
        
        # Añadir el número a la lista
        numeros.append(numero)
        
        # Si la lista tiene más de 20 números, terminar el bucle
        if len(numeros) > 20:
            print("Has ingresado más de 20 números. El programa terminará.")
            break

    # Ordenar la lista de mayor a menor
    numeros.sort(reverse=True)

    # Mostrar los números ordenados
    print("Los números ordenados de mayor a menor son:")
    for numero in numeros:
        print(numero)
        pass        

def run_script2():

        # Crear un conjunto vacío para almacenar las palabras
    palabras = set()

    # Leer palabras hasta que el usuario ingrese ***
    while True:
        palabra = input("Por favor, introduce una palabra (o *** para terminar): ")
        
        # Si el usuario ingresa ***, terminar el bucle
        if palabra == "***":
            break
        
        # Añadir la palabra al conjunto
        palabras.add(palabra)

    # Mostrar las palabras únicas
    print("Las palabras únicas ingresadas son:")
    for palabra in palabras:
        print(palabra) 
        pass



t1 = threading.Thread(target=run_script1)
t2 = threading.Thread(target=run_script2)

#Star y join 1 juntos
t1.start()
t1.join()

t2.start()
t2.join() 