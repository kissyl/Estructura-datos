class Animal:
    def __init__(self, nombre, edad, tipo):
        self.nombre = nombre
        self.edad = edad
        self.tipo = tipo


    def __str__(self):
        return f"{self.nombre} (tiene {self.edad} años  y es {self.tipo} )"
    
class Nodo:
    def __init__(self, animal):
        self.animal = animal
        self.next = None

class ListaEnlazadaAnimales:
    def __init__(self):
        self.cabeza = None

    def agregar(self, animal):
        if self.existe_animal(animal):
            print(f"el animal {animal.nombre} ya se encuentra registrado")
            return
        
        nuevo_animal = Nodo(animal)
        nuevo_animal.next = self.cabeza
        self.cabeza = nuevo_animal
        print(f"Animal {animal.nombre} añadido a la lista")


    def buscar_animal (self, animal):
        actual = self.cabeza
        while actual is not None:
            if actual.animal.nombre == animal.nombre:
                return True
            actual = actual.next
        return False

    def enseñar_animales_recursivo(self,  nodo):
        if nodo is None:
           print(nodo.animal)
        self.mostrar_animales_recursivo(nodo.next)
        