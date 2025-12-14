def swap_numbers(a, b):
    return b, a


def main():
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values only.")
        return

    a, b = swap_numbers(a, b)

    print("After swapping:")
    print("First number:", a)
    print("Second number:", b)


def test_cases():
    assert swap_numbers(10, 20) == (20, 10)
    assert swap_numbers(-5, 5) == (5, -5)
    assert swap_numbers(0, 0) == (0, 0)
    assert swap_numbers(2.5, 7.5) == (7.5, 2.5)
    assert swap_numbers(10**9, -10**9) == (-10**9, 10**9)

    print("All test cases passed!")


if __name__ == "__main__":
    test_cases()
    main()
