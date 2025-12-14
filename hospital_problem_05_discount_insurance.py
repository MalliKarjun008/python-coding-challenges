def apply_discount(total_amount, has_insurance):
    if has_insurance:
        discount = total_amount * 0.20
    else:
        discount = 0
    return total_amount - discount


def main():
    total_amount = int(input("Enter total bill amount: "))
    insurance = input("Do you have insurance? (yes/no): ").lower()

    has_insurance = insurance == "yes"
    final_amount = apply_discount(total_amount, has_insurance)

    print("Final Amount Payable:", final_amount)


def test_cases():
    assert apply_discount(1000, True) == 800
    assert apply_discount(1000, False) == 1000
    assert apply_discount(0, True) == 0
    print("All test cases passed!")


if __name__ == "__main__":
    main()
    test_cases()
