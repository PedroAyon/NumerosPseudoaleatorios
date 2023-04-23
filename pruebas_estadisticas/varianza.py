from scipy.stats import chi2

from pruebas_estadisticas import Status


def varianza(numbers: [int], acceptance_level) -> Status:
    n = len(numbers)
    mean = sum(numbers) / n
    alpha = 1 - acceptance_level
    variance = sum([(ri - mean) ** 2 for ri in numbers]) / (n - 1)
    upper_limit = (chi2.ppf(acceptance_level / 2, n - 1)) / (12 * (n - 1))
    lower_limit = (chi2.ppf(alpha / 2, n - 1)) / (12 * (n - 1))
    return Status.APPROVED if lower_limit < variance < upper_limit else Status.FAILED
