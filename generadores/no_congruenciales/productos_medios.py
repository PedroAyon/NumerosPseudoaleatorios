from utils import *

filepath = 'C:/Users/pedro/Dev/Simulacion/NumerosPseudoaleatorios/data/productos_medios.json'


def productos_medios():
    print("Algoritmo de Productos Medios")
    try:
        seed1 = valid_integer(input('Semilla X0: '), positive=True, min_digits=3)
        seed2 = valid_integer(input('Semilla X1: '), positive=True, min_digits=3)
        if len(str(seed1)) != len(str(seed2)):
            raise ValueError('X0 y X1 deben tener la misma longitud')
        iterations = valid_integer(input('Número de iteraciones: '), positive=True, max_value=1000)
        data = {
            "X0": seed1,
            "X1": seed2,
            "iteraciones": iterations,
            "numeros": generate_numbers(seed1, seed2, iterations)
        }
        write_json_file(filepath, data)
    except Exception as e:
        print(f"Error: {e}")


def generate_numbers(seed1: int, seed2: int, iterations: int):
    numbers = []
    digits = len(str(seed1))
    for i in range(iterations):
        xi = get_n_middle_digits(str(seed1 * seed2), digits)
        seed1 = seed2
        seed2 = xi
        numbers.append(truncate_float(xi * pow(10, -digits), digits))
    return numbers
