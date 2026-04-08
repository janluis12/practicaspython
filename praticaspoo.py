class Banco():
    def __init__(self, titular,saldo):
        self.titular = titular
        self.__saldo = saldo
        
    def consultar_saldo(self):
        print("Saldo:", self.__saldo)
    
    def depositar_saldo(self):
        
        while True:
            try:
                saldo_depositar = float(input("Ingresa el monto a depositar"))
            except ValueError:
                print("No se permiten caracteres tipo texto, por favor intentelo nuevamente")
                continue
            if saldo_depositar > 0:
                self.__saldo += saldo_depositar
                print("Saldo depositado con exito")
                print("Nuevo saldo", self.__saldo)
                break
            else:
                print("No se permiten valores negativos, intentalo nuevamente por favor")

    def retirar_saldo(self):
        
        while True:
            try:
                retirar_dinero=float(input("Ingresa el monto a retirar"))
            except ValueError:
                print("No se permiten caracteres tipo texto, por favor intentelo nuevamente")
                continue
            if retirar_dinero <= self.__saldo and retirar_dinero>0:
                self.__saldo -= retirar_dinero
                print("Saldo retirado con exito")
                print("Nuevo saldo", self.__saldo)
                break
            else:
                print("No se permiten valores negativos, intentalo nuevamente por favor")

    def menu(self):
        opciones = -1
        while opciones!=4:
            print("1 - Consultar saldo")
            print("2 - Depositar")
            print("3 - Retirar")
            print("4 - salir")
            try:
                opciones = int(input("Ingresa una de las siguientes opciones por favor"))
            except ValueError:
                print("No se permiten caracteres de tipo texto, intentalo nuevamente por favor")
                continue

            if opciones == 1:
                self.consultar_saldo()

            elif opciones == 2:
                self.depositar_saldo()

            elif opciones == 3:
                self.retirar_saldo()

            elif opciones == 4:
                print("Programa terminado con exito")
                break
            else:
                print("Opcion ingresada invalida, intentalo nuevamente por favor")

                
            
#Agregar mejoras a este codigo
                
            
banco1 = Banco("janluis",3000)
banco1.menu()

            
    
