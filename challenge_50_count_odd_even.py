def count_odd_even(arr):
    if not isinstance(arr, list):
        raise ValueError("Input must be a list")

    odd = 0
    even = 0

    for x in arr:
        if not isinstance(x, int):
            raise ValueError("Array elements must be integers")

        if x % 2 == 0:
            even += 1
        else:
            odd += 1

    return odd, even


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

    odd, even = count_odd_even(arr)
    print("Odd count:", odd)
    print("Even count:", even)


def test_cases():
    assert count_odd_even([1, 2, 3, 4]) == (2, 2)
    assert count_odd_even([2, 4, 6]) == (0, 3)
    assert count_odd_even([]) == (0, 0)

    try:
        count_odd_even("123")
        assert False
    except ValueError:
        pass

    try:
        count_odd_even([1, "a"])
        assert False
    except ValueError:
        pass

    print("All test cases passed!")


if __name__ == "__main__":
    test_cases()
    main()
