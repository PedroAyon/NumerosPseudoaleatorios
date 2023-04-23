import random

from generadores import *
from pruebas_estadisticas import aplicar_pruebas_estadisticas, Status
from utils.json_utils import *

data_folder_file_path = 'C:/Users/pedro/Dev/Simulacion/NumerosPseudoaleatorios/data'


def main():
    for i in range(500):
        data = multiplicativo(int(random.uniform(1000, 200000)), int(random.uniform(1, 300)),
                              int(random.uniform(2, 20)), 200)
        numbers = [float(x) for x in data['numeros']]
        status = aplicar_pruebas_estadisticas(numbers)
        print(status.value)
        if status == Status.APPROVED:
            print()
            test_passed_list_count = read_json_file(f'{data_folder_file_path}/test_passed_list_count.json')['count'] + 1
            filepath = f'{data_folder_file_path}/{test_passed_list_count}.json'
            write_json_file(filepath, data)
            write_json_file(f'{data_folder_file_path}/test_passed_list_count.json', {'count': test_passed_list_count})


def menu():
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
