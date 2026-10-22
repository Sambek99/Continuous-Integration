
"""Command-line interface for Gym Membership Quote."""

from gym import calculate_membership


def main():
    """Ask for membership details and display the quote."""
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

    total = calculate_membership(plan, extras, members)

    if total == -1:
        print("Invalid membership selection.")
        print("Final result: -1")
        return -1

    print(f"Total: {total}")

    confirmation = input(
        "Confirm quotation? (y/n): "
    ).strip().lower()

    if confirmation != "y":
        print("Final result: -1")
        return -1

    print(f"Final result: {total}")
    return total


if __name__ == "__main__":
    main()
