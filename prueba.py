#declaramos nuestro coche con su clase respectiva, las clase las iniciales siempre con mayuscula
class Coche():

    # Método constructor
    # Se ejecuta automáticamente cuando creamos un objeto
    # Sirve para dar valores iniciales a los atributos del objeto
    def __init__(self, color,ruedas,ancho,largo):
        # propiedades del coche
        self.color = color       # atributo público
        self.__ruedas = ruedas   # atributo privado
        self.__ancho = ancho     # atributo privado
        self.__largo = largo     # atributo privado
        self.enmarcha = False
        
    
     # Método para mostrar en pantalla las propiedades del coche
    def mostrar_propiedades(self,):
        print("Color:", self.color)
        print("Ruedas:", self.__ruedas)
        print("Ancho:", self.__ancho)
        print("Largo:", self.__largo)

    def arrancar(self,arrancamos):
        self.enmarcha = arrancamos

        if(self.enmarcha):
            chequeo=self.__chequeo_interno()

        if(self.enmarcha and chequeo):
            return "el coche esta en marcha"
        elif(self.enmarcha and chequeo ==False):
            return "algo esta mal en el chequeo no podemos arrancar"
        else:
            return "el coche esta apagado"
        
        #aqui esta encapsulada mi variable __
    def __chequeo_interno(self):
        print("realizando chequeo interno")
        self.gasolina ="ok"
        self.aceite = "ok"
        self.puertas ="cerradas"

        if(self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="cerradas"):
            return True
        else:
            return False
    

# Creamos un objeto llamado micoche1
micoche1 = Coche("rojo",4,240,150)
# Este objeto pertenece a la clase Coche


# Llamamos al método mostrarpropiedades para ver los datos del coche

print(micoche1.arrancar(True))
micoche1.mostrar_propiedades()


