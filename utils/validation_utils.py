def valid_integer(number: str, positive=False, min_digits=None, max_value=2147483647):
    if not (number.startswith('-') and number[1:].isdigit()) and not number.isdigit():
        raise ValueError("El valor ingresado no es un número")
    number = int(number)
    if abs(number) > max_value:
        raise ValueError(f"El número excede el límite de {max_value}")
    if positive and number < 0:
        raise ValueError("El número debe ser positivo")
    if min_digits is not None and len(str(number)) < min_digits:
        raise ValueError(f"El número debe tener al menos {min_digits} dígitos")
    return number
