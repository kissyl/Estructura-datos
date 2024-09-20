class Animal:
    def __init__(self, nombre: str, tipo: str, edad: int):
        self.nombre = nombre
        self.tipo = tipo
        self.edad = edad

    def __str__(self):
        return f"{self.nombre} (es {self.tipo} y tiene {self.edad} años)"

class Nodo:
    def __init__(self, animal):
        self.animal = animal
        self.next = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar_animal(self, animal):
        if self.existe_animal(animal):
            print(f"El animal {animal.nombre} ya está registrado")
            return

        nuevo_animal = Nodo(animal)
        nuevo_animal.next = self.cabeza
        self.cabeza = nuevo_animal
        print(f"Animal {animal.nombre} agregado a la lista")

    def agregar_animales(self, animales):
        for animal in animales:
            self.agregar_animal(animal)

    def existe_animal(self, animal):
        actual = self.cabeza
        while actual is not None:
            if actual.animal.nombre == animal.nombre:  
                return True
            actual = actual.next
        return False

    def mostrar_animales(self):
        self._mostrar_animales_recursivo(self.cabeza)

    def _mostrar_animales_recursivo(self, nodo):
        if nodo is not None:
            print(nodo.animal)
            self._mostrar_animales_recursivo(nodo.next)

    def mostrar_animales_bucle(self):
        actual = self.cabeza
        if actual is None:
            print("No hay animales en la lista.")
            return

        while actual is not None:
            print(actual.animal)
            actual = actual.next

def agregar_animales_a_lista(zoologico):
    while True:
        print("-" * 80)
        print("--- Agregar Animal al Zoológico ---")
        print()
        nombre = input("Nombre del animal: ")
        tipo = input("Tipo de animal (Felino, Mamifero, Ave, etc.): ")
        edad = int(input("Edad del animal: "))

        nuevo_animal = Animal(nombre, tipo, edad)
        zoologico.agregar_animal(nuevo_animal)

        continuar = input("¿Desea agregar otro animal? (s/n): ")
        if continuar != 's':
            break

lista_de_animales = [
    Animal("León", "Felino", 5),
    Animal("Elefante", "Mamífero", 10),
    Animal("Águila", "Ave", 3),
    Animal("Vaca", "Mamifero", 4),
    Animal("Pantera", "Felino", 6)
]

zoologico = ListaEnlazada()
print("-" * 80)
print("Lista de animales en el zoologico:")
print()
for animal in lista_de_animales:
    print(animal)

agregar_animales_a_lista(zoologico)
zoologico.agregar_animales(lista_de_animales)

print("-" * 80)
print("Animales en el zoológico (Recursivo):")
zoologico.mostrar_animales()

print("-" * 80)
print("Animales en el zoológico (Bucle):")
zoologico.mostrar_animales_bucle()