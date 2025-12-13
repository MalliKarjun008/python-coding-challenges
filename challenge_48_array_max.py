def array_max(arr):
    if not arr:
        return None
    m = arr[0]
    for x in arr:
        if x > m:
            m = x
    return m


def main():
    n = int(input("Enter n: "))
    arr = []
    for _ in range(n):
        arr.append(int(input("Enter element: ")))

    result = array_max(arr)
    if result is None:
        print("Array is empty")
    else:
        print("Maximum:", result)


def test_cases():
    assert array_max([3, 1, 4]) == 4
    assert array_max([-5, -2, -10]) == -2
    assert array_max([]) is None
    print("All test cases passed!")


if __name__ == "__main__":
    main()
    test_cases()
