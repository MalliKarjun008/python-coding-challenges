def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def main():
    n = int(input("Enter n: "))
    arr = []
    for _ in range(n):
        arr.append(int(input("Enter element: ")))

    arr.sort()
    target = int(input("Enter element to search: "))

    index = binary_search(arr, target)
    if index == -1:
        print("Element not found")
    else:
        print("Element found at index:", index)


def test_cases():
    assert binary_search([1, 2, 3, 4, 5], 3) == 2
    assert binary_search([1, 2, 3, 4, 5], 6) == -1
    assert binary_search([], 1) == -1
    print("All test cases passed!")


if __name__ == "__main__":
    main()
    test_cases()
