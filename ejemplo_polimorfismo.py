# Definimos la clase coche
class coche():
    
    # Método desplazamiento
    # Este método indica cómo se desplaza un coche
    def desplazamiento(self):
        print("me desplazo utilizando cuatro ruedas")


# Definimos la clase moto
class moto():
    
    # Método desplazamiento
    # Este método indica cómo se desplaza una moto
    def desplazamiento(self):
        print("me desplazo en dos ruedas")


# Función que recibe cualquier objeto vehiculo
# y llama a su método desplazamiento()
# Aquí se aplica el polimorfismo, porque puede funcionar
# tanto con un coche como con una moto
def desplamazamientovehiculo(vehiculo):
    vehiculo.desplazamiento()


# Ahora la variable mivehiculo guarda un objeto de tipo moto
mivehiculo = coche()


# Llamamos a la función y le pasamos el objeto moto
# La función ejecutará el método desplazamiento()
# del objeto recibido
desplamazamientovehiculo(mivehiculo)