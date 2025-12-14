def apply_tax(amount):
    if not isinstance(amount, (int, float)) or amount < 0:
        raise ValueError("Invalid amount")

    if amount < 5000:
        tax = amount * 0.05
    elif amount <= 20000:
        tax = amount * 0.10
    else:
        tax = amount * 0.15

    return tax, amount + tax


def main():
    while True:
        try:
            amount = float(input("Enter amount after discounts: "))
            if amount < 0:
                raise ValueError
            break
        except ValueError:
            print("Invalid amount. Please enter a non-negative number.")

    tax, total = apply_tax(amount)
    print("Tax Amount:", tax)
    print("Total Amount with Tax:", total)


def test_cases():
    tax, total = apply_tax(4000)
    assert tax == 200
    assert total == 4200

    tax, total = apply_tax(5000)
    assert tax == 500
    assert total == 5500

    tax, total = apply_tax(10000)
    assert tax == 1000
    assert total == 11000

    tax, total = apply_tax(25000)
    assert tax == 3750
    assert total == 28750

    tax, total = apply_tax(0)
    assert tax == 0
    assert total == 0

    try:
        apply_tax(-100)
        assert False
    except ValueError:
        pass

    try:
        apply_tax("5000")
        assert False
    except ValueError:
        pass

    print("All test cases passed!")


if __name__ == "__main__":
    test_cases()
    main()
