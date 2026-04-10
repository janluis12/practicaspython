class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        print("El animal hace un sonido")


class Perro(Animal):
    def __init__(self, nombre, raza):
        super().__init__(nombre)   # llama al constructor de Animal
        self.raza = raza

    def hacer_sonido(self):
        super().hacer_sonido()     # llama al método de Animal
        print("Nombre:", self.nombre,"Raza:", self.raza,"hace","Guau,guau")

perro1 = Perro("Firulais", "Labrador")
perro1.hacer_sonido()