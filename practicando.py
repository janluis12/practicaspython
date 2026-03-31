class Alumno():
    
    # metodo constructor de la clase Alumno
    def __init__(self, nombre, apellido, nota):
        self.nombre = nombre
        self.apellido = apellido
        self.__nota = 0
        self.set_nota(nota)
        
    # metodo privado para mostrar los datos del alumno
    def __datos_alumnos(self):
        print("Nombre:", self.nombre)
        print("Apellido:", self.apellido)
        print("Nota:", self.__nota)
        
    # metodo publico para acceder a los datos
    def mostrar_datos(self):
        self.__datos_alumnos()
        
    # getter de la nota
    def get_nota(self):
        return self.__nota
        
    # setter de la nota
    def set_nota(self, nueva_nota):
        if 0 <= nueva_nota <=100:
            self.__nota = nueva_nota
        else:
            print("la nota debe estar entre 0 y 100") 
        

alumno1 = Alumno("janluis", "melendez", 80)
alumno1.set_nota(50)
alumno1.mostrar_datos()
print("Nota actual:", alumno1.get_nota())