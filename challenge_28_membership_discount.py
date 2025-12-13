def apply_membership_discount(amount, is_member):
    if is_member:
        amount -= amount * 0.02
    return amount


def main():
    amount = float(input("Enter amount after previous discounts: "))
    member = input("Is customer a member (y/n): ").lower()

    final_amount = apply_membership_discount(amount, member == "y")
    print("Final Amount:", final_amount)


def test_cases():
    assert apply_membership_discount(1000, True) == 980
    assert apply_membership_discount(1000, False) == 1000
    assert apply_membership_discount(0, True) == 0
    print("All test cases passed!")


if __name__ == "__main__":
    main()
    test_cases()
