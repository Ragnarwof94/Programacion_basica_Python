def main():
    print ("\n<----JUEGO DE SECUENCIA NÚMERICA---->")

    try:
        #solicitar al usuario ingrese un número del 1 al 9
        número= int(input("Con que número desea jugar, elija un número del 1 al 9: "))

        #Validación
        if número < 1 or número > 9:
            print("Por favor, ingrese un número del 1 y 9 ")
            return

        #Contador
        i = 1

        #Se solicita al usuario iniciar por el número 1
        print ("\n====¡INICIE POR EL NÚMERO 1!==== ")
        while True: 
            #solicitar que ingrese los número secuenciales según número elegido
            entrada =int(input(f"ingrese un número secuencial que no sea múltiplo de {número}: "))

            #salte los números que son multiplos del número que yo igreso
            if i % número ==0:
                i += 1

            #En caso de que ingrese un valor erróneo
            if entrada != i:
                #mensaje de error
                #el número que debía ingresar es...
                print (f"Perdiste!!!! Error en número ingresado, corresponde ingresar {i}.")
                break

            i += 1

    except ValueError:
        print("Por favor, ingrese un número válido.")
    finally: 
        print("\n====FIN DEL JUEGO====\nVuelve a intentarlo!!!!")    

if __name__ == "__main__":
    main()  
