
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
