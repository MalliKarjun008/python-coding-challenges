def check_minimum_purchase(amount):
    if not isinstance(amount, (int, float)) or amount < 0:
        raise ValueError("Invalid amount")
    return amount >= 500


def main():
    while True:
        try:
            amount = float(input("Enter final amount after all charges: "))
            if amount < 0:
                raise ValueError
            break
        except ValueError:
            print("Invalid amount. Please enter a non-negative number.")

    if check_minimum_purchase(amount):
        print("Invoice can be generated")
    else:
        print("Minimum purchase amount not met")


def test_cases():
    assert check_minimum_purchase(500) is True
    assert check_minimum_purchase(499.99) is False
    assert check_minimum_purchase(1000) is True
    assert check_minimum_purchase(0) is False

    try:
        check_minimum_purchase(-100)
        assert False
    except ValueError:
        pass

    try:
        check_minimum_purchase("500")
        assert False
    except ValueError:
        pass

    print("All test cases passed!")


if __name__ == "__main__":
    test_cases()
    main()
