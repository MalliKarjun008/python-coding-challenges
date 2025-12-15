def array_min(arr):
    if not isinstance(arr, list):
        raise ValueError("Input must be a list")

    if not arr:
        return None

    m = arr[0]
    for x in arr:
        if not isinstance(x, int):
            raise ValueError("Array elements must be integers")
        if x < m:
            m = x

    return m


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

    result = array_min(arr)
    if result is None:
        print("Array is empty")
    else:
        print("Minimum:", result)


def test_cases():
    assert array_min([3, 1, 4]) == 1
    assert array_min([-5, -2, -10]) == -10
    assert array_min([]) is None

    try:
        array_min("123")
        assert False
    except ValueError:
        pass

    try:
        array_min([1, "a"])
        assert False
    except ValueError:
        pass

    print("All test cases passed!")


if __name__ == "__main__":
    test_cases()
    main()
