class Bancoestado():
    
    # Método constructor de la clase
    # Se ejecuta automáticamente al crear un objeto
    # Recibe el titular y el saldo inicial
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    # Método para consultar solo el saldo de la cuenta
    def consultar_saldo(self):
        print("Saldo:", self.saldo)

    # Método para mostrar los datos principales de la cuenta
    def consultar_datos(self):
        print("Titular:", self.titular)
        print("Saldo:", self.saldo)

    # Método para depositar saldo en la cuenta
    def depositar_saldo(self):
        try:
            # Pedimos al usuario el monto a depositar
            # float permite ingresar números con decimales
            nuevo_saldo = float(input("Ingresa el monto a depositar"))
        except ValueError:
            # Si el usuario escribe texto u otro valor inválido
            print("No se aceptan caracteres de tipo texto, solo numericos.")
            return
        
        # Validamos que el monto sea mayor que 0
        if nuevo_saldo > 0:
            print("monto transferido con exito")
            self.saldo += nuevo_saldo  # Sumamos el monto al saldo actual
        else:
            print("monto ingresado incorrecto")

    # Método para retirar saldo
    # Aún no está implementado
    def retirar_saldo(self):
        pass

    # Método que muestra un menú con opciones al usuario
    def menu_opciones(self):
        opciones = -1  # Valor inicial para entrar al while
        
        # El menú se repetirá mientras la opción no sea 0
        while opciones != 0:
            print("1 - Consultar saldo")
            print("2 - Depositar")
            print("3 - Retirar")
            print("4 - Ver datos")
            print("5 - Ver datos cuenta 2")
            print("0 - Salir")

            try:
                # Pedimos al usuario que elija una opción del menú
                opciones = int(input("Ingresa una de las siguientes opciones"))
            except ValueError:
                # Si el usuario escribe texto, se muestra error y vuelve al menú
                print("No se admiten caracteres tipo texto, solo se permiten numericos, intentalo nuevamente")
                continue
            
            # Si elige 1, consulta el saldo de esta cuenta
            if opciones == 1:
                self.consultar_saldo()

            # Si elige 2, deposita saldo en esta cuenta
            elif opciones == 2:
                self.depositar_saldo()

            # Si elige 3, intenta retirar saldo
            elif opciones == 3:
                self.retirar_saldo()

            # Si elige 4, muestra los datos de esta cuenta
            elif opciones == 4:
                self.consultar_datos()

            # Si elige 5, muestra los datos de la cuenta llamada chile
            elif opciones == 5:
                chile.consultar_datos()

            # Si elige 0, termina el programa
            elif opciones == 0:
                print("Programa terminado con exito")
            
            # Si escribe una opción no válida
            else:
                print("Opcion elegida incorrecta vuelva a intentarlo por favor")


# Clase hija que hereda de Bancoestado
class bancochile(Bancoestado):

    # Constructor de la clase hija
    # Usa super() para reutilizar el constructor de la clase padre
    def __init__(self, titular, saldo):
        super().__init__(titular, saldo)
        
    # Sobrescribimos el método consultar_datos
    # Primero muestra los datos normales de la cuenta
    # Luego agrega el nombre del banco
    def consultar_datos(self):
        super().consultar_datos()
        print("Banco: Chile")



# Creamos un objeto de la clase Bancoestado
estado = Bancoestado("Janluis", 2000)

# Creamos un objeto de la clase bancochile
chile = bancochile("Sofia", 500)

# Ejecutamos el menú sobre la cuenta estado
estado.menu_opciones()