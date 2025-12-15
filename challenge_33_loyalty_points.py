def calculate_loyalty_points(amount):
    if not isinstance(amount, (int, float)) or amount < 0:
        raise ValueError("Invalid amount")
    return int(amount // 100)


def main():
    while True:
        try:
            amount = float(input("Enter final amount paid: "))
            if amount < 0:
                raise ValueError
            break
        except ValueError:
            print("Invalid amount. Please enter a non-negative number.")

    points = calculate_loyalty_points(amount)
    print("Loyalty Points Earned:", points)


def test_cases():
    assert calculate_loyalty_points(100) == 1
    assert calculate_loyalty_points(999) == 9
    assert calculate_loyalty_points(0) == 0
    assert calculate_loyalty_points(1050) == 10

    try:
        calculate_loyalty_points(-100)
        assert False
    except ValueError:
        pass

    try:
        calculate_loyalty_points("1000")
        assert False
    except ValueError:
        pass

    print("All test cases passed!")


if __name__ == "__main__":
    test_cases()
    main()
