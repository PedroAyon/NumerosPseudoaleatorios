import math

from scipy.stats import chi2

from pruebas_estadisticas import Status


def chi_cuadrada(numbers: [int], acceptance_level: float = 0.95) -> Status:
    n = len(numbers)
    m = int(math.sqrt(n))
    interval_width = 1 / m
    frequencies = [0] * m
    for x in numbers:
        i = int(x / interval_width)
        if i == m:
            i -= 1
        frequencies[i] += 1
    expected_freq = int(n / m)
    test_result = 0
    for observed_freq in frequencies:
        test_result += (expected_freq - observed_freq) ** 2 / expected_freq
    chi_squared = chi2.ppf(acceptance_level, m - 1)
    return Status.APPROVED if test_result < chi_squared else Status.FAILED
