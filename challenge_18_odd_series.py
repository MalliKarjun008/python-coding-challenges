def generate_odd_series(n):
    return [i for i in range(1, n + 1) if i % 2 != 0]


def main():
    n = int(input("Enter N: "))
    series = generate_odd_series(n)
    print(*series)


def test_cases():
    assert generate_odd_series(10) == [1, 3, 5, 7, 9]
    assert generate_odd_series(1) == [1]
    assert generate_odd_series(0) == []
    print("All test cases passed!")


if __name__ == "__main__":
    main()
    test_cases()
