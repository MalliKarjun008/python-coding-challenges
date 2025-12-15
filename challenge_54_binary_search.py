def binary_search(arr, target):
    if not isinstance(arr, list):
        raise ValueError("Input must be a list")

    for x in arr:
        if not isinstance(x, int):
            raise ValueError("Array elements must be integers")

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
    while True:
        try:
            n = int(input("Enter n: "))
            if n < 0:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Please enter a non-negative integer.")

    arr = []
    for i in range(n):
        while True:
            try:
                arr.append(int(input(f"Enter element {i + 1}: ")))
                break
            except ValueError:
                print("Invalid input. Please enter an integer.")

    # IMPORTANT: sort array before binary search
    arr.sort()

    print("Sorted Array:", arr)

    while True:
        try:
            target = int(input("Enter target value to search: "))
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")

    result = binary_search(arr, target)

    if result != -1:
        print(f"Element found at index: {result}")
    else:
        print("Element not found in the array.")


def test_cases():
    assert binary_search([1, 2, 3, 4, 5], 3) == 2
    assert binary_search([10, 20, 30, 40, 50], 10) == 0
    assert binary_search([5, 15, 25, 35, 45], 50) == -1
    assert binary_search([], 3) == -1
    assert binary_search([7], 7) == 0

    try:
        binary_search("123", 3)
        assert False
    except ValueError:
        pass

    try:
        binary_search([1, "a", 3], 3)
        assert False
    except ValueError:
        pass

    print("All test cases passed!")


if __name__ == "__main__":
    test_cases()
    main()
