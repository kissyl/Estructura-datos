class Nodo:
    def __init__(self, tarea):
        self.tarea = tarea
        self.next = None

class Cola:
    def __init__(self):
        self.primero = None
        self.ultimo = None
    
    def esta_vacia(self):
        return self.primero is None
    
    def encolar(self, tarea):
        nuevo_nodo = Nodo(tarea)
        if self.esta_vacia():
            self.primero = nuevo_nodo
        else:
            self.ultimo.next = nuevo_nodo
        self.ultimo = nuevo_nodo
    
    def desencolar(self):
        if self.esta_vacia():
            return None
        tarea = self.primero.tarea
        self.primero = self.primero.next
        if self.primero is None:
            self.ultimo = None
        return tarea

class Tarea:
    def __init__(self, id, tiempo_ejecucion, nivel_prioridad, tiempo_llegada):
        self.id = id
        self.tiempo_ejecucion = tiempo_ejecucion
        self.nivel_prioridad = nivel_prioridad
        self.tiempo_llegada = tiempo_llegada

class SistemaColasPrioridad:
    def __init__(self):
        self.colas = {
            'alta': Cola(),
            'media': Cola(),
            'baja': Cola()
        }
        self.tiempo_actual = 0

    def agregar_tarea(self, tarea):
        self.colas[tarea.nivel_prioridad].encolar(tarea)

    def procesar_tareas(self):
        prioridades = ['alta', 'media', 'baja']
        
        for prioridad in prioridades:
            print(f"\nProcesando tareas de prioridad {prioridad}:")
            cola = self.colas[prioridad]
            while not cola.esta_vacia():
                tarea = cola.desencolar()
                tiempo_espera = self.tiempo_actual - tarea.tiempo_llegada
                print(f"  Tarea {tarea.id}:")
                print(f"    Nivel de Prioridad: {tarea.nivel_prioridad}")
                print(f"    Tiempo de Ejecución: {tarea.tiempo_ejecucion} Horas")
                print(f"    Tiempo de Espera: {tiempo_espera} Horas")
                print(f"    Tiempo Total: {tiempo_espera + tarea.tiempo_ejecucion} Horas")

                self.tiempo_actual += tarea.tiempo_ejecucion

sistema = SistemaColasPrioridad()

sistema.agregar_tarea(Tarea(1, 3, "alta", 0))
sistema.agregar_tarea(Tarea(2, 2, "media", 1))
sistema.agregar_tarea(Tarea(3, 1, "baja", 2))
sistema.agregar_tarea(Tarea(4, 2, "alta", 3))
sistema.agregar_tarea(Tarea(5, 4, "media", 4))

sistema.procesar_tareas()