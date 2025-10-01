#Esta funcion sirve para crear un Menú con el cual tendremos acceso a las demas funciones
def mostrar_menu() -> None:
    print("\n===== MENÚ PRINCIPAL =====")
    print("1) Saludar")
    print("2) Calcular la suma de dos números")
    print("3) Mostrar la tabla de multiplicar del 5")
    print("0) Salir")
    
#En esta vas a introducir tu nombre y la funcion lo va a imprimir junto con un saludo
def opcion_saludar() -> None:
    nombre = input("¿Cómo te llamas? ").strip()
    print(f"¡Hola, {nombre}! Bienvenido/a.")

#Esta funcion te pide dos numeros para luego sumarlos e imprimir el resultado
def opcion_suma() -> None:
    try:
        a = float(input("Primer número: "))
        b = float(input("Segundo número: "))
        print(f"La suma es: {a + b}")
    except ValueError:
        print(" Debes introducir valores numéricos.")

#En esta funcion solo se va a imprimir la tabla del numero 5
def opcion_tabla() -> None:
    numero = 5
    print(f"\nTabla del {numero}:")
    for i in range(1, 11):
        print(f"{numero} × {i} = {numero * i}")

#La variable continuar sirve para poder iniciar el bucle while, Minetras la variable Continuar este en True se va a ejecutar indefinidamente el bucle, hasta que se ponga en False
# ---------- Bucle principal ----------
Continuar = True              
while Continuar:
    mostrar_menu()             
    eleccion = input("Elige una opción: ").strip()

    if eleccion == "1":
        opcion_saludar()
    elif eleccion == "2":
        opcion_suma()
    elif eleccion == "3":
        opcion_tabla()
    elif eleccion == "0":
        print("\n ¡Hasta luego!")
        Continuar = False
    else:
        print(" Opción no válida, intenta de nuevo.")

print("Programa terminado.")