#una lista con 5 imputs: (Nombre, Escuela, Domicilio, Edad, Carrera)

lista_Alu = []
print(" Inscripcion de Alumno ")

Nom = input("Agrega tu nombre: ")
lista_Alu.append(Nom)

Prep = input("Agrega tu preparatoria: ")
lista_Alu.append(Prep)

Dom = input("Agrega el domicilio: ")
lista_Alu.append(Dom)

Edad = input("Agrega tu edad: ")
lista_Alu.append(Edad)

car = input("Agrega tu carrera: ")
lista_Alu.append(car)

print("\n📌 Datos Inscripcion:")
for producto in lista_Alu:
    print(f"- {producto}")
print("\n✅ ¡Inscripcion realizada con éxito!🥷")