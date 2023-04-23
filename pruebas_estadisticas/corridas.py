import math
from scipy.stats import norm
from pruebas_estadisticas import Status


def corridas(numbers: [int], acceptance_level: float = 0.95):
    return Status.APPROVED if arriba_y_abajo(numbers, acceptance_level) == Status.APPROVED \
                              and arriba_y_abajo_de_la_media(numbers, acceptance_level) == Status.APPROVED else Status.FAILED


def arriba_y_abajo(numbers: [int], acceptance_level: float) -> Status:
    n = len(numbers)
    s = []
    for i in range(1, n):
        s.append(0 if numbers[i] < numbers[i - 1] else 1)
    c0 = count_subgroups(s)
    expected_value = (2 * n - 1) / 3
    squared_variance = (16 * n - 29) / 90
    z0 = abs((c0 - expected_value) / math.sqrt(squared_variance))
    alpha = 1 - acceptance_level
    z_score = norm.ppf(acceptance_level + alpha / 2)
    return Status.APPROVED if z0 < z_score else Status.FAILED


def arriba_y_abajo_de_la_media(numbers: [int], acceptance_level: float) -> Status:
    n = len(numbers)
    s = []
    n0 = n1 = 0
    for i in range(n):
        if numbers[i] < 0.5:
            n0 += 1
            s.append(0)
        else:
            n1 += 1
            s.append(1)
    c0 = count_subgroups(s)
    expected_value = (2 * n0 * n1) / n + 0.5
    squared_variance = (2 * n0 * n1 * (2 * n0 * n1 - n)) / (n ** 2 * (n - 1))
    if squared_variance == 0:
        z0 = 0
    else:
        z0 = (c0 - expected_value) / math.sqrt(squared_variance)
    alpha = 1 - acceptance_level
    z_score = norm.ppf(acceptance_level + alpha / 2)
    return Status.APPROVED if -z_score < z0 < z_score else Status.FAILED


def count_subgroups(numbers: [int]):
    c = 0
    flag = None
    for n in numbers:
        if n != flag:
            c += 1
            flag = n
    return c
