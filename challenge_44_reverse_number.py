def reverse_number(n):
    sign = -1 if n < 0 else 1
    n = abs(n)
    rev = 0
    while n > 0:
        rev = rev * 10 + (n % 10)
        n //= 10
    return sign * rev


def main():
    n = int(input("Enter number: "))
    print(reverse_number(n))


def test_cases():
    assert reverse_number(1234) == 4321
    assert reverse_number(1000) == 1
    assert reverse_number(-123) == -321
    assert reverse_number(0) == 0
    print("All test cases passed!")


if __name__ == "__main__":
    main()
    test_cases()
