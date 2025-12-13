def apply_payment_rule(amount, mode):
    if mode == "credit":
        amount += amount * 0.02
    return amount


def main():
    amount = float(input("Enter final amount before payment mode: "))
    mode = input("Enter payment mode (cash/credit): ").lower()

    final_amount = apply_payment_rule(amount, mode)
    print("Final Payable Amount:", final_amount)


def test_cases():
    assert apply_payment_rule(1000, "cash") == 1000
    assert apply_payment_rule(1000, "credit") == 1020
    assert apply_payment_rule(0, "credit") == 0
    print("All test cases passed!")


if __name__ == "__main__":
    main()
    test_cases()
