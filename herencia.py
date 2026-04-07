#codigo de lo que seran la seccion con poo herencia
#modelo,marca,enmarcha,acelera,frena
#hacer una clase vehiculos y que este tenga comportamientos

class Vehiculos():

    #Constructor

    def __init__(self, modelo,marca):

        self.modelo = modelo
        self.marca = marca
        self.acelera = False
        self.frena = False
        self.enmarcha = False
        
    def vehiculo_acelerar(self):
        self.acelera = True

    def vehiculo_frenar(self):
        self.frena =True

    def vehiculo_enmarcha(self):
        self.enmarcha =True

    def estado(self):
        print("marca", self.marca)
        print("modelo", self.modelo)
        print("acelera", self.acelera)
        print("frena", self.frena)
        print("enmarcha", self.enmarcha)


class moto(Vehiculos):
    hcaballito =""
    def caballito(self):
        self.hcaballito ="voy haciendo un caballito jajaj"

    def estado(self): # en la clase moto esto se le conoce como sobreescritura de metodo
        print("marca", self.marca)
        print("modelo", self.modelo)
        print("acelera", self.acelera)
        print("frena", self.frena)
        print("enmarcha", self.enmarcha)
        print(self.hcaballito)



mimoto1=moto("yamaha","CRB")
mimoto1.caballito()
mimoto1.vehiculo_acelerar()
mimoto1.estado()


class furgoneta(Vehiculos):


    def estado(self):
        print("marca", self.marca)
        print("modelo", self.modelo)
        print("acelera", self.acelera)
        print("frena", self.frena)
        print("enmarcha", self.enmarcha)

furgo1 = furgoneta("mitsu","china")
furgo1.vehiculo_enmarcha()
furgo1.vehiculo_acelerar()
furgo1.vehiculo_frenar()
furgo1.estado()




