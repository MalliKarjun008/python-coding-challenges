def generate_series(n):
    result = []
    i = 2
    while True:
        value = i * i
        if value > n:
            break
        result.append(value)
        i += 2
    return result


def main():
    n = int(input("Enter N: "))
    series = generate_series(n)
    print(*series)


def test_cases():
    assert generate_series(70) == [4, 16, 36, 64]
    assert generate_series(10) == [4]
    assert generate_series(3) == []
    print("All test cases passed!")


if __name__ == "__main__":
    main()
    test_cases()
