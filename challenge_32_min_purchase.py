def check_minimum_purchase(amount):
    return amount >= 500


def main():
    amount = float(input("Enter final amount after all charges: "))

    if check_minimum_purchase(amount):
        print("Invoice can be generated")
    else:
        print("Minimum purchase amount not met")


def test_cases():
    assert check_minimum_purchase(500) is True
    assert check_minimum_purchase(499.99) is False
    assert check_minimum_purchase(1000) is True
    assert check_minimum_purchase(0) is False
    print("All test cases passed!")


if __name__ == "__main__":
    main()
    test_cases()
