from enum import Enum
from scipy.stats import chi2
from pruebas_estadisticas import Status
from utils import truncate_float


class Category(Enum):
    TD = 'TD'
    P1 = '1P'
    P2 = '2P'
    T = 'T'
    TP = 'TP'
    P = 'P'
    Q = 'Q'


def get_category(n, decimals) -> Category:
    try:
        n = truncate_float(n, decimals)
        n = n[str(n).index('.') + 1:]
    except Exception as e:
        print(n)
        return None
    while len(n) < decimals:
        n += '0'
    frequencies = {}
    cat = Category.TD
    for digit in n:
        if digit not in frequencies:
            frequencies[digit] = 1
            continue
        frequencies[digit] += 1
        if frequencies[digit] == 2 and cat == Category.TD:
            cat = Category.P1
        elif frequencies[digit] == 2 and cat == Category.P1:
            cat = Category.P2
        elif (frequencies[digit] == 2 and cat == Category.T) or (frequencies[digit] == 3 and cat == Category.P2):
            cat = Category.TP
        elif frequencies[digit] == 3 and cat == Category.P1:
            cat = Category.T
        elif frequencies[digit] == 4:
            cat = Category.P
        else:
            cat = Category.Q
    return cat


probabilities_3_decimals = {
    Category.TD: 0.72,
    Category.P1: 0.27,
    Category.T: 0.01
}

probabilities_4_decimals = {
    Category.TD: 0.5040,
    Category.P1: 0.4320,
    Category.P2: 0.0270,
    Category.T: 0.0360,
    Category.P: 0.001
}

probabilities_5_decimals = {
    Category.TD: 0.3024,
    Category.P1: 0.5040,
    Category.P2: 0.1080,
    Category.T: 0.0720,
    Category.TP: 0.009,
    Category.P: 0.0045,
    Category.Q: 0.0001
}

probability_tables = {
    3: probabilities_3_decimals,
    4: probabilities_4_decimals,
    5: probabilities_5_decimals
}

degrees_of_freedom = {
    3: 2,
    4: 4,
    5: 6
}


def poker(numbers: [int], decimals: int, acceptance_level: float = 0.95) -> Status:
    n = len(numbers)
    probabilities = probability_tables[decimals]
    frequencies = {}
    for x in numbers:
        category = get_category(x, decimals)
        if category not in frequencies:
            frequencies[category] = 1
        else:
            frequencies[category] += 1
    test_result = 0
    for category in frequencies:
        observed_freq = frequencies[category]
        expected_freq = probabilities[category] * n
        test_result += (expected_freq - observed_freq) ** 2 / expected_freq
    chi_squared = chi2.ppf(acceptance_level, degrees_of_freedom[decimals])
    return Status.APPROVED if test_result < chi_squared else Status.FAILED
