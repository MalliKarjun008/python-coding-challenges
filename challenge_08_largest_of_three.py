def largest_of_three(a, b, c):
    for value in (a, b, c):
        if not isinstance(value, (int, float)):
            raise ValueError("Inputs must be numeric")
    return max(a, b, c)


def main():
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        c = float(input("Enter third number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values only.")
        return

    try:
        print("Largest number:", largest_of_three(a, b, c))
    except ValueError as e:
        print(e)


def test_cases():
    assert largest_of_three(1, 2, 3) == 3
    assert largest_of_three(10, 5, 7) == 10
    assert largest_of_three(-1, -5, -3) == -1
    assert largest_of_three(0, 0, 0) == 0
    assert largest_of_three(2.5, 2.7, 2.6) == 2.7
    assert largest_of_three(10**9, 5, 7) == 10**9

    try:
        largest_of_three(1, "2", 3)
        assert False
    except ValueError:
        pass

    print("All test cases passed!")


if __name__ == "__main__":
    test_cases()
    main()
