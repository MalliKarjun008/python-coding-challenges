def generate_series(n):
    series = []
    current = 1
    primes = [3, 3, 5, 11, 13, 17, 19, 23]
    i = 0

    while current <= n:
        series.append(current)
        if i >= len(primes):
            break
        current += primes[i]
        i += 1

    return series


def main():
    n = int(input("Enter N: "))
    print(*generate_series(n))


def test_cases():
    assert generate_series(25) == [1, 4, 7, 12, 23]
    assert generate_series(10) == [1, 4, 7]
    assert generate_series(1) == [1]
    assert generate_series(0) == []
    print("All test cases passed!")


if __name__ == "__main__":
    main()
    test_cases()
