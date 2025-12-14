def is_leap_year(year):
    if not isinstance(year, int) or year <= 0:
        raise ValueError("Year must be a positive integer")

    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    return year % 4 == 0


def main():
    try:
        year = int(input("Enter year: "))
    except ValueError:
        print("Invalid input. Please enter a valid year.")
        return

    try:
        if is_leap_year(year):
            print("Leap Year")
        else:
            print("Not a Leap Year")
    except ValueError as e:
        print(e)


def test_cases():
    assert is_leap_year(2000) is True
    assert is_leap_year(1900) is False
    assert is_leap_year(2024) is True
    assert is_leap_year(2023) is False
    assert is_leap_year(2400) is True

    try:
        is_leap_year(0)
        assert False
    except ValueError:
        pass

    try:
        is_leap_year(-2024)
        assert False
    except ValueError:
        pass

    print("All test cases passed!")


if __name__ == "__main__":
    test_cases()
    main()
