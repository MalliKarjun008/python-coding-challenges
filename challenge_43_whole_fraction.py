def separate_whole_fraction(value):
    whole = int(value)
    fraction = value - whole
    return whole, fraction


def main():
    value = float(input("Enter a number: "))
    whole, fraction = separate_whole_fraction(value)
    print("Whole Part:", whole)
    print("Fraction Part:", fraction)


def test_cases():
    w, f = separate_whole_fraction(12.75)
    assert w == 12 and round(f, 2) == 0.75

    w, f = separate_whole_fraction(5.0)
    assert w == 5 and f == 0.0

    w, f = separate_whole_fraction(0.25)
    assert w == 0 and round(f, 2) == 0.25

    print("All test cases passed!")


if __name__ == "__main__":
    main()
    test_cases()
