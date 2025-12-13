def generate_series(n):
    series = []
    current = 1
    diff = 1
    while current <= n:
        series.append(current)
        current += diff
        diff += 1
    return series


def main():
    n = int(input("Enter N: "))
    print(*generate_series(n))


def test_cases():
    assert generate_series(25) == [1, 2, 4, 7, 11, 16, 22]
    assert generate_series(9) == [1, 2, 4, 7]
    assert generate_series(1) == [1]
    assert generate_series(0) == []
    print("All test cases passed!")


if __name__ == "__main__":
    main()
    test_cases()
