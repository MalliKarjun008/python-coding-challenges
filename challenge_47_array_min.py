def array_min(arr):
    if not arr:
        return None
    m = arr[0]
    for x in arr:
        if x < m:
            m = x
    return m


def main():
    n = int(input("Enter n: "))
    arr = []
    for _ in range(n):
        arr.append(int(input("Enter element: ")))

    result = array_min(arr)
    if result is None:
        print("Array is empty")
    else:
        print("Minimum:", result)


def test_cases():
    assert array_min([3, 1, 4]) == 1
    assert array_min([-5, -2, -10]) == -10
    assert array_min([]) is None
    print("All test cases passed!")


if __name__ == "__main__":
    main()
    test_cases()
