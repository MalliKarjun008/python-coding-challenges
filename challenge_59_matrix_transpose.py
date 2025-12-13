def transpose_matrix(matrix):
    if not matrix:
        return []
    rows = len(matrix)
    cols = len(matrix[0])
    result = []
    for j in range(cols):
        row = []
        for i in range(rows):
            row.append(matrix[i][j])
        result.append(row)
    return result


def main():
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    matrix = []

    for _ in range(rows):
        row = []
        for _ in range(cols):
            row.append(int(input("Enter element: ")))
        matrix.append(row)

    print("Matrix:")
    for row in matrix:
        print(*row)

    print("Transpose:")
    t = transpose_matrix(matrix)
    for row in t:
        print(*row)


def test_cases():
    assert transpose_matrix([[1, 2, 3], [4, 5, 6]]) == [[1, 4], [2, 5], [3, 6]]
    assert transpose_matrix([[1]]) == [[1]]
    assert transpose_matrix([]) == []
    print("All test cases passed!")


if __name__ == "__main__":
    main()
    test_cases()
