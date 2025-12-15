def apply_payment_rule(amount, mode):
    if not isinstance(amount, (int, float)) or amount < 0:
        raise ValueError("Invalid amount")
    if mode not in ("cash", "credit"):
        raise ValueError("Invalid payment mode")

    if mode == "credit":
        amount += amount * 0.02
    return amount


def main():
    while True:
        try:
            amount = float(input("Enter final amount before payment mode: "))
            if amount < 0:
                raise ValueError
            break
        except ValueError:
            print("Invalid amount. Please enter a non-negative number.")

    while True:
        mode = input("Enter payment mode (cash/credit): ").strip().lower()
        if mode in ("cash", "credit"):
            break
        print("Invalid payment mode. Enter 'cash' or 'credit'.")

    final_amount = apply_payment_rule(amount, mode)
    print("Final Payable Amount:", final_amount)


def test_cases():
    assert apply_payment_rule(1000, "cash") == 1000
    assert apply_payment_rule(1000, "credit") == 1020
    assert apply_payment_rule(0, "credit") == 0

    try:
        apply_payment_rule(-100, "cash")
        assert False
    except ValueError:
        pass

    try:
        apply_payment_rule(1000, "upi")
        assert False
    except ValueError:
        pass

    try:
        apply_payment_rule("1000", "cash")
        assert False
    except ValueError:
        pass

    print("All test cases passed!")


if __name__ == "__main__":
    test_cases()
    main()
