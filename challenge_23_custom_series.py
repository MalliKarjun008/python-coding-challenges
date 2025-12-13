def generate_series(n):
    series = []
    current = 1
    increments = [4, 4, 4, 8, 4, 4, 8, 4]

    for inc in increments:
        if current > n:
            break
        series.append(current)
        current += inc

    if current <= n:
        series.append(current)

    return series


def main():
    n = int(input("Enter N: "))
    print(*generate_series(n))


def test_cases():
    assert generate_series(50) == [1, 5, 9, 13, 21, 25, 29, 37, 41]
    assert generate_series(20) == [1, 5, 9, 13]
    assert generate_series(1) == [1]
    assert generate_series(0) == []
    print("All test cases passed!")


if __name__ == "__main__":
    main()
    test_cases()
