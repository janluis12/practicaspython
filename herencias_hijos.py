# Declaramos la clase padre llamada empleado
class empleado():
    
    # Método constructor de la clase empleado
    # Se ejecuta automáticamente al crear un objeto
    # Recibe nombre y cuidad como datos iniciales
    def __init__(self, nombre, cuidad):
        self.nombre = nombre
        self.cuidad = cuidad
       
    # Método para mostrar los datos del empleado
    def mostrar_datos(self):
        print("Nombre:", self.nombre)
        print("Cuidad:", self.cuidad)


# Declaramos la clase hija llamada programador
# Esta clase hereda de empleado
class programador(empleado):
    
    # Método constructor de la clase programador
    # Recibe nombre y cuidad que vienen de la clase padre
    # También recibe lenguaje y edad que son propios de esta clase
    def __init__(self, nombre, cuidad, lenguaje, edad):
        # super() llama al constructor de la clase padre
        # Así heredamos e inicializamos nombre y cuidad
        super().__init__(nombre, cuidad)
        
        # Atributos propios de la clase programador
        self.lenguaje = lenguaje
        self.edad = edad
       
    # Método para mostrar todos los datos del programador
    def mostrar_datos(self):
        # Llamamos al método mostrar_datos de la clase padre
        # para mostrar nombre y cuidad
        super().mostrar_datos()
        
        # Mostramos los atributos propios de programador
        print("lenguaje:", self.lenguaje)
        print("edad:", self.edad)

    # Método propio de la clase programador
    def programar(self):
        print("Me gusta mucho programar con python")

# Creamos un objeto llamado janluis
# Este objeto pertenece a la clase programador
janluis = programador("janluis", "chile", "Python", 26)
sofia = programador("sofia","rancagua","java",20)

# Llamamos al método para mostrar todos sus datos
janluis.mostrar_datos()
print("--------------Programadora 2---------------")
sofia.mostrar_datos()

# Llamamos al método propio de la clase programador
janluis.programar()