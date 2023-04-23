from utils import *


def cuadrados_medios():
    try:
        seed = valid_integer(input('Semilla X0: '), positive=True, min_digits=3)
        iterations = valid_integer(input('Número de iteraciones: '), positive=True, max_value=1000)
        data = {
            "metodo": 'cuadrados_medios',
            "X0": seed,
            "iteraciones": iterations,
            "numeros": generate_numbers(seed, iterations)
        }
        return data
    except Exception as e:
        print(f"Error: {e}")


def generate_numbers(seed, iterations):
    numbers = []
    digits = len(str(seed))
    for i in range(iterations):
        seed = get_n_middle_digits(str(seed ** 2), digits)
        numbers.append(truncate_float(seed * pow(10, -digits), digits))
    return numbers
