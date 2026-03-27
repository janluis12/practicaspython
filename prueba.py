#declaramos nuestro coche con su clase respectiva, las clase las iniciales siempre con mayuscula
class Coche():

    # Método constructor
    # Se ejecuta automáticamente cuando creamos un objeto
    # Sirve para dar valores iniciales a los atributos del objeto
    def __init__(self, color,estado,ruedas,ancho,largo):
        # propiedades del coche
        self.color = color       # atributo público
        self.estado = estado     # atributo público
        self.__ruedas = ruedas   # atributo privado
        self.__ancho = ancho     # atributo privado
        self.__largo = largo     # atributo privado
    
     # Método para mostrar en pantalla las propiedades del coche
    def mostrar_propiedades(self):
        print("Color:", self.color)
        print("Estado:", self.estado)
        print("Ruedas:", self.__ruedas)
        print("Ancho:", self.__ancho)
        print("Largo:", self.__largo)

        

# Creamos un objeto llamado micoche1
# Este objeto pertenece a la clase Coche
micoche1 = Coche("rojo","encendido",4,240,150)
micoche2 = Coche("verde","apagado",4,100,200)

# Llamamos al método mostrarpropiedades para ver los datos del coche
micoche1.mostrar_propiedades()
print("---------------segundo coche----------------")
micoche2.mostrar_propiedades()
