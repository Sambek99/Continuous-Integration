"""Pruebas unitarias para los requisitos R1, R2, R3 y R7 de Developer A."""

import pytest
from gym_calculator import (
    is_valid_selection,
    calculate_subtotal,
    round_half_up,
)


def test_r1_valid_plans():
    """Valida que los planes catalogados sean reconocidos exitosamente."""
    assert is_valid_selection("BASIC", [], 1) is True
    assert is_valid_selection("STANDARD", [], 1) is True
    assert is_valid_selection("PREMIUM", [], 1) is True


def test_r1_invalid_plan():
    """R1: Un plan que no esta en la tabla debe ser invalido."""
    assert is_valid_selection("GOLD", [], 1) is False
    assert calculate_subtotal("VIP", [], 1) == -1.0


def test_r2_unknown_extra():
    """R2: Un extra desconocido debe invalidar la cotizacion."""
    assert is_valid_selection("BASIC", ["SAUNA"], 1) is False
    assert calculate_subtotal("BASIC", ["SAUNA"], 1) == -1.0


def test_r2_premium_extra_on_non_premium_plan():
    """R2: Extras premium solo se permiten con plan PREMIUM."""
    assert is_valid_selection("BASIC", ["SPA"], 1) is False
    assert is_valid_selection("STANDARD", ["SPECIALIZED_PROGRAM"], 1) is False
    assert calculate_subtotal("BASIC", ["SPA"], 1) == -1.0


def test_r2_premium_extra_on_premium_plan_allowed():
    """R2: Extras premium deben ser validos con el plan PREMIUM."""
    assert is_valid_selection("PREMIUM", ["SPA"], 1) is True
    assert (
        is_valid_selection(
            "PREMIUM", ["SPA", "SPECIALIZED_PROGRAM"], 2
        )
        is True
    )


def test_r3_invalid_members_count():
    """R3: El numero de miembros debe ser al menos 1."""
    assert is_valid_selection("BASIC", [], 0) is False
    assert is_valid_selection("BASIC", [], -3) is False
    assert calculate_subtotal("BASIC", [], 0) == -1.0


def test_r3_subtotal_calculation():
    """R3: Comprueba el calculo exacto del subtotal."""
    # BASIC (30) + GROUP_CLASSES (15) = 45 por miembro * 2 miembros = 90
    assert calculate_subtotal("BASIC", ["GROUP_CLASSES"], 2) == 90.0
    # PREMIUM (70) + SPA (30) + PERSONAL_TRAINING (25) = 125 * 1 = 125
    assert (
        calculate_subtotal(
            "PREMIUM", ["SPA", "PERSONAL_TRAINING"], 1
        )
        == 125.0
    )


@pytest.mark.parametrize(
    "input_val, expected",
    [
        (80.4, 80),
        (80.5, 81),
        (80.6, 81),
        (121.5, 122),
        (285.5, 286),
        (-1.0, -1),
    ],
)
def test_r7_round_half_up(input_val, expected):
    """R7: Redondeo half up al entero mas cercano y retorno de -1 en error."""
    assert round_half_up(input_val) == expected