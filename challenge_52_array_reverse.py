def reverse_array(arr):
    if not isinstance(arr, list):
        raise ValueError("Input must be a list")

    for x in arr:
        if not isinstance(x, int):
            raise ValueError("Array elements must be integers")

    return arr[::-1]


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

    print("Reversed Array:")
    print(reverse_array(arr))


def test_cases():
    assert reverse_array([1, 2, 3]) == [3, 2, 1]
    assert reverse_array([]) == []
    assert reverse_array([5]) == [5]

    try:
        reverse_array("123")
        assert False
    except ValueError:
        pass

    try:
        reverse_array([1, "a"])
        assert False
    except ValueError:
        pass

    print("All test cases passed!")


if __name__ == "__main__":
    test_cases()
    main()
