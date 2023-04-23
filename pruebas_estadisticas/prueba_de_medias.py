import math
from scipy.stats import norm


def prueba_de_medias(numbers: [int], acceptance_level: float) -> bool:
    n = len(numbers)
    mean = sum(numbers) / n
    alpha = 1 - acceptance_level
    z_score = norm.ppf(acceptance_level + alpha / 2)
    lower_limit = (1 / 2) - z_score * (1 / math.sqrt(12 * n))
    upper_limit = (1 / 2) + z_score * (1 / math.sqrt(12 * n))
    print(f'mean: {mean}')
    print(f'z_score: {z_score}')
    print(f'lower_limit: {lower_limit}')
    print(f'upper_limit: {upper_limit}')
    return True if lower_limit < mean < upper_limit else False
