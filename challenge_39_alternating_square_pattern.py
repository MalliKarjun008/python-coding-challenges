def generate_pattern(n):
    result = []
    num = 1
    sign = 1
    for i in range(1, n + 1):
        row = []
        for _ in range(i):
            value = (num * num) * sign
            row.append(str(value))
            sign *= -1
            num += 1
        result.append(" ".join(row))
    return result


def main():
    n = int(input("Enter N: "))
    for row in generate_pattern(n):
        print(row)


def test_cases():
    assert generate_pattern(4) == [
        "1",
        "-4 9",
        "-16 25 -36",
        "49 -64 81 -100"
    ]
    assert generate_pattern(1) == ["1"]
    assert generate_pattern(0) == []
    print("All test cases passed!")


if __name__ == "__main__":
    main()
    test_cases()
