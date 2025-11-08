class Auto:
    def __init__(self, marca, velocidad_maxima):
        self.__marca = marca           # atributo privado
        self.__velocidad_maxima = velocidad_maxima
        self.__velocidad_actual = 0

    # obtiene velocidad
    #esta funcion define la velocidad del objeto
    def get_velocidad_actual(self):
        return self.__velocidad_actual

    # método para acelerar
    #esta funcion permite que el objeto inicie su movimiento
    def acelerar(self, aumento):
        if self.__velocidad_actual + aumento > self.__velocidad_maxima:
            self.__velocidad_actual = self.__velocidad_maxima
        else:
            self.__velocidad_actual += aumento

    # método para frenar
    #la funcion permite ejecutar un comando sobre la aceleracion de un objeto, para frenar si es true o continuar si es false
    def frenar(self, reduccion):
        if self.__velocidad_actual - reduccion < 0:
            self.__velocidad_actual = 0
        else:
            self.__velocidad_actual -= reduccion


auto1 = Auto("Toyota", 180)
auto2 = Auto("Nissan", 150)

auto1.acelerar(50)
print("Velocidad actual:", auto1.get_velocidad_actual(), "km/h")

auto1.acelerar(200)
print("Velocidad actual:", auto1.get_velocidad_actual(), "km/h")

auto1.frenar(100)
print("Velocidad actual:", auto1.get_velocidad_actual(), "km/h")
#-------------------------------------------------------------------
auto2.acelerar(40)
print("Velocidad actual:", auto1.get_velocidad_actual(), "km/h")

auto2.acelerar(200)
print("Velocidad actual:", auto1.get_velocidad_actual(), "km/h")

auto2.frenar(100)
print("Velocidad actual:", auto1.get_velocidad_actual(), "km/h")
