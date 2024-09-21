class Animal:
    def __init__(self, nombre, edad, tipo):
        self.nombre = nombre
        self.edad = edad
        self.tipo = tipo

    def __str__(self):
        return f"{self.nombre} (tiene {self.edad} años y es {self.tipo})"

class Nodo:
    def __init__(self, animal):
        self.animal = animal
        self.next = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar(self, animal):
        if self.buscar_animal(animal):
            print(f"El animal {animal.nombre} ya se encuentra registrado")
            return
        
        nuevo_animal = Nodo(animal)
        nuevo_animal.next = self.cabeza
        self.cabeza = nuevo_animal
        print(f"Animal {animal.nombre} añadido a la lista")

    def agregar_animales(self, animales):
        for animal in animales:
            self.agregar(animal)

    def mostrar_animales(self):
        print("Animales en el zoológico (recursivo):")
        self._mostrar_animales_recursivo(self.cabeza)
        
    def buscar_animal(self, animal):
        actual = self.cabeza
        while actual is not None:
            if actual.animal.nombre == animal.nombre:
                return True
            actual = actual.next
        return False

    def _mostrar_animales_recursivo(self, nodo):
        if nodo is not None:
            print(nodo.animal)
            self._mostrar_animales_recursivo(nodo.next)

    def mostrar_animales_bucle(self):
        print("Animales en el zoológico (bucle):")
        actual = self.cabeza
        while actual is not None:
            print(actual.animal)
            actual = actual.next
        
def agregar_animales_a_lista(zoologico):
    while True:
        print("\n---♡-- Agregar Animal al Zoológico k --♡---")
        nombre = input("Nombre del animal: ")
        tipo = input("Tipo de animal (Felino, Mamifero, Ave, Reptil, Anfibio, Pez): ")
        edad = int(input("Edad del animal: "))
        nuevo_animal = Animal(nombre, edad, tipo)
        zoologico.agregar(nuevo_animal)

        continuar = input("¿Desea agregar otro animal? (si/no): ")
        if continuar.lower() != 's':
            break

if __name__ == "__main__":
    Lista_de_animales = [
        Animal("Búho", 2, "Ave"),
        Animal("Jirafa", 4, "Mamifero"),
        Animal("Leopardo", 5, "Felino"),
        Animal("Rana", 1, "Anfibio"),
        Animal("Serpiente", 3, "Reptil") 
    ]

    zoologico = ListaEnlazada()
    
    print("-" * 30)
    print("♡♡ Lista de animales ♡♡")
    print("-" * 30)
    for animal in Lista_de_animales:
        print(animal)

    zoologico.agregar_animales(Lista_de_animales)

    print("\n" + "-" * 30)
    zoologico.mostrar_animales()
    
    print("\n" + "-" * 30)
    zoologico.mostrar_animales_bucle()

    print("\n" + "-" * 30)
    agregar_animales_a_lista(zoologico)

    print("\n" + "-" * 30)
    print("Lista final de animales:")
    zoologico.mostrar_animales_bucle()