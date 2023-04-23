from utils import *


def aditivo():
    try:
        n = valid_integer(input('Numero de semillas (n): '), positive=True)
        # Entrada de n semillas identificadas por Xi
        seeds = []
        for i in range(n):
            seed = input(f'X{i + 1}: ')
            seeds.append(valid_integer(seed, positive=True))
        m = valid_integer(input('m: '), positive=True)
        iterations = valid_integer(input('Número de iteraciones: '), positive=True, max_value=1000)
        data = {}
        data['metodo'] = 'aditivo'
        for i in range(n):
            data[f'X{i + 1}'] = seeds[i]
        data['m'] = m
        data['numeros'] = generate_numbers(n, seeds, m, iterations)
        return data
    except Exception as e:
        print(f"Error: {e}")


def generate_numbers(n, seeds: [int], m, iterations):
    numbers = []
    for i in range(iterations):
        xi = (seeds[n - 1] + seeds[0]) % m
        seeds.pop(0)
        seeds.append(xi)
        numbers.append(truncate_float(xi / (m - 1), 4))
    return numbers
