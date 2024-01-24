# Definir una clase llamada 'Persona'
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f'Hola, soy {self.nombre} y tengo {self.edad} años.')

# Crear una instancia de la clase 'Persona'
persona1 = Persona("Juan", 30)

# Acceder a los atributos y métodos de la instancia
print(persona1.nombre)  # Output: Juan
print(persona1.edad)    # Output: 30
persona1.saludar()      # Output: Hola, soy Juan y tengo 30 años.
