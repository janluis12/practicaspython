class persona():
    def __init__(self, nombre, edad, lugar_residencia):
        self.nombre = nombre
        self.edad = edad
        self.lugar_residencia = lugar_residencia

    def mostrar_datos(self):
        print("nombre:", self.nombre)
        print("edad:", self.edad)
        print("lugar residencia", self.lugar_residencia)



class empleado(persona):

    def __init__(self, salario,antiguedad, nombre_empleado, edad_empleado,residencia_empleado):

        super().__init__(nombre_empleado,edad_empleado,residencia_empleado)
        self.salario = salario
        self.antiguedad = antiguedad

    def mostrar_datos(self):
        super().mostrar_datos()
        print("salario:", self.salario,)
        print("antiguedad",self.antiguedad)

persona1 = persona("janluis",20,"chile")
empleado1 = empleado(1500,2,"janluis",26,"chile")
empleado1.mostrar_datos()
persona1.mostrar_datos()
