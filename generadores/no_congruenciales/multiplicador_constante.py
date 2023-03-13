from utils import *

filepath = 'C:/Users/pedro/Dev/Simulacion/NumerosPseudoaleatorios/data/multiplicador_constante.json'


def multiplicador_constante():
    print("Algoritmo de Multiplicador Constante")
    try:
        seed = valid_integer(input('Semilla X0: '), positive=True, min_digits=3)
        a = valid_integer(input('Constante a: '), positive=True, min_digits=3)
        if len(str(seed)) != len(str(a)):
            raise ValueError("X0 y a deben tener la misma longitud.")
        iterations = valid_integer(input('Número de iteraciones: '), positive=True, max_value=1000)
        data = {
            "X0": seed,
            "a": seed,
            "iteraciones": iterations,
            "numeros": generate_numbers(seed, a, iterations)
        }
        write_json_file(filepath, data)
    except Exception as e:
        print(f"Error: {e}")


def generate_numbers(seed: int, a: int, iterations: int):
    numbers = []
    digits = len(str(seed))
    for i in range(iterations):
        seed = get_n_middle_digits(str(seed * a), digits)
        numbers.append(round(seed * pow(10, -digits), digits))
    return numbers
