def is_even(n):
    return n % 2 == 0


def main():
    n = int(input("Enter a number: "))
    if is_even(n):
        print("Even")
    else:
        print("Odd")


def test_cases():
    assert is_even(2) is True
    assert is_even(3) is False
    assert is_even(0) is True
    assert is_even(-4) is True
    print("All test cases passed!")


if __name__ == "__main__":
    main()
    test_cases()
