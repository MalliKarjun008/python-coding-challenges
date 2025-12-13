def generate_pattern(n):
    return ["*" * n for _ in range(n)]


def main():
    n = int(input("Enter N: "))
    for row in generate_pattern(n):
        print(row)


def test_cases():
    assert generate_pattern(3) == ["***", "***", "***"]
    assert generate_pattern(1) == ["*"]
    assert generate_pattern(0) == []
    print("All test cases passed!")


if __name__ == "__main__":
    main()
    test_cases()
