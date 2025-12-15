def create_array(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("N must be a non-negative integer")

    arr = []
    for i in range(n):
        arr.append(int(input(f"Enter element {i + 1}: ")))

    return arr


def main():
    while True:
        try:
            n = int(input("Enter n: "))
            array = create_array(n)
            break
        except ValueError:
            print("Invalid input. Please enter a non-negative integer.")

    print("Array elements:")
    print(array)


def test_cases():
    assert create_array(0) == []

    try:
        create_array(-3)
        assert False
    except ValueError:
        pass

    try:
        create_array(3.5)
        assert False
    except ValueError:
        pass

    print("Test cases passed (manual input required for element entry).")


if __name__ == "__main__":
    test_cases()
    main()
