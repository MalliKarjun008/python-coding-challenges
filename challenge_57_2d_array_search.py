def two_array_search(matrix, target):
    if not isinstance(matrix, list):
        raise ValueError("Input must be a list of lists")

    for row in matrix:
        if not isinstance(row, list):
            raise ValueError("Input must be a list of lists")
        for val in row:
            if not isinstance(val, int):
                raise ValueError("Matrix elements must be integers")

    for row in matrix:
        for val in row:
            if val == target:
                return True

    return False


def main():
    while True:
        try:
            rows = int(input("Enter number of rows: "))
            cols = int(input("Enter number of columns: "))
            if rows < 0 or cols < 0:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Please enter non-negative integers.")

    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            while True:
                try:
                    row.append(int(input(f"Enter element [{i + 1}][{j + 1}]: ")))
                    break
                except ValueError:
                    print("Invalid input. Please enter an integer.")
        matrix.append(row)

    while True:
        try:
            target = int(input("Enter target value to search: "))
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")

    found = two_array_search(matrix, target)

    if found:
        print("Element found in the 2D array.")
    else:
        print("Element not found in the 2D array.")


def test_cases():
    assert two_array_search([[1, 2, 3], [4, 5, 6]], 5) is True
    assert two_array_search([[1, 2, 3], [4, 5, 6]], 7) is False
    assert two_array_search([[]], 1) is False

    try:
        two_array_search("123", 1)
        assert False
    except ValueError:
        pass

    try:
        two_array_search([[1, "a"]], 1)
        assert False
    except ValueError:
        pass

    print("All test cases passed!")


if __name__ == "__main__":
    test_cases()
    main()
