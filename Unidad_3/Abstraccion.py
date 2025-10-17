from abc import ABC, abstractmethod

# Clase abstracta
class Vehiculo(ABC):
    def __init__(self, marca, modelo, año, color):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.color = color

    def __str__(self):
        return f"Vehículo genérico: {self.marca} {self.modelo} ({self.año}) - Color: {self.color}"


# Subclases que heredan solo los atributos
class Auto(Vehiculo):
    pass


class Moto(Vehiculo):
    pass


class Camion(Vehiculo):
    pass


class Caballo(Vehiculo):
    pass


# Crear objetos de las clases hijas
auto1 = Auto("Toyota", "Corolla", 2022, "Rojo")
moto1 = Moto("Yamaha", "FZ", 2021, "Negra")
camion1 = Camion("Volvo", "FH", 2020, "Blanco")
caballo1 = Caballo("Arabe", "Completo", 2016, "Blanco")

# Otras estancias
auto2 = Auto("Mustang", "Boss 429", 1969, "Negro")
moto2 = Moto("Honda", "CB750", 1992, "Negra")
camion2 = Camion("Ford", "E-350", 1982, "Blanco")
caballo2 = Caballo("Sangre caliente Holandes", "Completo", 1899, "Dorado")


# Visualización
print(auto1)
print(moto1)
print(camion1)
print(caballo1)

print(auto2)
print(moto2)
print(camion2)
print(caballo2)