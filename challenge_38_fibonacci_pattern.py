def generate_pattern(n):
    result = []
    a, b = 1, 1
    for i in range(1, n + 1):
        row = []
        for _ in range(i):
            row.append(a)
            a, b = b, a + b
        result.append(" ".join(map(str, row)))
    return result


def main():
    n = int(input("Enter N: "))
    for row in generate_pattern(n):
        print(row)


def test_cases():
    assert generate_pattern(4) == [
        "1",
        "1 2",
        "3 5 8",
        "13 21 34 55"
    ]
    assert generate_pattern(1) == ["1"]
    assert generate_pattern(0) == []
    print("All test cases passed!")


if __name__ == "__main__":
    main()
    test_cases()
