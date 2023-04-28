from generadores import *
from pruebas_estadisticas import aplicar_pruebas_estadisticas, Status
from utils import read_json_file, write_json_file

data_folder_file_path = 'C:/Users/pedro/Dev/Simulacion/NumerosPseudoaleatorios/data'


def menu():
    print("\n\nGENERACION DE NUMEROS PSEUDOALEATORIOS \n")
    while True:
        print("\nSeleccionar método de generación:")
        print("1. Algoritmo Aditivo")
        print("2. Algoritmo Lineal")
        print("3. Algoritmo Multiplicativo")
        print("4. Algoritmo de Cuadrados Medios")
        print("5. Algoritmo de Multiplicador Constante")
        print("6. Algoritmo de Productos Medios")
        print("Escriba cualquier otra cosa para salir.")
        opcion = input("Opción -> ")
        print()
        if opcion == "1":
            data = aditivo()
        elif opcion == "2":
            data = lineal()
        elif opcion == "3":
            data = multiplicativo()
        elif opcion == "4":
            data = cuadrados_medios()
        elif opcion == "5":
            data = multiplicador_constante()
        elif opcion == "6":
            data = productos_medios()
        else:
            print("Saliendo del programa...")
            break
        print('Realizando pruebas estadísticas...')
        numbers = [float(x) for x in data['numeros']]
        result = aplicar_pruebas_estadisticas(numbers)
        if result == Status.APPROVED:
            store_data(data)


def store_data(data):
    test_passed_list_count = read_json_file(f'{data_folder_file_path}/test_passed_list_count.json')['count'] + 1
    filepath = f'{data_folder_file_path}/{test_passed_list_count}.json'
    write_json_file(filepath, data)
    write_json_file(f'{data_folder_file_path}/test_passed_list_count.json', {'count': test_passed_list_count})
    print(f'Lista de números pseudoaleatorios almacenada en: {filepath}')


if __name__ == "__main__":
    menu()
