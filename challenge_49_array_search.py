def search_element(arr, target):
    if not isinstance(arr, list):
        raise ValueError("Input must be a list")

    for x in arr:
        if not isinstance(x, int):
            raise ValueError("Array elements must be integers")

    for i in range(len(arr)):
        if arr[i] == target:
            return i

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

    while True:
        try:
            target = int(input("Enter element to search: "))
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")

    index = search_element(arr, target)

    if index == -1:
        print("Element not found")
    else:
        print("Element found at index:", index)


def test_cases():
    assert search_element([1, 2, 3], 2) == 1
    assert search_element([1, 2, 3], 5) == -1
    assert search_element([], 1) == -1

    try:
        search_element("123", 1)
        assert False
    except ValueError:
        pass

    try:
        search_element([1, "a"], 1)
        assert False
    except ValueError:
        pass

    print("All test cases passed!")


if __name__ == "__main__":
    test_cases()
    main()
