def generate_series(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("N must be a positive integer")

    series = []
    current = 1
    diffs = [3, 3, 5, 11]
    i = 0

    while current <= n:
        series.append(current)
        current += diffs[i]
        i = (i + 1) % len(diffs)

    return series


def main():
    while True:
        try:
            n = int(input("Enter N: "))
            series = generate_series(n)
            break
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

    print(*series)


def test_cases():
    assert generate_series(25) == [1, 4, 7, 12, 23]
    assert generate_series(10) == [1, 4, 7]
    assert generate_series(1) == [1]

    try:
        generate_series(0)
        assert False
    except ValueError:
        pass

    try:
        generate_series(-5)
        assert False
    except ValueError:
        pass

    try:
        generate_series(3.5)
        assert False
    except ValueError:
        pass

    print("All test cases passed!")


if __name__ == "__main__":
    test_cases()
    main()
