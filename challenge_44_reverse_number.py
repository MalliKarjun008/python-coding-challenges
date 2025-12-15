def reverse_number(n):
    if not isinstance(n, int):
        raise ValueError("Input must be an integer")

    sign = -1 if n < 0 else 1
    reversed_num = int(str(abs(n))[::-1])

    return sign * reversed_num


def main():
    while True:
        try:
            n = int(input("Enter an integer N: "))
            result = reverse_number(n)
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")

    print("Reversed Number:")
    print(result)


def test_cases():
    assert reverse_number(123) == 321
    assert reverse_number(0) == 0
    assert reverse_number(5) == 5
    assert reverse_number(9081726354) == 4536271809
    assert reverse_number(-123) == -321
    assert reverse_number(-100) == -1

    try:
        reverse_number(4.5)
        assert False
    except ValueError:
        pass

    try:
        reverse_number("123")
        assert False
    except ValueError:
        pass

    print("All test cases passed!")


if __name__ == "__main__":
    test_cases()
    main()
