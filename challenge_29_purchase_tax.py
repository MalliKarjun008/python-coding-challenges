def apply_tax(amount):
    if amount < 5000:
        tax = amount * 0.05
    elif amount <= 20000:
        tax = amount * 0.10
    else:
        tax = amount * 0.15
    return tax, amount + tax


def main():
    amount = float(input("Enter amount after discounts: "))
    tax, total = apply_tax(amount)

    print("Tax Amount:", tax)
    print("Total Amount with Tax:", total)


def test_cases():
    tax, total = apply_tax(4000)
    assert tax == 200
    assert total == 4200

    tax, total = apply_tax(10000)
    assert tax == 1000
    assert total == 11000

    tax, total = apply_tax(25000)
    assert tax == 3750
    assert total == 28750

    print("All test cases passed!")


if __name__ == "__main__":
    main()
    test_cases()
