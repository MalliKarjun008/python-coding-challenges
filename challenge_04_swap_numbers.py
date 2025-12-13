def swap_numbers(a, b):
    a, b = b, a
    return a, b


def main():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    a, b = swap_numbers(a, b)

    print("After swapping:")
    print("First number:", a)
    print("Second number:", b)


def test_cases():
    assert swap_numbers(10, 20) == (20, 10)
    assert swap_numbers(-5, 5) == (5, -5)
    assert swap_numbers(0, 0) == (0, 0)

    print("All test cases passed!")


if __name__ == "__main__":
    main()
    test_cases()
