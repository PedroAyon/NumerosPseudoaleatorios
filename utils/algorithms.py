def get_n_middle_digits(number: str, digits: int) -> int:
    while len(number) < digits:
        number = '0' + number
    start_index = (len(number) - digits) // 2
    center_num = int(number[start_index: start_index + digits])
    return center_num


def coprime_numbers(x, y):
    x_factors = set(prime_factors(x))
    y_factors = set(prime_factors(y))
    for n in x_factors:
        if n in y_factors:
            return False
    return True


def prime_factors(n):
    primes = primes_less_than(int(n ** 0.5) + 1)
    factors = []
    for p in primes:
        while n % p == 0:
            factors.append(p)
            n //= p
        if n == 1:
            break
    if n > 1:
        factors.append(n)
    return factors


def primes_less_than(n):
    is_prime = [True] * n
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i ** 2, n, i):
                is_prime[j] = False
    primes = []
    for i in range(2, n):
        if is_prime[i]:
            primes.append(i)
    return primes


# Recortar sin redondear
def truncate_float(n, places):
    return int(n * 10 ** places) / 10 ** places
