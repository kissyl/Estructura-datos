class Tarea:
    def __init__(self, descripcion: str, prioridad: int, fecha_vencimiento: str, tarea: str):
        self.descripcion = descripcion
        self.prioridad = prioridad
        self.fecha_vencimiento = fecha_vencimiento  
        self.tarea = tarea  

    def __str__(self):
        return f"Tarea: {self.tarea}, Descripción: {self.descripcion}, Prioridad: {self.prioridad}, Fecha de vencimiento: {self.fecha_vencimiento}"

class Node:
    def __init__(self, tarea):
        self.tarea = tarea
        self.next = None

class ListaDeTareas:
    def __init__(self):
        self.cabeza = None

    def es_vacio(self):
        return self.cabeza is None

    def agregar_tarea(self, tarea):
        nueva_tarea = Node(tarea)  

        if self.cabeza is None:
            self.cabeza = nueva_tarea
        else:
            actual = self.cabeza
            while actual.next is not None:
                actual = actual.next
            actual.next = nueva_tarea
        
        print(f"{tarea.tarea} ♡ se añadio a la lista. ♡")

    def mostrar_tareas(self):
        if self.cabeza is None:
            print("✘ No se encuentra tareas  en la lista. ✘")
            return
        
        actual = self.cabeza
        while actual is not None:
            print(actual.tarea)  
            actual = actual.next

    def buscar_tarea(self, nombre_tarea):
        if self.cabeza is None:
            print("✘ No se encuentra  tareas en la lista. ✘")
            return None
        
        actual = self.cabeza
        while actual is not None:
            if actual.tarea.tarea == nombre_tarea:  
                return actual.tarea
            actual = actual.next
        
        return None

    def eliminar_tarea(self, nombre_tarea):
        if self.cabeza is None:
            print("♡ ----- No se encuentran tareas para eliminar.----- ♡")
            return False
        
        if self.cabeza.tarea.tarea == nombre_tarea:  
            print(f"Tarea '{self.cabeza.tarea.tarea}'  terminada ✔  y borrada. ✔ ")
            self.cabeza = self.cabeza.next
            return True
        
        actual = self.cabeza
        while actual.siguiente is not None:
            if actual.siguiente.tarea.tarea == nombre_tarea:  
                print(f"Tarea '{actual.siguiente.tarea.tarea}' terminada ✔  y borrada. ✔ ")
                actual.siguiente = actual.siguiente.siguiente
                return True
            actual = actual.next
        
        print(f"Tarea '{nombre_tarea}'------ no hallada para eliminar -----")  
        return False

def agregar_tarea(lista_tareas):
    tarea_nombre = input("♡ Ingresa el nombre de la tarea: ♡ ")
    descripcion = input("♡ Ingresa la descripción de la tarea: ♡ ")
    prioridad = int(input(" ❀ Ingresa el nivel de prioridad ↗︎ ↘︎ (3 es alto, 2 es mediano, 1 es bajo ): "))
    fecha_vencimiento = input("❀ Ingresa la fecha de vencimiento ❀(ejemplo: 2025-10-05): ")

    nueva_tarea = Tarea(descripcion, prioridad, fecha_vencimiento, tarea_nombre)
    lista_tareas.agregar_tarea(nueva_tarea)

def mostrar_menu():
    print("\n" + " ❀ "*20)
    print(" " * 10 + "❀ MENU ❀")
    print(" ❀ "*20)
    print("1. Agregar tarea")
    print("2. Mostrar tareas")
    print("3. Buscar tarea")
    print("4. Eliminar tarea")
    print("5. Salir")

def main():
    lista_tareas = ListaDeTareas()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            agregar_tarea(lista_tareas)
        elif opcion == '2':
            lista_tareas.mostrar_tareas()
        elif opcion == '3':
            nombre_tarea = input("❃ Ingresa el nombre de la tarea que buscas ❃: ")
            tarea_encontrada = lista_tareas.buscar_tarea(nombre_tarea)
            if tarea_encontrada:
                print(f"Tarea encontrada: {tarea_encontrada}")
            else:
                print(f"Tarea '{nombre_tarea}' no se encontro.")
        elif opcion == '4':
            nombre_tarea = input("❃ Ingresa el nombre de la tarea para  eliminar: ❃")
            lista_tareas.eliminar_tarea(nombre_tarea)
        elif opcion == '5':
            print("-----♥ cerrando  el  programa ♥ -----")
            break
        else:
            print("✘ Opción inválida ✘, por favor intentar de nuevo.")

if __name__ == "__main__":
    main()
