def dibujar_matriz():
    # Solicitar el número de filas
    filas = int(input("Por favor, introduce el número de filas: "))
    
    # Solicitar el número de columnas
    columnas = int(input("Por favor, introduce el número de columnas: "))
    
    # Imprimir la cantidad de filas y columnas
    print(f'cantidad de filas:{filas}')
    print(f'cantidad de columnas:{columnas}')
    
    # Dibujar la matriz
    for i in range(filas):
        # Dibujar la línea horizontal
        print('+---' * columnas + '+')
        
        # Dibujar la línea vertical
        print('|   ' * (columnas + 1))
    
    # Dibujar la última línea horizontal
    print('+---' * columnas + '+')

# Llamar a la función para dibujar la matriz
dibujar_matriz()

