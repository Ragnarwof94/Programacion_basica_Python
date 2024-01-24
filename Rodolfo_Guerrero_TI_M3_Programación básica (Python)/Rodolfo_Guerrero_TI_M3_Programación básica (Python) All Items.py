 # Se imprime un mensaje indicando el comienzo de la sección del código relacionada con el programa.
print("\n====Código Item 1, Escribir un programa que lea entre 10 a 20 números ingresados por el usuario, los almacene en una lista y los muestre ordenados de mayor o menor====\n")

def run_script1():

    '''Escribir un programa que lea entre 10 a 20 números ingresados por el usuario, los almacene en una lista y los muestre ordenados de mayor o menor. Debe recibir el ingreso de números hasta que el usuario ingrese 0. Pero el 0 no se debe mostrar en pantalla.'''

    # Crear una lista vacía para almacenar los números
    numeros = []

    # Leer números hasta que el usuario ingrese 0
    while True:
        try:
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
        except ValueError:
            print("Por favor, ingrese un número válido")

    #Si la lista  tiene menos de 10 números, se muestre un mensaje y se termine el programaS
    if len (numeros) < 10:
        print ("No ha ingresado suficientes números, se requieren al menos 10")
        return
            
    # Ordenar la lista de mayor a menor
    numeros.sort(reverse=True)

    # Mostrar los números ordenados
    print("\nLos números ordenados de mayor a menor son:")
    for numero in numeros:
        print(numero)


def run_script2():
      
    # Se imprime un mensaje indicando el comienzo de la sección del código relacionada con el programa.
    print("\n====Código Item 2, Escribir un programa que almacene palabras ingresadas por el usuario sin repetir las palabras====\n")

    '''Escribir un programa que almacene palabras ingresadas por el usuario. Debe recibir ingreso de palabras hasta que el usuario ingrese tres asteriscos ***. Luego de esto, las palabras se deben mostrar por pantalla una única vez. Es decir que, si el usuario ingresó palabras repetidas, se deben mostrar solo una vez.'''

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

def run_script3():

    # Se imprime un mensaje indicando el comienzo de la sección del código relacionada con el juego de Scrabble.
    print("\n====Código item 3, ¡Juguemos Scrabble!====\n")

    # Se define una función llamada calcular_puntaje que toma una palabra como argumento.
    def calcular_puntaje(palabra):
        # Se crea un diccionario que asocia letras con sus respectivos valores de puntaje en Scrabble.
        diccionario = {
            'A': 1, 'E': 1, 'I': 1, 'L': 1, 'N': 1, 'O': 1, 'R': 1, 'S': 1, 'T': 1, 'U': 1,
            'D': 2, 'G': 2,
            'B': 3, 'C': 3, 'M': 3, 'P': 3,
            'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
            'K': 5,
            'J': 8, 'X': 8,
            'Q': 10, 'Z': 10
        }

        # Se inicializa el puntaje en 0.
        puntaje = sum(diccionario.get(letra.upper(), 0) for letra in palabra)  # Se calcula el puntaje.

        return puntaje  # Se retorna el puntaje total.

    # Se solicita al usuario que ingrese una palabra.
    palabra = input("Por favor, ingresa una palabra: ")

    # Se imprime el puntaje de la palabra ingresada utilizando la función calcular_puntaje.
    print(f'El puntaje de "{palabra}" es {calcular_puntaje(palabra)}')



def run_script4():     

    # Se imprime un mensaje indicando el comienzo de la sección del código relacionada con el programa de anagramas.
    print("\n====Código item 4, ¡Anagramas!====\n")      

    # Se define una función llamada son_anagramas que toma dos palabras como argumentos y verifica si son anagramas.
    def son_anagramas(palabra1, palabra2):
        # La función compara si las palabras tienen los mismos caracteres cuando están ordenadas.
        return sorted(palabra1) == sorted(palabra2)

    # Se solicita al usuario que ingrese dos palabras.
    palabra1 = input("Por favor, ingresa la primera palabra: ")
    palabra2 = input("Por favor, ingresa la segunda palabra: ")

    # Se llama a la función son_anagramas para verificar si las palabras son anagramas.
    if son_anagramas(palabra1, palabra2):
        print(f'"{palabra1}" y "{palabra2}" son anagramas.')  # Si son anagramas, se imprime este mensaje.
    else:
        print(f'"{palabra1}" y "{palabra2}" no son anagramas.')  # Si no son anagramas, se imprime este mensaje.


def run_script5():

    # Se imprime un mensaje indicando el comienzo de la sección del código relacionada con el programa de suma de números.
    print("\n====Código item 5, Construir un programa en donde el usuario ingrese número por pantalla y el programa devuelva la suma de cada número ingresado por el usuario====\n")     

    # Se inicializa una variable llamada 'suma' que almacenará la suma de los números ingresados por el usuario.
    suma = 0

    # Se inicia un bucle infinito que continuará hasta que se rompa explícitamente con 'break'.
    while True:
        # Se solicita al usuario que ingrese un número. Si presiona Enter sin ingresar nada, el bucle se romperá.
        numero = input("Por favor, ingresa un número (presiona enter sin nada para terminar): ")
        
        if numero == "":
            break  # Si se presiona Enter sin ingresar nada, el bucle se rompe.

        try:
            suma += int(numero)  # Se intenta convertir el valor ingresado a un número entero y se suma a 'suma'.
        except ValueError:
            # Si hay un error al convertir a entero (por ejemplo, si se ingresa un texto no numérico), se imprime un mensaje de error.
            print("¡Eso no es un número válido! Por favor, intenta de nuevo.")
            continue  # El bucle continúa sin cambiar 'suma'.

        # Se imprime la suma hasta el momento.
        print(f"La suma hasta ahora es {suma}.")

    # Cuando el bucle termina (porque el usuario presionó Enter sin ingresar nada), se imprime la suma total.
    print(f"\nLa suma total de los números ingresados es {suma}.\n")



# Define una función llamada main.
def main():
    # Llama a las funciones run_script1, run_script2, run_script3, run_script4 y run_script5 en secuencia.
    run_script1()
    run_script2()
    run_script3()
    run_script4()
    run_script5()

    # Imprime un mensaje indicando que todos los scripts han terminado.
    print("\n===¡Todos los scripts han terminado!===\n")

# Llama a la función main para ejecutar los scripts.
main()
