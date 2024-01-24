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