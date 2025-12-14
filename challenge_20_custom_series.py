def custom_series(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer.")
    series = []
    diff = 1
    current = 1
    while current <= n:
        series.append(current)
        current += diff
        diff += 1
    return series


def main():
    while True:
        try:
            n = int(input("Enter a positive integer N: "))
            series = custom_series(n)
            break
        except ValueError:
            print("Invalid input. Please enter a positive integer.")
    print("Custom series up to", n, ":", series)


def test_cases():
    assert custom_series(10) == [1, 2, 4, 7]
    assert custom_series(1) == [1]
    assert custom_series(15) == [1, 2, 4, 7, 11]

    try:
        custom_series(0)
        assert False
    except ValueError:
        pass

    try:
        custom_series(-3)
        assert False
    except ValueError:
        pass

    try:
        custom_series(4.5)
        assert False
    except ValueError:
        pass

    print("All test cases passed!")


if __name__ == "__main__":
    test_cases()
    main()
