def create_array(n, elements):
    return elements[:n]


def main():
    n = int(input("Enter n: "))
    arr = []
    for _ in range(n):
        arr.append(int(input("Enter element: ")))
    print(create_array(n, arr))


def test_cases():
    assert create_array(3, [1, 2, 3, 4]) == [1, 2, 3]
    assert create_array(0, [1, 2]) == []
    assert create_array(2, [5, 6]) == [5, 6]
    print("All test cases passed!")


if __name__ == "__main__":
    main()
    test_cases()

