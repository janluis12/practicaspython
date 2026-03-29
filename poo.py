
#declaracion de nuestra primera clase
#siempre recordar que esta tienen su estado, propiedades, y comportamiento
#comportamientos, seria "que es capaz de hacer nuestro coche"

#sintaxis

class coche():
    #propiedades de la clase coche
    largocoche = 250
    ruedascoche = 4
    anchochasis = 120
    enmarcha = False

    #los metodos se crean con la palabra reservada def
     #el self hace referencia a los objectos perteneciente a la clase.
    #sintaxis de un metodo

   #aqui declaramos el metodo de la clase, con su comportamiento
    def arranchar(self):
        self.enmarcha=True

    def estado(self):
        if(self.enmarcha):
            return "el coche esta en marcha"
        else:
            return "el coche esta parado"

#Creacion de nuestro primer objecto instacia.

#mi primer objecto
micoche=coche() #esto seria una instaciacion de una clase este objecto pertenece a nuestra clase coche

#para acceder a un objecto utilizamos la nomenclatura del punto

#aqui accedemos a unas de las propiedades de nuestro coche
print("el largo del chasis es: ",micoche.largocoche)
print("el auto tiene: ",micoche.ruedascoche, " ruedas")

#accediento a nuestro primer comportamiento
micoche.arranchar()
print(micoche.estado())



""" practicas """


""" class Moto:
    
    # Declaración del método constructor perteneciente a la clase Moto
    def __init__(self, color_moto, ruedas_moto, modelo_moto, luces_moto):
        self.color_moto = color_moto
        self.ruedas_moto = ruedas_moto
        self.modelo_moto = modelo_moto
        self.luces_moto = luces_moto
        self.arrancado = True   # Estado inicial de la moto
    
    # Método para mostrar las propiedades de la moto
    def mostrar_propiedades(self):
        print("Color:", self.color_moto)
        print("Ruedas:", self.ruedas_moto)
        print("Modelo:", self.modelo_moto)
        print("Luces:", self.luces_moto)
        print("Estado:", self.mostrar_estado_moto())
    
    # Método para mostrar el estado de la moto
    def mostrar_estado_moto(self):
        if self.arrancado:
            return "moto encendida"
        else:
            return "moto apagada"


moto1 = Moto("rojo", 2, "yamaha", "encendidas")
moto1.mostrar_propiedades()
     """