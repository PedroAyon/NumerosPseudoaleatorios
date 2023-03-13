from utils import *

filepath = 'C:/Users/pedro/Dev/Simulacion/NumerosPseudoaleatorios/data/cuadrados_medios.json'


def cuadrados_medios():
    print("Algoritmo de Cuadrados Medios")
    try:
        seed = valid_integer(input('Semilla X0: '), positive=True, min_digits=3)
        iterations = valid_integer(input('Número de iteraciones: '), positive=True, max_value=1000)
        data = {
            "X0": seed,
            "iteraciones": iterations,
            "numeros": generate_numbers(seed, iterations)
        }
        write_json_file(filepath, data)
    except Exception as e:
        print(f"Error: {e}")


def generate_numbers(seed, iterations):
    numbers = []
    digits = len(str(seed))
    for i in range(iterations):
        seed = get_n_middle_digits(str(seed ** 2), digits)
        numbers.append(round(seed * pow(10, -digits), digits))
    return numbers
