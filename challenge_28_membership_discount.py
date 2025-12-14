def apply_membership_discount(amount, is_member):
    if not isinstance(amount, (int, float)) or amount < 0:
        raise ValueError("Invalid amount")
    if not isinstance(is_member, bool):
        raise ValueError("Invalid membership flag")

    if is_member:
        amount -= amount * 0.02
    return amount


def main():
    while True:
        try:
            amount = float(input("Enter amount after previous discounts: "))
            if amount < 0:
                raise ValueError
            break
        except ValueError:
            print("Invalid amount. Please enter a non-negative number.")

    while True:
        member_input = input("Is customer a member (y/n): ").strip().lower()
        if member_input in ("y", "n"):
            is_member = member_input == "y"
            break
        print("Invalid input. Enter 'y' or 'n'.")

    final_amount = apply_membership_discount(amount, is_member)
    print("Final Amount:", final_amount)


def test_cases():
    assert apply_membership_discount(1000, True) == 980
    assert apply_membership_discount(1000, False) == 1000
    assert apply_membership_discount(0, True) == 0

    try:
        apply_membership_discount(-100, True)
        assert False
    except ValueError:
        pass

    try:
        apply_membership_discount(1000, "y")
        assert False
    except ValueError:
        pass

    print("All test cases passed!")


if __name__ == "__main__":
    test_cases()
    main()
