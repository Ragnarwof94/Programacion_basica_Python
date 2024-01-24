from datetime import datetime

def es_bisiesto(año):
    # Comprobar si el año es divisible por 4
    if año % 4 == 0:
        # Comprobar si el año es un siglo
        if año % 100 == 0:
            # Comprobar si el siglo es divisible por 400
            if año % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def contar_anios_bisiestos(año_nacimiento, año_muerte):
    # Reemplazar el año de muerte con el año actual si es cero
    if año_muerte == 0:
        año_muerte = datetime.now().year
    
    # Contar la cantidad de años bisiestos
    contador = 0
    for año in range(año_nacimiento, año_muerte + 1):
        if es_bisiesto(año):
            contador += 1
    
    return contador

# Solicitar el año de nacimiento
año_nacimiento = int(input("Por favor, introduce tu año de nacimiento: "))

# Solicitar el año de muerte
año_muerte = int(input("Por favor, introduce tu año de muerte (o cero si aún estás vivo): "))

# Calcular la cantidad de años bisiestos
cantidad = contar_anios_bisiestos(año_nacimiento, año_muerte)

# Imprimir la cantidad de años bisiestos
print(f'Has vivido {cantidad} años bisiestos.')

