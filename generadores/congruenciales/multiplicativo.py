from utils import *


def multiplicativo():
    try:
        seed = valid_integer(input('Semilla X0: '), positive=True)
        k = valid_integer(input('k: '), positive=True)
        g = valid_integer(input('g: '), positive=True)
        m = pow(2, g)
        a = 5 + 8 * k
        iterations = valid_integer(input('Número de iteraciones: '), positive=True, max_value=1000)
        data = {
            "metodo": 'multiplicativo',
            "X0": seed,
            "k": k,
            "g": g,
            "iteraciones": iterations,
            "numeros": generate_numbers(seed, a, m, iterations)
        }
        return data
    except Exception as e:
        print(f"Error: {e}")


def generate_numbers(seed, a, m, iterations):
    numbers = []
    for i in range(iterations):
        seed = (a * seed) % m
        if seed / (m - 1) > 1:
            print(seed, a, m, seed / (m - 1))
        numbers.append(truncate_float(seed / (m - 1), 5))
    return numbers
