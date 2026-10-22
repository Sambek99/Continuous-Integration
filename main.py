
from decimal import Decimal

"""Command-line interface for Gym Membership Quote."""

from gym_calculator import calculate_subtotal, is_valid_selection
from gym_discounts import (
    apply_group_discount,
    apply_special_offer,
    apply_premium_surcharge,
    round_half_up,
)


def main():
    """Ask for membership details and display the quotation."""
    print("===== GYM MEMBERSHIP QUOTE =====")

    plan = input(
        "Select a plan (BASIC/STANDARD/PREMIUM): "
    ).strip().upper()

    extras_input = input(
        "Enter extras (comma-separated, or NONE): "
    ).strip().upper()

    if extras_input in ("", "NONE"):
        extras = []
    else:
        extras = [
            extra.strip()
            for extra in extras_input.split(",")
        ]

    try:
        members = int(input("Number of members: "))
    except ValueError:
        print("Invalid number of members.")
        print("Final result: -1")
        return -1

    if not is_valid_selection(plan, extras, members):
        print("Invalid membership selection.")
        print("Final result: -1")
        return -1

    subtotal = Decimal(str(calculate_subtotal(plan, extras, members)))
    after_group = apply_group_discount(subtotal, members)
    group_discount = subtotal - after_group

    after_offer = apply_special_offer(after_group)
    special_discount = after_group - after_offer

    has_premium_extra = any(
        extra in ("SPA", "SPECIALIZED_PROGRAM")
        for extra in extras
    )

    after_surcharge = apply_premium_surcharge(
        after_offer, has_premium_extra
    )
    premium_surcharge = after_surcharge - after_offer

    total = round_half_up(after_surcharge)

    print("\n===== QUOTATION DETAILS =====")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Group discount: -${group_discount:.2f}")
    print(f"Special offer: -${special_discount:.2f}")
    print(f"Premium surcharge: +${premium_surcharge:.2f}")
    print(f"Total: ${total:.2f}")

    confirmation = input(
        "\nConfirm quotation? (y/n): "
    ).strip().lower()

    if confirmation != "y":
        print("Quotation cancelled.")
        print("Final result: -1")
        return -1

    print(f"Final result: {total}")
    return total


if __name__ == "__main__":
    main()
