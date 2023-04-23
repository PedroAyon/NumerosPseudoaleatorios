import math
from scipy.stats import norm
from pruebas_estadisticas import Status


def medias(numbers: [int], acceptance_level: float = 0.95) -> Status:
    n = len(numbers)
    mean = sum(numbers) / n
    alpha = 1 - acceptance_level
    z_score = norm.ppf(acceptance_level + alpha / 2)
    lower_limit = (1 / 2) - z_score * (1 / math.sqrt(12 * n))
    upper_limit = (1 / 2) + z_score * (1 / math.sqrt(12 * n))
    return Status.APPROVED if lower_limit < mean < upper_limit else Status.FAILED
