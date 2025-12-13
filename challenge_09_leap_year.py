def is_leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    return year % 4 == 0


def main():
    year = int(input("Enter year: "))
    if is_leap_year(year):
        print("Leap Year")
    else:
        print("Not a Leap Year")


def test_cases():
    assert is_leap_year(2000) is True
    assert is_leap_year(1900) is False
    assert is_leap_year(2024) is True
    assert is_leap_year(2023) is False
    print("All test cases passed!")


if __name__ == "__main__":
    main()
    test_cases()
