#Clase vehiculo, Padre
class Vehiculo:
    #Metodo constructor de la clase padre
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.encendido = False
    #Metodo arrancar de nuestro vehiculo
    def arrancar(self):
        self.encendido = True
        print(f"El {self.marca} {self.modelo} ha arrancado. ¡Brum brum!")

#Clase hija de (Vehiculo), esta hereda, su constructor
class CocheElectrico(Vehiculo):
    #constructor clase hija, pero herendado esto de clase vehiculo, pero asi mismo añadiendo una nueva propiedad que seria capacidad bateria
    def __init__(self, marca, modelo, capacidad_bateria):
        # Llamamos al constructor de la clase padre para que haga su trabajo
        super().__init__(marca, modelo)
        
        # Ahora, solo nos preocupamos de lo que es exclusivo del Coche Electrico
        self.capacidad_bateria = capacidad_bateria

    def arrancar(self):
        # Queremos el arranque normal, pero con un sonido distinto
        super().arrancar() # Esto ejecutará el código de Vehiculo.arrancar()
        print(f"Silencio total... la batería está al {self.capacidad_bateria}%.")

bmw = CocheElectrico("bwm","a200",100)
bmw.arrancar()