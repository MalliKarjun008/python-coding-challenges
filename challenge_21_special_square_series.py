def generate_series(n):
    series = []
    i = 1
    while True:
        sq = i * i
        if sq > n:
            break
        series.append(sq)
        i += 1
    return series


def main():
    n = int(input("Enter N: "))
    print(*generate_series(n))


def test_cases():
    assert generate_series(100) == [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    assert generate_series(10) == [1, 4, 9]
    assert generate_series(1) == [1]
    assert generate_series(0) == []
    print("All test cases passed!")


if __name__ == "__main__":
    main()
    test_cases()
