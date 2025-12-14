def is_even(n):
    if not isinstance(n, int):
        raise ValueError("Input must be an integer.")
    return n % 2 == 0


def main():
    try:
        n=int(input("enter an number"))
    except ValueError:
        print("Invalid input. Please enter an integer value.")
        return
    if is_even(n):
        print("Even")
    else:
        print("Odd")


def test_cases():
    assert is_even(2) is True
    assert is_even(3) is False
    assert is_even(0) is True
    assert is_even(-4) is True

    try:
        is_even(2.5)
        assert False

    except ValueError:
        pass
    print("All test cases passed!")


if __name__ == "__main__":
    main()
    test_cases()
