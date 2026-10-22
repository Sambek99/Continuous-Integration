
"""Mandatory membership quotation tests for R9."""

import pytest

from gym_calculator import calculate_subtotal, is_valid_selection
from gym_discounts import (
    apply_group_discount,
    apply_special_offer,
    apply_premium_surcharge,
    round_half_up,
)


def calculate_quote(plan, extras, members):
    """Combine the existing calculation modules for testing."""
    if not is_valid_selection(plan, extras, members):
        return -1

    subtotal = calculate_subtotal(plan, extras, members)
    after_group = apply_group_discount(subtotal, members)
    after_offer = apply_special_offer(after_group)

    has_premium_extra = any(
        extra in ("SPA", "SPECIALIZED_PROGRAM")
        for extra in extras
    )

    after_surcharge = apply_premium_surcharge(
        after_offer, has_premium_extra
    )

    return round_half_up(after_surcharge)


@pytest.mark.parametrize(
    "plan,extras,members,expected",
    [
        ("BASIC", [], 1, 30),
        ("STANDARD", ["PERSONAL_TRAINING"], 1, 70),
        ("BASIC", ["GROUP_CLASSES"], 2, 81),
        ("BASIC", ["GROUP_CLASSES"], 3, 122),
        ("STANDARD", ["GROUP_CLASSES", "PERSONAL_TRAINING"], 4, 286),
        ("PREMIUM", ["GROUP_CLASSES", "SPA"], 2, 215),
        ("PREMIUM", ["SPA", "SPECIALIZED_PROGRAM"], 3, 412),
        ("PREMIUM", ["SPA", "SPECIALIZED_PROGRAM", "PERSONAL_TRAINING"], 4, 626),
        ("BASIC", ["SPA"], 1, -1),
        ("GOLD", [], 1, -1),
        ("BASIC", [], 0, -1),
    ],
)
def test_mandatory_membership_cases(plan, extras, members, expected):
    """Verify the eleven mandatory quotation scenarios."""
    assert calculate_quote(plan, extras, members) == expected
