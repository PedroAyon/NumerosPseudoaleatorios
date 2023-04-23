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


if __name__ == "__main__":
    main()
