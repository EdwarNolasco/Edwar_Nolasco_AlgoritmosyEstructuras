from SimpleStack import *   # Importa la clase SimpleStack

class TowerOfHanoi(object):   # Define la clase TowerOfHanoi
                                # modelando la torre en 3 espigas utilizando
                                # 3 pilas
    
    def __init__(self, nDisks=3):   # Constructor que acepta el número inicial de discos (3 por defecto)
        
        self.__stacks = [None] * 3  # Crear un array de 3 pilas inicialmente vacías
        self.__labels = ["L", "M", "R"]  # Crear etiquetas para las espigas o pilas (L = Left, M = Middle, R = Right)
        self.__nDisks = nDisks  # Guardar el número total de discos
        self.reset()  # Inicializa el estado del rompecabezas
    
    def reset(self):    # Inicializa el estado del rompecabezas
        
        for spindle in range(3):  # Configura cada una de las 3 espigas
            self.__stacks[spindle] = Stack(self.nDisks)   # Empieza con una pila vacía que pueda sostener todos los discos
            if spindle == 0:   # En la primera espiga,
                for disk in range(self.__nDisks, 0, -1):   # Agrega los discos a la pila en orden descendente de tamaño
                    self.__stacks[spindle].push(disk)
    
    def label(self, spindle):  # Obtiene la etiqueta de una espiga
        
        return self.__labels[spindle]
    
    def height(self, spindle):  # Obtiene el número de discos en una espiga
        
        return len(self.__stacks[spindle])
    
    def topDisk(self, spindle):  # Obtiene el número del disco superior en una espiga o None si no hay discos
        
        if not self.__stacks[spindle].isEmpty():  # Si la pila no está vacía
            return self.__stacks[spindle].peek()  # Mira el disco en la parte superior de la pila
        
    def __str__(self):   # Muestra el estado del rompecabezas como una cadena
        
        result = ""   # Empieza con una cadena vacía
        
        for spindle in range(3):   # Recorre las espigas
            if len(result) > 0:   # Después de la primera espiga,
                result += "\n"   # separa las pilas en nuevas líneas
            result += (self.label(spindle) + ": " + str(self.__stacks[spindle]))  # Agrega la etiqueta de la espiga y el contenido de la pila a la cadena
        
        return result   # Retorna la cadena

