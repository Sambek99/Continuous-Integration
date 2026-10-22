"""Modulo para la cotizacion de membresias de gimnasio.

Proporciona catalogos, validaciones, calculo de subtotal y redondeo half up.
"""

from decimal import Decimal, ROUND_HALF_UP

# R1. Catalogo de planes
PLANS = {
    "BASIC": 30.0,
    "STANDARD": 45.0,
    "PREMIUM": 70.0,
}

# R2. Catalogo de extras y definicion de extras premium
EXTRAS = {
    "GROUP_CLASSES": {"price": 15.0, "is_premium": False},
    "PERSONAL_TRAINING": {"price": 25.0, "is_premium": False},
    "SPA": {"price": 30.0, "is_premium": True},
    "SPECIALIZED_PROGRAM": {"price": 40.0, "is_premium": True},
}


def is_valid_selection(plan, extras, members):
    """Valida plan, extras y miembros segun R1, R2 y R3."""
    if members < 1:
        return False

    if plan not in PLANS:
        return False

    for extra in extras:
        if extra not in EXTRAS:
            return False
        if EXTRAS[extra]["is_premium"] and plan != "PREMIUM":
            return False

    return True


def calculate_subtotal(plan, extras, members):
    """Calcula el subtotal base. Si es invalido, retorna -1.0."""
    if not is_valid_selection(plan, extras, members):
        return -1.0

    plan_price = PLANS[plan]
    extras_total = sum(EXTRAS[extra]["price"] for extra in extras)
    return (plan_price + extras_total) * members


def round_half_up(amount):
    """Aplica redondeo half up a un entero segun el requisito R7."""
    if amount < 0:
        return -1
    decimal_val = Decimal(str(amount))
    rounded = decimal_val.quantize(Decimal("1"), rounding=ROUND_HALF_UP)
    return int(rounded)