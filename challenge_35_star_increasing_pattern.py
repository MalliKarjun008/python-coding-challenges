def star_increasing_pattern(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer")

    pattern = []
    for i in range(1, n + 1):
        pattern.append('*' * i)

    return pattern


def main():
    while True:
        try:
            n = int(input("Enter a positive integer N: "))
            pattern = star_increasing_pattern(n)
            break
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

    print("Star Increasing Pattern:")
    for line in pattern:
        print(line)


def test_cases():
    assert star_increasing_pattern(3) == ['*', '**', '***']
    assert star_increasing_pattern(1) == ['*']
    assert star_increasing_pattern(5) == ['*', '**', '***', '****', '*****']

    try:
        star_increasing_pattern(0)
        assert False
    except ValueError:
        pass

    try:
        star_increasing_pattern(-3)
        assert False
    except ValueError:
        pass

    try:
        star_increasing_pattern(4.5)
        assert False
    except ValueError:
        pass

    print("All test cases passed!")


if __name__ == "__main__":
    test_cases()
    main()
