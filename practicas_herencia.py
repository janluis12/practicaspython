class Banco():

    def __init__(self,titular,saldo):
        self.titular = titular
        self.__saldo = saldo

    def get_saldo(self):
        print("saldo:", self.__saldo)

    def get_titular(self):
        print("Titular", self.titular)

    def depositar(self):
        try:
            nuevomonto = int(input("Ingresa el monto a depositar"))
        except ValueError:
            print("Por favor intentalo nuevamente ya que no admitimos caracteres de tipo texto, solo numericos.")
            return
        if nuevomonto > 0:
            print("monto depositado con exito")
            self.__saldo += nuevomonto
        else:
            print("monto ingresado incorrecto vuelve a intentarlo nuevamente")

    def retirar(self):
        try:
            montoretirar = int(input("Ingresa el monto que deseas retirar"))
        except ValueError:
            print("Por favor intentalo nuevamente ya que no admitimos caracteres de tipo texto, solo numericos.")
            return

        if montoretirar > 0 and self.__saldo >= montoretirar:
            self.__saldo -= montoretirar
            print("Monto retirado con exito")
        else:
            print("el monto intentado retirar supera el total del saldo, vuelva a intentarlo nuevamente por favor")

    def get_datos(self):
        print("Titular", self.titular)
        print("Saldo", self.__saldo)

    def set_nuevotitular(self):
        nuevotitular = input("ingresa el nuevo titular")
        self.titular = nuevotitular
        print("Titular cambiado con exito")

    def menu(self):
        opciones = 5
        while opciones !=0:
            print("1 - consultar saldo")
            print("2 - depositar")
            print("3 - retirar")
            print("4 - ver datos")
            print("5 - Cambiar titular")
            print("6 - Titular")
            print("0 - salir")
           
            try:
                opciones = int(input("Escoje una de las siguientes opciones por favor"))
            except ValueError:
                print("Por favor intentalo nuevamente ya que no admitimos caracteres de tipo texto, solo numericos.")
                return

            if opciones == 1:
                self.get_saldo()

            elif opciones == 2:
                self.depositar()

            elif opciones == 3:
                self.retirar()

            elif opciones == 4:
                self.get_datos()

            elif opciones == 5:
               self.set_nuevotitular()

            elif opciones == 6:
                self.get_titular()
            
            elif opciones == 0:
                print("Programa terminado")

            else:
                print("Opcion no valida, intentalo nuevamente.")
                

cuenta1 = Banco("janluis",2000)
cuenta1.menu()





