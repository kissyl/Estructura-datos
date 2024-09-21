class Tarea:
    def __init__(self, descripcion:str, prioridad: int, fecha_vencimiento: str):
        self.descripcion = descripcion
        self.prioridad = prioridad
        self.fecha_vencimiento = fecha_vencimiento
        self.next = None
        self.completada = False

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
        self.tareas_completadas = []


    def agregar_tarea(self, tarea: Tarea):
        if not self.cabeza:
            self.cabeza = tarea
        else:
            actual = self.cabeza
            while  actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = tarea 

    def mostrar_tarea(self):
        ac = self.cabeza
        tareas= []
        while actual:
            tareas.append(f'descripción:{actual.descripcion}, tarea proritaria: {actual.prioridad}, fecha de vencimiento: {actual.fecha_vencimiento}')
            actual= actual.siguiente
        return '\n'.join(tareas)
    
    def eliminar_tarea(self, descripcion: str) -> bool:
        if not self.cabeza:
            return False
        if self.cabeza.tarea.descripcion == descripcion:
            self.cabeza = self.cabeza.siguiente
            return True
        actual = self.cabeza
        while actual.siguiente:
            if actual.siguiente.tarea.descripcion == descripcion:
                actual.siguiente = actual.siguiente.siguiente
                return True
            actual = actual.siguiente
        return False

    def mostrar_tareas(self):
        actual = self.cabeza
        if not actual:
            print("No hay tareas en la lista.")
            return
        while actual:
            print(actual.tarea)
            actual = actual.siguiente

    def buscar_tarea(self, descripcion: str) -> Optional[Tarea]:
        actual = self.cabeza
        while actual:
            if actual.tarea.descripcion == descripcion:
                return actual.tarea
            actual = actual.siguiente
        return None

    def marcar_completada(self, descripcion: str) -> bool:
        tarea = self.buscar_tarea(descripcion)
        if tarea:
            tarea.completada = True
            self.eliminar_tarea(descripcion)
            return True
        return False

def menu():
    lista_tareas = ListaTareas()
    while True:
        print("\n--- Sistema de Gestión de Tareas ---")
        print("1. Agregar tarea")
        print("2. Eliminar tarea")
        print("3. Mostrar todas las tareas")
        print("4. Buscar tarea")
        print("5. Marcar tarea como completada")
        print("6. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            descripcion = input("Ingrese la descripción de la tarea: ")
            prioridad = int(input("Ingrese la prioridad de la tarea (1-3): "))
            fecha_vencimiento = input("Ingrese la fecha de vencimiento (YYYY-MM-DD): ")
            nueva_tarea = Tarea(descripcion, prioridad, fecha_vencimiento)
            lista_tareas.agregar_tarea(nueva_tarea)
            print("Tarea agregada con éxito.")
        
        elif opcion == "2":
            descripcion = input("Ingrese la descripción de la tarea a eliminar: ")
            if lista_tareas.eliminar_tarea(descripcion):
                print("Tarea eliminada con éxito.")
            else:
                print("No se encontró la tarea.")
        
        elif opcion == "3":
            lista_tareas.mostrar_tareas()
        
        elif opcion == "4":
            descripcion = input("Ingrese la descripción de la tarea a buscar: ")
            tarea = lista_tareas.buscar_tarea(descripcion)
            if tarea:
                print(f"Tarea encontrada: {tarea}")
            else:
                print("No se encontró la tarea.")
        
        elif opcion == "5":
            descripcion = input("Ingrese la descripción de la tarea a marcar como completada: ")
            if lista_tareas.marcar_completada(descripcion):
                print("Tarea marcada como completada y eliminada de la lista.")
            else:
                print("No se encontró la tarea.")
        
        elif opcion == "6":
            print("Gracias por usar el Sistema de Gestión de Tareas. ¡Hasta luego!")
            break
        
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    menu()