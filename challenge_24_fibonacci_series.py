def generate_series(n):
    series = []
    a, b = 1, 1
    while a <= n:
        series.append(a)
        a, b = b, a + b
    return series


def main():
    n = int(input("Enter N: "))
    print(*generate_series(n))


def test_cases():
    assert generate_series(50) == [1, 1, 2, 3, 5, 8, 13, 21, 34]
    assert generate_series(1) == [1, 1]
    assert generate_series(0) == []
    print("All test cases passed!")


if __name__ == "__main__":
    main()
    test_cases()
