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

class ListaEnlazada:
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

    def mostrar_animales_recursivo(self,  nodo):
        if nodo is None:
            print(nodo.animal)
            self.mostrar_animales_recursivo(nodo.next)

    def mostrar_animales_bucle(self):
        actual = self.cabeza
        while actual is not None:
            print(actual.animal)
            actual = actual.next
        
def agregar_animales_a_lista(zoologico):
    while True:
        print("---♡-- Agregar Animal al Zoológico k --♡---")
        nombre = input("Nombre del animal: ")
        tipo = input("Tipo de animal (Felino, Mamifero, Ave, Reptil, Anfibio, Pez): ")
        edad = int(input("Edad del animal: "))
             
        zoologico.agregar_animal(nombre, edad, tipo)

        continuar = input("¿Desea agregar otro animal? (s/n): ")
        if continuar != 's':
            break
         

Lista_de_animales = []
búho = Animal("Zeus", 2, "Ave")
jirafa = Animal("Nessa", 4, "Mamifero")
Leopardo = Animal("Garras", 5, "Felino")
Rana = Animal("Azul", 1, "Anfibio")
Serpiente = Animal("Pitou", 3, "Reptil")
    

zoologico = ListaEnlazada ()
print ("-" * 60)
print ("Lista de animales ♡ ")
print ()
for animal in Lista_de_animales:
    print (animal)

agregar_animales_a_lista(zoologico)
zoologico.agregar_animales(lista_de_animales)

print("Animales en el zoologico (recursivo):")
zoologico.mostar_animales()
