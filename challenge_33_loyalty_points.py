def calculate_loyalty_points(amount):
    return int(amount // 100)


def main():
    amount = float(input("Enter final amount paid: "))
    points = calculate_loyalty_points(amount)
    print("Loyalty Points Earned:", points)


def test_cases():
    assert calculate_loyalty_points(100) == 1
    assert calculate_loyalty_points(999) == 9
    assert calculate_loyalty_points(0) == 0
    assert calculate_loyalty_points(1050) == 10
    print("All test cases passed!")


if __name__ == "__main__":
    main()
    test_cases()
