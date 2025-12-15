def whole_fraction(n):
    if not isinstance(n, (int, float)):
        raise ValueError("Input must be a number")

    whole_part = int(n)
    fraction_part = round(n - whole_part, 10)

    return whole_part, fraction_part


def main():
    while True:
        try:
            n = float(input("Enter a double value: "))
            whole, fraction = whole_fraction(n)
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    print("Whole Value:", whole)
    print("Fractional Value:", fraction)


def test_cases():
    assert whole_fraction(12.34) == (12, 0.34)
    assert whole_fraction(0.56) == (0, 0.56)
    assert whole_fraction(-7.89) == (-7, -0.89)
    assert whole_fraction(5.0) == (5, 0.0)
    assert whole_fraction(3) == (3, 0.0)

    try:
        whole_fraction("3.14")
        assert False
    except ValueError:
        pass

    print("All test cases passed!")


if __name__ == "__main__":
    test_cases()
    main()
