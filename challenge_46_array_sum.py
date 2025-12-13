def array_sum(arr):
    total = 0
    for x in arr:
        total += x
    return total


def main():
    n = int(input("Enter n: "))
    arr = []
    for _ in range(n):
        arr.append(int(input("Enter element: ")))
    print("Sum:", array_sum(arr))


def test_cases():
    assert array_sum([1, 2, 3]) == 6
    assert array_sum([]) == 0
    assert array_sum([-1, 1]) == 0
    print("All test cases passed!")


if __name__ == "__main__":
    main()
    test_cases()
