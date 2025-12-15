def sort_array(arr, order):
    if not isinstance(arr, list):
        raise ValueError("Input must be a list")

    for x in arr:
        if not isinstance(x, int):
            raise ValueError("Array elements must be integers")

    if order == "asc":
        return sorted(arr)
    elif order == "desc":
        return sorted(arr, reverse=True)
    else:
        raise ValueError("Order must be 'asc' or 'desc'")


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
        order = input("Enter sorting order (asc/desc): ").strip().lower()
        if order in ("asc", "desc"):
            break
        else:
            print("Invalid input. Please enter 'asc' or 'desc'.")

    sorted_arr = sort_array(arr, order)
    print(f"Sorted Array ({order}):")
    print(sorted_arr)


def test_cases():
    assert sort_array([3, 1, 2], "asc") == [1, 2, 3]
    assert sort_array([3, 1, 2], "desc") == [3, 2, 1]
    assert sort_array([], "asc") == []
    assert sort_array([5], "desc") == [5]

    try:
        sort_array("123", "asc")
        assert False
    except ValueError:
        pass

    try:
        sort_array([1, "a"], "asc")
        assert False
    except ValueError:
        pass

    try:
        sort_array([1, 2, 3], "xyz")
        assert False
    except ValueError:
        pass

    print("All test cases passed!")


if __name__ == "__main__":
    test_cases()
    main()
