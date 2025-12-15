def multiply_matrix(a, b):
    if not isinstance(a, list) or not isinstance(b, list):
        raise ValueError("Inputs must be lists of lists")

    if not a or not b:
        return []

    cols_a = len(a[0])
    rows_b = len(b)

    for row in a:
        if not isinstance(row, list) or len(row) != cols_a:
            raise ValueError("Invalid first matrix")

    cols_b = len(b[0])
    for row in b:
        if not isinstance(row, list) or len(row) != cols_b:
            raise ValueError("Invalid second matrix")

    if cols_a != rows_b:
        raise ValueError(
            "Number of columns in first matrix must equal number of rows in second matrix"
        )

    result = []

    for i in range(len(a)):
        row = []
        for j in range(cols_b):
            cell_sum = 0
            for k in range(cols_a):
                cell_sum += a[i][k] * b[k][j]
            row.append(cell_sum)
        result.append(row)

    return result


def main():
    while True:
        try:
            rows_a = int(input("Enter number of rows for first matrix: "))
            cols_a = int(input("Enter number of columns for first matrix: "))
            if rows_a < 0 or cols_a < 0:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Please enter non-negative integers.")

    matrix_a = []
    for i in range(rows_a):
        row = []
        for j in range(cols_a):
            while True:
                try:
                    row.append(int(input(f"Enter element [{i+1}][{j+1}] for first matrix: ")))
                    break
                except ValueError:
                    print("Invalid input. Please enter an integer.")
        matrix_a.append(row)

    while True:
        try:
            rows_b = int(input("Enter number of rows for second matrix: "))
            cols_b = int(input("Enter number of columns for second matrix: "))
            if rows_b < 0 or cols_b < 0 or cols_a != rows_b:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Columns of first matrix must equal rows of second matrix.")

    matrix_b = []
    for i in range(rows_b):
        row = []
        for j in range(cols_b):
            while True:
                try:
                    row.append(int(input(f"Enter element [{i+1}][{j+1}] for second matrix: ")))
                    break
                except ValueError:
                    print("Invalid input. Please enter an integer.")
        matrix_b.append(row)

    product = multiply_matrix(matrix_a, matrix_b)

    print("Product of the two matrices:")
    for row in product:
        print(row)


def test_cases():
    assert multiply_matrix([[1, 2], [3, 4]], [[5, 6], [7, 8]]) == [[19, 22], [43, 50]]
    assert multiply_matrix([[1, 2, 3]], [[4], [5], [6]]) == [[32]]
    assert multiply_matrix([[1]], [[2]]) == [[2]]

    try:
        multiply_matrix("123", [[1]])
        assert False
    except ValueError:
        pass

    try:
        multiply_matrix([[1, 2]], [[1, 2]])
        assert False
    except ValueError:
        pass

    print("All test cases passed!")


if __name__ == "__main__":
    test_cases()
    main()
