from generadores import *


def main():
    print("\n\nGENERACION DE NUMEROS ALEATORIOS \n")
    while True:
        print("\nSeleccione la función que desea ejecutar:")
        print("1. Algoritmo Aditivo")
        print("2. Algoritmo Lineal")
        print("3. Algoritmo Multiplicativo")
        print("4. Algoritmo de Cuadrados Medios")
        print("5. Algoritmo de Multiplicador Constante")
        print("6. Algoritmo de Productos Medios")
        print("Escriba cualquier otra cosa para salir.")

        opcion = input("Opción seleccionada: ")
        print()

        if opcion == "1":
            aditivo()
        elif opcion == "2":
            lineal()
        elif opcion == "3":
            multiplicativo()
        elif opcion == "4":
            cuadrados_medios()
        elif opcion == "5":
            multiplicador_constante()
        elif opcion == "6":
            productos_medios()
        else:
            print("Saliendo del programa...")
            break


if __name__ == "__main__":
    main()
