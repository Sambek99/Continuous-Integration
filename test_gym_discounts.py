import unittest
from decimal import Decimal

from gym_discounts import (
    apply_group_discount,
    apply_special_offer,
    apply_premium_surcharge,
    round_half_up,
)


class TestGroupDiscount(unittest.TestCase):  # R4
    def test_one_member_no_discount(self):
        self.assertEqual(apply_group_discount(30, 1), Decimal("30"))

    def test_two_members_ten_percent(self):
        self.assertEqual(apply_group_discount(90, 2), Decimal("81"))

    def test_three_members_ten_percent(self):
        self.assertEqual(apply_group_discount(135, 3), Decimal("121.5"))


class TestSpecialOffer(unittest.TestCase):  # R5
    def test_above_400_subtracts_50(self):
        self.assertEqual(apply_special_offer(594), Decimal("544"))

    def test_exactly_400_subtracts_20(self):
        self.assertEqual(apply_special_offer(400), Decimal("380"))

    def test_above_200_subtracts_20(self):
        self.assertEqual(apply_special_offer(306), Decimal("286"))

    def test_exactly_200_no_offer(self):
        self.assertEqual(apply_special_offer(200), Decimal("200"))

    def test_never_adds_both(self):
        self.assertEqual(apply_special_offer(500), Decimal("450"))


class TestPremiumSurcharge(unittest.TestCase):  # R6
    def test_with_premium_extra(self):
        self.assertEqual(apply_premium_surcharge(187, True), Decimal("215.05"))

    def test_without_premium_extra(self):
        self.assertEqual(apply_premium_surcharge(187, False), Decimal("187"))


class TestRounding(unittest.TestCase):  # R7 (apoyo)
    def test_half_rounds_up(self):
        self.assertEqual(round_half_up(Decimal("121.5")), 122)


class TestTableCases(unittest.TestCase):
    """Casos de la tabla que ejercitan R4 + R5 + R6."""

    def pipeline(self, subtotal, members, premium):
        a = apply_group_discount(subtotal, members)
        a = apply_special_offer(a)
        a = apply_premium_surcharge(a, premium)
        return round_half_up(a)

    def test_basic_group_3(self):
        self.assertEqual(self.pipeline(135, 3, False), 122)

    def test_standard_4(self):
        self.assertEqual(self.pipeline(340, 4, False), 286)

    def test_premium_group_spa_2(self):
        self.assertEqual(self.pipeline(230, 2, True), 215)

    def test_premium_spa_specialized_3(self):
        self.assertEqual(self.pipeline(420, 3, True), 412)

    def test_premium_four_extras_4(self):
        self.assertEqual(self.pipeline(660, 4, True), 626)


if __name__ == "__main__":
    unittest.main()
