def generate_odd_series(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("N must be a positive integer")
    return [i for i in range(1, n + 1) if i % 2 != 0]


def main():
    while True:
        try:
            n = int(input("Enter N: "))
            series = generate_odd_series(n)
            break
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

    print(*series)


def test_cases():
    assert generate_odd_series(10) == [1, 3, 5, 7, 9]
    assert generate_odd_series(1) == [1]

    try:
        generate_odd_series(0)
        assert False
    except ValueError:
        pass

    try:
        generate_odd_series(-5)
        assert False
    except ValueError:
        pass

    print("All test cases passed!")


if __name__ == "__main__":
    test_cases()
    main()
