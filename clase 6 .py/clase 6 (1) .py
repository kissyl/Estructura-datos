class Pila:
    def __init__(self):
        self.elementos = []

    def insertar(self, dato):
        self.elementos.append(dato)

    def esta_vacia(self):
        return len(self.elementos) == 0
    
    def quitar(self):
        if self.esta_vacia():
            print("Lista vacía")
            return None
        return self.elementos.pop()
    
    def limpiar(self):
        del self.elementos[:]

    def cima(self):
        if self.esta_vacia():
            print("LISTA VACÍA")
            return None
        return self.elementos[-1]
    
    def mostrar(self):
        print("Los elementos son:")
        print(self.elementos)


p = Pila()
p.insertar("k")
p.insertar("i")
p.insertar("s")
p.insertar("s")
p.insertar("y")

print("Mostrando elementos:")
p.mostrar()

quitar_elemento = p.quitar()
print (f"\ Quitar elemento() {quitar_elemento} ")
print("Mostrando ")
p.mostrar()