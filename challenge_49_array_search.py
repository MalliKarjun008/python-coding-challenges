def search_element(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


def main():
    n = int(input("Enter n: "))
    arr = []
    for _ in range(n):
        arr.append(int(input("Enter element: ")))

    target = int(input("Enter element to search: "))
    index = search_element(arr, target)

    if index == -1:
        print("Element not found")
    else:
        print("Element found at index:", index)


def test_cases():
    assert search_element([1, 2, 3], 2) == 1
    assert search_element([1, 2, 3], 5) == -1
    assert search_element([], 1) == -1
    print("All test cases passed!")


if __name__ == "__main__":
    main()
    test_cases()
