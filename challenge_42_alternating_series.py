def alternating_series(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer")

    series = []
    num = 1

    while num <= n:
        series.append(num)
        num += 4

    return series


def main():
    while True:
        try:
            n = int(input("Enter a positive integer N: "))
            series = alternating_series(n)
            break
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

    print("Series up to N:")
    print(series)


def test_cases():
    assert alternating_series(10) == [1, 5, 9]
    assert alternating_series(1) == [1]
    assert alternating_series(4) == [1]
    assert alternating_series(5) == [1, 5]
    assert alternating_series(20) == [1, 5, 9, 13, 17]

    try:
        alternating_series(0)
        assert False
    except ValueError:
        pass

    try:
        alternating_series(-5)
        assert False
    except ValueError:
        pass

    try:
        alternating_series(3.5)
        assert False
    except ValueError:
        pass

    print("All test cases passed!")


if __name__ == "__main__":
    test_cases()
    main()
