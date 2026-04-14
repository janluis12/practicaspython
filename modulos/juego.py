class Juegos:
    
    # Constructor de la clase juego con sus atributos
    def __init__(self, nombre, vida, poder):
        self.nombre = nombre
        self.vida = vida
        self.poder = poder

    def mostrar_personaje(self):
        print("Nombre:", self.nombre)
        print("Vida:", self.vida)
        print("Poder:", self.poder)

    def bajarvida(self, daño):
        if daño <= self.vida:
            print(self.nombre, "ha recibido daño")
            self.vida -= daño
            print("Tu vida actual es", self.vida)
        else:
            self.vida = 0
            print(self.nombre, "ha sido derrotado")
            print("Vida:", self.vida)


class Mago(Juegos):
    def __init__(self, nombre, vida, poder):
        super().__init__(nombre, vida, poder)

    def ataquesper(self, enemigo):
        print(self.nombre, "lanza un ataque tipo fuego")
        enemigo.bajarvida(30)


class Bruja(Juegos):
    def __init__(self, nombre, vida, poder):
        super().__init__(nombre, vida, poder)

    def ataquesper(self, enemigo):
        print(self.nombre, "lanza una horda de esqueletos")
        enemigo.bajarvida(10)

class Montapuercos(Juegos):
    def __init__(self, nombre, vida, poder):
        super().__init__(nombre, vida, poder)

    def ataquesper(self, enemigo):
        print(self.nombre, "lanza una super martillazo")
        enemigo.bajarvida(10)

#montapuercos=Montapuercos("Jason",100,"Martillazos")
#montapuercos.mostrar_personaje()

mago1 = Mago("Mr mago", 100, "Fuego")
mago1.mostrar_personaje()

print("----------------Personaje 2---------------")

bruja1 = Bruja("Clonis", 100, "Esqueletos")
bruja1.mostrar_personaje()

print("-----------Ataques1---------")
bruja1.ataquesper(mago1)
print("---------Ataques2-----------")
mago1.ataquesper(bruja1)
print("---------Ataques3-----------")
#montapuercos.ataquesper(mago1)