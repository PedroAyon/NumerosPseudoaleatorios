from .status import Status
from .medias import medias
from .varianza import varianza
from .chi_cuadrada import chi_cuadrada
from .poker import poker
from .corridas import arriba_y_abajo, arriba_y_abajo_de_la_media


def aplicar_pruebas_estadisticas(numbers: [int], acceptance_level=0.95, decimals_for_poker_test=5) -> Status:
    statuses = {
        'Prueba de medias': medias(numbers, acceptance_level).value,
        'Prueba de varianza': varianza(numbers, acceptance_level).value,
        'Prueba de chi cuadrada': chi_cuadrada(numbers, acceptance_level).value,
        'Prueba de póker': poker(numbers, decimals_for_poker_test, acceptance_level).value,
        'Prueba de corridas arriba y abajo': arriba_y_abajo(numbers, acceptance_level).value,
        'Prueba de corridas arriba y abajo de la media': arriba_y_abajo_de_la_media(numbers, acceptance_level).value
    }
    final_status = Status.APPROVED
    for test in statuses:
        print(f'{test}: {statuses[test]}')
        if statuses[test] == Status.FAILED.value:
            final_status = Status.FAILED
    return final_status

