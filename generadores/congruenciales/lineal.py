from utils import *


def lineal():
    try:
        seed = valid_integer(input('Semilla X0: '), positive=True)
        k = valid_integer(input('k: '), positive=True)
        c = valid_integer(input('c: '), positive=True)
        g = valid_integer(input('g: '), positive=True)
        m = pow(2, g)
        if not coprime_numbers(c, m):
            raise ValueError('c y m deben ser relativamente primos')
        a = 1 + 4 * k
        iterations = valid_integer(input('Número de iteraciones: '), positive=True, max_value=1000)
        data = {
            "metodo": 'lineal',
            "X0": seed,
            "k": k,
            "c": c,
            "g": g,
            "iteraciones": iterations,
            "numeros": generate_numbers(seed, a, c, m, iterations)
        }
        return data
    except Exception as e:
        print(f"Error: {e}")


def generate_numbers(seed, a, c, m, iterations):
    numbers = []
    for i in range(iterations):
        seed = (a * seed + c) % m
        numbers.append(truncate_float(seed / (m - 1), 4))
    return numbers
