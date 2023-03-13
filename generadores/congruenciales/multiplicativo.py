from utils import *

filepath = 'C:/Users/pedro/Dev/Simulacion/NumerosPseudoaleatorios/data/multiplicativo.json'


def multiplicativo():
    print('Algoritmo Multiplicativo')
    try:
        seed = valid_integer(input('Semilla X0: '), positive=True)
        k = valid_integer(input('k: '), positive=True)
        g = valid_integer(input('g: '), positive=True)
        m = pow(2, g)
        a = 5 + 8 * k
        iterations = valid_integer(input('Número de iteraciones: '), positive=True, max_value=1000)
        data = {
            "X0": seed,
            "k": k,
            "g": g,
            "iteraciones": iterations,
            "numeros": generate_numbers(seed, a, m, iterations)
        }
        write_json_file(filepath, data)
    except Exception as e:
        print(f"Error: {e}")


def generate_numbers(seed, a, m, iterations):
    numbers = []
    for i in range(iterations):
        seed = (a * seed) % m
        numbers.append(round(seed / (m - 1), 4))
    return numbers
