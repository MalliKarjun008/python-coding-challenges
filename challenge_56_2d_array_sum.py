def sum_2d_array(matrix):
    if not isinstance(matrix, list):
        raise ValueError("Input must be a 2D list")

    total = 0
    for row in matrix:
        if not isinstance(row, list):
            raise ValueError("Each row must be a list")
        for val in row:
            if not isinstance(val, int):
                raise ValueError("Matrix elements must be integers")
            total += val

    return total


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

    print("Sum of all elements:", sum_2d_array(matrix))


def test_cases():
    assert sum_2d_array([[1, 2], [3, 4]]) == 10
    assert sum_2d_array([[5]]) == 5
    assert sum_2d_array([]) == 0

    try:
        sum_2d_array("123")
        assert False
    except ValueError:
        pass

    try:
        sum_2d_array([[1, "a"]])
        assert False
    except ValueError:
        pass

    print("All test cases passed!")


if __name__ == "__main__":
    test_cases()
    main()
