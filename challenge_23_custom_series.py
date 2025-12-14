def generate_series(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("N must be a positive integer")

    result = []
    diffs = [4, 4, 4, 8]
    num = 1
    i = 0

    while num <= n:
        result.append(num)
        num += diffs[i]
        i = (i + 1) % len(diffs)

    return result


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
    assert generate_series(50) == [1, 5, 9, 13, 21, 25, 29, 37, 41, 45, 49]
    assert generate_series(45) == [1, 5, 9, 13, 21, 25, 29, 37, 41, 45]
    assert generate_series(20) == [1, 5, 9, 13]
    assert generate_series(1) == [1]

    try:
        generate_series(0)
        assert False
    except ValueError:
        pass

    try:
        generate_series(-10)
        assert False
    except ValueError:
        pass

    try:
        generate_series(7.5)
        assert False
    except ValueError:
        pass

    print("All test cases passed!")


if __name__ == "__main__":
    test_cases()
    main()
