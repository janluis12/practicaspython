class animales():
    def __init__(self,animal, color):
        self.animal = animal
        self.color = color
        
    def accionesanimales(self):
        print("miau", self.animal, self.color)

gato = animales("hace gato","negro")
gato.accionesanimales()


class perro(animales):

    def accionesanimales(self):
        print("guau", self.animal, self.color)

perro1 = perro("hace perro","marron")
perro1.accionesanimales()
