# Se imprime un mensaje indicando el comienzo de la sección del código relacionada con el programa.
print("\n====Contraseña Segura====\n")

def run_script1():

    """Crear un programa que determine si una contraseña en segura o no. Se considera segura si tiene al menos una mayúscula, una minúscula y un número. Se debe utilizar funciones."""

    # Definimos una función que verifica si la contraseña contiene al menos una letra mayúscula
    def contiene_mayuscula(password):
        for caracter in password:
            if caracter.isupper():  # Verifica si el caracter es una letra mayúscula
                return True  # Retorna True si encuentra al menos una letra mayúscula
        return False  # Si no se encontró ninguna letra mayúscula, retorna False al final

    # Definimos una función que verifica si la contraseña contiene al menos una letra minúscula
    def contiene_minuscula(password):
        for caracter in password:
            if caracter.islower():  # Verifica si el caracter es una letra minúscula
                return True  # Retorna True si encuentra al menos una letra minúscula
        return False  # Si no se encontró ninguna letra minúscula, retorna False al final

    # Definimos una función que verifica si la contraseña contiene al menos un número
    def contiene_numero(password):
        for caracter in password:
            if caracter.isdigit():  # Verifica si el caracter es un dígito numérico
                return True  # Retorna True si encuentra al menos un número
        return False  # Si no se encontró ningún número, retorna False al final

    # Definimos una función que verifica si la contraseña es segura según los criterios dados
    def es_segura(password):
        # La contraseña es segura si contiene al menos una mayúscula, una minúscula y un número
        return contiene_mayuscula(password) and contiene_minuscula(password) and contiene_numero(password)

    # Pedimos al usuario que ingrese una contraseña
    contrasena = input("Ingrese la contraseña: ")

    # Verificamos si la contraseña es segura utilizando la función es segura
    if es_segura(contrasena):
        print("La contraseña es segura.")
    else:
        print("La contraseña no es segura. Asegúrate de tener al menos una mayúscula, una minúscula y un número.")


def run_script2():

    # Se imprime un mensaje indicando el comienzo de la sección del código relacionada con el programa.
    print("\n====Suma Recursiva, para terminar presione la tecla ESPACIO y luego ENTER====\n")

    """Escribir un programa que lea números ingresados y luego devuelva el total. Se debe desarrollar usando recursión. No se pueden utilizar ciclos. Se ingresar números hasta que el usuario ingrese un espacio. Si el primer input es un espacio, entonces imprime 0."""

        # Definimos una función recursiva llamada suma_recursiva
    def suma_recursiva():
        # Pedimos al usuario que ingrese un número (o un espacio para salir)
        num = input("Ingrese un número (o espacio para salir): ")

        # Si el usuario ingresa un espacio, retornamos 0 para terminar la recursión
        if num == " ":
            return 0

        try:
            num = int(num)  # Intenta convertir el input en un número entero
            # Llama recursivamente a la función para sumar el siguiente número y lo retorna
            return num + suma_recursiva()
        except ValueError:
            # Maneja el caso de una entrada no numérica mostrando un mensaje de error
            print("Entrada inválida. Por favor ingrese un número o un ESPACIO (Tecla espacio y presione ENTER).")
            # Llama recursivamente nuevamente
            return suma_recursiva()

    # Llamamos a la función suma_recursiva y guardamos el resultado en la variable total
    total = suma_recursiva()

    # Imprimimos el total de la suma
    print(f"La suma total es: {total}")


def run_script3():

    # Se imprime un mensaje indicando el comienzo de la sección del código relacionada con el programa.
    print("\n====Cuenta Bancaria====\n")
    
    """Crear una clase llamada “cuenta”. Al instanciar la clase se debe proveer el número de cuenta, el nombre el titular, saldo inicial, tipo cuenta (ahorro, corriente, inversiones). Crear tres métodos depositar, retirar, obtener balance. Si en la cuenta1 hay un saldo inicial de 10 y se hace un depósito de 20 y un retiro de 5, entonces al obtener el balance debe mostrar un saldo de 25. Imprimir la información con todos los datos de usuarios y balances."""

    class Cuenta:
        def __init__(self, numero_cuenta, titular, saldo_inicial, tipo_cuenta):
            self.numero_cuenta = numero_cuenta
            self.titular = titular
            self.saldo_inicial = saldo_inicial
            self.saldo = saldo_inicial
            self.tipo_cuenta = tipo_cuenta

        def depositar(self, cantidad):
            self.saldo += cantidad

        def retirar(self, cantidad):
            if cantidad <= self.saldo:
                self.saldo -= cantidad
            else:
                print("Saldo insuficiente.")

        def obtener_balance(self):
            return self.saldo

    # Crear una instancia de cuenta con saldo inicial de 10
    cuenta1 = Cuenta("18567521", "Rodolfo Guerrero", 10, "Corriente")

    # Pedir al usuario que ingrese el monto a depositar
    monto_deposito = float(input("Ingrese el monto a depositar: "))
    cuenta1.depositar(monto_deposito)

    # Pedir al usuario que ingrese el monto a retirar
    monto_retiro = float(input("Ingrese el monto a retirar: "))
    cuenta1.retirar(monto_retiro)

    # Obtener el balance de la cuenta1
    balance_cuenta1 = cuenta1.obtener_balance()

    # Imprimir información
    print(f"Número de Cuenta: {cuenta1.numero_cuenta}")
    print(f"Titular: {cuenta1.titular}")
    print(f"Tipo de Cuenta: {cuenta1.tipo_cuenta}")
    print(f"Saldo: {balance_cuenta1:.0f}")
    print("\n===Hasta Pronto===\n")


# Define una función llamada main.
def main():
    # Llama a las funciones run_script1, run_script2 y run_script3 en secuencia.
    run_script1()
    run_script2()
    run_script3()

    # Imprime un mensaje indicando que todos los scripts han terminado.
    print("\n===¡Todos los scripts han terminado!===\n")

# Llama a la función main para ejecutar los scripts.
main()