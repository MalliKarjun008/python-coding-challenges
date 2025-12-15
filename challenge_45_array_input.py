def read_array(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("N must be a positive integer")

    arr = []
    for i in range(n):
        arr.append(int(input(f"Enter element {i + 1}: ")))

    return arr


def main():
    while True:
        try:
            n = int(input("Enter number of elements N: "))
            array = read_array(n)
            break
        except ValueError:
            print("Invalid input. Please enter valid integers.")

    print("Array elements:")
    print(array)


def test_cases():
    try:
        read_array(0)
        assert False
    except ValueError:
        pass

    try:
        read_array(-3)
        assert False
    except ValueError:
        pass

    print("Test cases passed (manual input required for full test).")


if __name__ == "__main__":
    test_cases()
    main()
