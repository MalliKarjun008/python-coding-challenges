def generate_pattern(n):
    pattern = []
    for i in range(1, n + 1):
        pattern.append(str(i) * i)
    return pattern


def main():
    n = int(input("Enter N: "))
    for row in generate_pattern(n):
        print(row)


def test_cases():
    assert generate_pattern(4) == ["1", "22", "333", "4444"]
    assert generate_pattern(1) == ["1"]
    assert generate_pattern(0) == []
    print("All test cases passed!")


if __name__ == "__main__":
    main()
    test_cases()
