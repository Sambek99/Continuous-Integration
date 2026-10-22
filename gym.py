from decimal import Decimal, ROUND_HALF_UP

GROUP_DISCOUNT_RATE = Decimal("0.10")
PREMIUM_SURCHARGE_RATE = Decimal("0.15")

class GymMembership:
    """Represent a gym membership calculator."""

    @staticmethod
    def calculate_membership(plan, extras, members):
        """Calculate the initial membership price."""
        prices = {
            "BASIC": 30,
            "STANDARD": 45,
            "PREMIUM": 70,
        }

        if plan not in prices or members < 1:
            return -1

        if extras:
            return -1

        return prices[plan] * members


def calculate_membership(plan, extras, members):
    """Provide access to the membership calculation."""
    return GymMembership.calculate_membership(
        plan, extras, members
    )

def apply_group_discount(amount, members):
    """R4. Con 2 o mas miembros, el subtotal recibe 10% de descuento."""
    amount = Decimal(str(amount))
    if members >= 2:
        return amount * (1 - GROUP_DISCOUNT_RATE)
    return amount
 
 
def apply_special_offer(amount):
    """R5. Sobre el monto despues de R4.
    Si es mayor que 400 se resta 50; si no, si es mayor que 200 se resta 20.
    Nunca se suman ambos descuentos.
    """
    amount = Decimal(str(amount))
    if amount > 400:
        return amount - 50
    if amount > 200:
        return amount - 20
    return amount
 
 
def apply_premium_surcharge(amount, has_premium_extra):
    """R6. Si hay al menos un extra premium, se suma 15% al monto despues de R5."""
    amount = Decimal(str(amount))
    if has_premium_extra:
        return amount * (1 + PREMIUM_SURCHARGE_RATE)
    return amount
 
 
def round_half_up(amount):
    """R7. Redondeo half up a entero (solo al final)."""
    return int(Decimal(str(amount)).quantize(Decimal("1"), rounding=ROUND_HALF_UP))
