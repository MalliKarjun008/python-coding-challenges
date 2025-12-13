def transpose_matrix(matrix):
    if not matrix:
        return []
    rows = len(matrix)
    cols = len(matrix[0])
    transposed = []
    for c in range(cols):
        row = []
        for r in range(rows):
            row.append(matrix[r][c])
        transposed.append(row)
    return transposed


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
    m = [[1, 2], [3, 4]]
    assert transpose_matrix(m) == [[1, 3], [2, 4]]
    assert transpose_matrix([]) == []
    print("All test cases passed!")


if __name__ == "__main__":
    main()
    test_cases()
