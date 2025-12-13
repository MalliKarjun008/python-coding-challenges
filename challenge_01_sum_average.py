
def calculate_sum_and_average(a, b):
    total = a + b
    average = total / 2
    return total, average


def main():
    # User input
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    total, avg = calculate_sum_and_average(a, b)

    print("Sum:", total)
    print("Average:", avg)


# ---------------- TEST CASES ----------------
def test_cases():
    # Positive cases
    assert calculate_sum_and_average(10, 20) == (30, 15)
    assert calculate_sum_and_average(5, 5) == (10, 5)

    # Negative cases
    assert calculate_sum_and_average(-10, -20) == (-30, -15)

    # Edge cases
    assert calculate_sum_and_average(0, 0) == (0, 0)

    print("All test cases passed!")


if __name__ == "__main__":
    main()
    test_cases()
