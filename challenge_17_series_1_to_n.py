def generate_series(n):
    return list(range(1, n + 1))


def main():
    n = int(input("Enter N: "))
    series = generate_series(n)
    print(*series)


def test_cases():
    assert generate_series(5) == [1, 2, 3, 4, 5]
    assert generate_series(1) == [1]
    assert generate_series(0) == []
    print("All test cases passed!")


if __name__ == "__main__":
    main()
    test_cases()
