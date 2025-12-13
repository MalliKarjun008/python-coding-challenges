def generate_pattern(n):
    result = []
    fact = 1
    current = 1

    for row_len in range(1, n + 1):
        row = []
        for _ in range(row_len):
            fact *= current
            row.append(str(fact))
            current += 1
        result.append(" ".join(row))

    return result


def main():
    n = int(input("Enter N: "))
    for row in generate_pattern(n):
        print(row)


def test_cases():
    assert generate_pattern(3) == [
        "1",
        "1 2",
        "6 24 120"
    ]
    assert generate_pattern(1) == ["1"]
    assert generate_pattern(0) == []
    print("All test cases passed!")


if __name__ == "__main__":
    main()
    test_cases()
