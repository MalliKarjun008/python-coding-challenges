def generate_series(n):
    series = []
    value = 1
    sign = 1
    while abs(value) <= n:
        series.append(value * sign)
        value += 4
        sign *= -1
    return series


def main():
    n = int(input("Enter N: "))
    print(*generate_series(n))


def test_cases():
    assert generate_series(25) == [1, -5, 9, -13, 17, -21]
    assert generate_series(10) == [1, -5, 9]
    assert generate_series(1) == [1]
    assert generate_series(0) == []
    print("All test cases passed!")


if __name__ == "__main__":
    main()
    test_cases()
