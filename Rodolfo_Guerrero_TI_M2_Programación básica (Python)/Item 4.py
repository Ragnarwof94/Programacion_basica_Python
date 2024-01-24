# Escoje las 2 palabras de acuerdo a lo solicitado
palabra1 = input("Por favor, introduce la primera palabra: ")
palabra2 = input("Por favor, introduce la segunda palabra: ")

# Verificar que las palabras tienen el mismo largo
if len(palabra1) != len(palabra2):
    print("Las palabras deben tener el mismo largo.")
else:
    # Crear un diccionario de reemplazo
    reemplazo = {}
    for i in range(len(palabra1)):
        if palabra1[i] != palabra2[i]:
            reemplazo[palabra1[i]] = palabra2[i]
    
    # Solicita la frase al usuario
    frase = input("Por favor, introduce una frase: ")
    
    # Reemplaza los valores
    nueva_frase = ""
    for letra in frase:
        if letra in reemplazo:
            nueva_frase += reemplazo[letra]
        else:
            nueva_frase += letra
    
    # Imprime la nueva frase
    print(nueva_frase)
