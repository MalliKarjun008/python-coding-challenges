def largest_of_three(a, b, c):
    return max(a, b, c)


def main():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    c = float(input("Enter third number: "))

    print("Largest number:", largest_of_three(a, b, c))


def test_cases():
    assert largest_of_three(1, 2, 3) == 3
    assert largest_of_three(10, 5, 7) == 10
    assert largest_of_three(-1, -5, -3) == -1
    assert largest_of_three(0, 0, 0) == 0
    print("All test cases passed!")


if __name__ == "__main__":
    main()
    test_cases()
