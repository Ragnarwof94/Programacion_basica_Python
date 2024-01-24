class Cuenta:
    def __init__(self, numero_cuenta, titular, saldo_inicial, tipo_cuenta):
        self.numero_cuenta = numero_cuenta
        self.titular = titular
        self.saldo_inicial = saldo_inicial
        self.saldo = saldo_inicial
        self.tipo_cuenta = tipo_cuenta

    def depositar(self, cantidad):
        try:
            if cantidad < 0:
                raise ValueError("La cantidad a depositar debe ser positiva.")
            self.saldo += cantidad
        except ValueError as e:
            print(f"Error: {e}")

    def retirar(self, cantidad):
        try:
            if cantidad < 0:
                raise ValueError("La cantidad a retirar debe ser positiva.")
            if cantidad > self.saldo:
                raise ValueError("No hay suficiente saldo para realizar el retiro.")
            self.saldo -= cantidad
        except ValueError as e:
            print(f"Error: {e}")

    def obtener_balance(self):
        return self.saldo

# Función para mostrar el menú
def mostrar_menu():
    print("\nMenú:")
    print("1. Mostrar información de la cuenta")
    print("2. Realizar depósito")
    print("3. Realizar retiro")
    print("4. Mostrar balance")
    print("5. Salir")

# Función para mostrar las opciones de cuentas disponibles
def mostrar_opciones_cuentas():
    print("\nOpciones de cuentas:")
    print("1. Cuenta 1")
    print("2. Cuenta 2")

# Pedir al usuario que ingrese los datos
print("\nDatos de cuenta 1\n")
numero_cuenta_1 = input("Ingrese el número de cuenta para la cuenta 1: ")
titular_1 = input("Ingrese el nombre del titular para la cuenta 1: ")
saldo_inicial_1 = float(input("Ingrese el saldo inicial para la cuenta 1: "))
tipo_cuenta_1 = input("Ingrese el tipo de cuenta para la cuenta 1 (ahorro, corriente, inversiones): ")

print("\nDatos de cuenta 2\n")
numero_cuenta_2 = input("Ingrese el número de cuenta para la cuenta 2: ")
titular_2 = input("Ingrese el nombre del titular para la cuenta 2: ")
saldo_inicial_2 = float(input("Ingrese el saldo inicial para la cuenta 2: "))
tipo_cuenta_2 = input("Ingrese el tipo de cuenta para la cuenta 2 (ahorro, corriente, inversiones): ")

# Crear instancias de la clase Cuenta con los datos proporcionados por el usuario
cuenta1 = Cuenta(numero_cuenta_1, titular_1, saldo_inicial_1, tipo_cuenta_1)
cuenta2 = Cuenta(numero_cuenta_2, titular_2, saldo_inicial_2, tipo_cuenta_2)

# Ciclo para interactuar con el usuario
while True:
    mostrar_menu()
    opcion = input("Ingrese el número de la opción que desea realizar: ")

    if opcion == "1":
        mostrar_opciones_cuentas()
        cuenta = input("Ingrese el número de cuenta (1 o 2) para mostrar la información: ")

        if cuenta == "1":
            print(f"\nInformación de la cuenta 1:")
            print(f"Número de cuenta: {cuenta1.numero_cuenta}")
            print(f"Titular: {cuenta1.titular}")
            print(f"Tipo de cuenta: {cuenta1.tipo_cuenta}")
            print(f"Saldo actual: {cuenta1.obtener_balance()}")

        elif cuenta == "2":
            print(f"\nInformación de la cuenta 2:")
            print(f"Número de cuenta: {cuenta2.numero_cuenta}")
            print(f"Titular: {cuenta2.titular}")
            print(f"Tipo de cuenta: {cuenta2.tipo_cuenta}")
            print(f"Saldo actual: {cuenta2.obtener_balance()}")

        else:
            print("Opción inválida. Por favor, ingrese 1 o 2 para seleccionar la cuenta.")

    elif opcion == "2":
        mostrar_opciones_cuentas()
        cuenta = input("Ingrese el número de cuenta (1 o 2): ")
        try:
            cantidad = float(input("Ingrese la cantidad a depositar: "))
            if cantidad < 0:
                raise ValueError("La cantidad a depositar debe ser positiva.")
            if cuenta == "1":
                cuenta1.depositar(cantidad)
            elif cuenta == "2":
                cuenta2.depositar(cantidad)
        except ValueError as e:
            print(f"Error: {e}")

    elif opcion == "3":
        mostrar_opciones_cuentas()
        cuenta = input("Ingrese el número de cuenta (1 o 2): ")
        try:
            cantidad = float(input("Ingrese la cantidad a retirar: "))
            if cantidad < 0:
                raise ValueError("La cantidad a retirar debe ser positiva.")
            if cantidad > cuenta1.obtener_balance() and cuenta == "1":
                raise ValueError("No hay suficiente saldo para realizar el retiro.")
            if cantidad > cuenta2.obtener_balance() and cuenta == "2":
                raise ValueError("No hay suficiente saldo para realizar el retiro.")
            if cuenta == "1":
                cuenta1.retirar(cantidad)
            elif cuenta == "2":
                cuenta2.retirar(cantidad)
        except ValueError as e:
            print(f"Error: {e}")

    elif opcion == "4":
        mostrar_opciones_cuentas()
        cuenta = input("Ingrese el número de cuenta (1 o 2) para mostrar el balance: ")
        if cuenta == "1":
            print(f"Saldo actual de la cuenta 1: {cuenta1.obtener_balance()}")
        elif cuenta == "2":
            print(f"Saldo actual de la cuenta 2: {cuenta2.obtener_balance()}")

    elif opcion == "5":
        print("\n===Hasta Pronto===\n")
        break

    else:
        print("Opción inválida. Por favor, ingrese un número del 1 al 5.")
