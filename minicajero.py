class Minicajero():

    def __init__(self, saldo,titular):

        self.__saldo = saldo
        self.titular = titular

    def mostrar_datos(self):
        print("Titular:", self.titular)
        print("Saldo:", self.__saldo)
        

    def consultar_saldo(self):
        print("Saldo:", self.__saldo)

    def depositar_saldo(self):
        try:
            depositar = int(input("Ingresa el monto a depositar"))
        except ValueError:
            print("Lo sentimos no se aceptan caracteres tipo texto, solo numericos intentalo de nuevo por favor")
            return
        
        if depositar >0:
            self.__saldo += depositar
            print("Saldo depositado con exito")
            print("Saldo actual:", self.__saldo)

        else:
            print("El saldo intentado a depositar es incorrecto intentalo de nuevo")

    def retirar_saldo(self):

        try:
            retirar = int(input("Ingresa el monto a retirar"))
            if retirar <= self.__saldo and retirar > 0:
                self.__saldo -= retirar
                print("Saldo retirado con exito")
                print("Saldo actual:", self.__saldo)

            else:
                print("supera el maximo de tu cuenta")
        except ValueError:
            print("Lo sentimos no se aceptan caracteres tipo texto, solo numericos intentalo de nuevo por favor")
            return
        

    def cambiar_titular(self):
        nuevotitular = input("Ingresa el nuevo titular por favor")
        self.titular = nuevotitular
        print("Titular cambiado con exito")
        
    def menu(self):
        opciones = -1
        while opciones !=0:
            print("1 - consultar saldo")
            print("2 - depositar saldo")
            print("3 - retirar saldo")
            print("4 - cambiar titular")
            print("5 - Mostrar datos")
            print("0 - Salir")
            try:
                opciones = int(input("Escoje una de las siguientes opciones"))
                if opciones == 1:
                    self.consultar_saldo()

                elif opciones == 2:
                    self.depositar_saldo()

                elif opciones == 3:
                    self.retirar_saldo()

                elif opciones == 4:
                    self.cambiar_titular()

                elif opciones == 5:
                    self.mostrar_datos()

                elif opciones == 0:
                    print("Programa terminado con exito")

                else:
                    print("Opcion ingresada no valida, intentalo nuevamente.")
            except ValueError:
                print("Lo sentimos no se aceptan caracteres tipo texto, solo numericos intentalo de nuevo por favor")
                continue

            

cuenta1=Minicajero(1000,"Janluis Melendez")
cuenta1.menu()
