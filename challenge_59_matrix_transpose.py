def transpose_matrix(matrix):
    if not isinstance(matrix, list):
        raise ValueError("Input must be a list of lists")

    if not matrix:
        return []

    cols = len(matrix[0])

    for row in matrix:
        if not isinstance(row, list):
            raise ValueError("Input must be a list of lists")
        if len(row) != cols:
            raise ValueError("All rows must have the same number of columns")
        for val in row:
            if not isinstance(val, int):
                raise ValueError("Matrix elements must be integers")

    rows = len(matrix)
    transposed = []

    for j in range(cols):
        new_row = []
        for i in range(rows):
            new_row.append(matrix[i][j])
        transposed.append(new_row)

    return transposed


def main():
    while True:
        try:
            rows = int(input("Enter number of rows (M): "))
            cols = int(input("Enter number of columns (N): "))
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

    transposed = transpose_matrix(matrix)

    print("\nMatrix:")
    for row in matrix:
        print(row)

    print("\nTranspose of Matrix:")
    for row in transposed:
        print(row)


def test_cases():
    assert transpose_matrix([[1, 2], [3, 4]]) == [[1, 3], [2, 4]]
    assert transpose_matrix([[1, 2, 3]]) == [[1], [2], [3]]
    assert transpose_matrix([[1], [2], [3]]) == [[1, 2, 3]]
    assert transpose_matrix([]) == []

    try:
        transpose_matrix("123")
        assert False
    except ValueError:
        pass

    try:
        transpose_matrix([[1, 2], [3]])
        assert False
    except ValueError:
        pass

    try:
        transpose_matrix([[1, "a"]])
        assert False
    except ValueError:
        pass

    print("All test cases passed!")


if __name__ == "__main__":
    test_cases()
    main()
