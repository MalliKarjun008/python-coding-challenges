def multiply_matrices(a, b):
    if not a or not b:
        return []

    rows_a = len(a)
    cols_a = len(a[0])
    rows_b = len(b)
    cols_b = len(b[0])

    if cols_a != rows_b:
        return None

    result = [[0 for _ in range(cols_b)] for _ in range(rows_a)]

    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                result[i][j] += a[i][k] * b[k][j]

    return result


def main():
    r1 = int(input("Enter rows of first matrix: "))
    c1 = int(input("Enter columns of first matrix: "))
    a = []
    for _ in range(r1):
        row = []
        for _ in range(c1):
            row.append(int(input("Enter element: ")))
        a.append(row)

    r2 = int(input("Enter rows of second matrix: "))
    c2 = int(input("Enter columns of second matrix: "))
    b = []
    for _ in range(r2):
        row = []
        for _ in range(c2):
            row.append(int(input("Enter element: ")))
        b.append(row)

    result = multiply_matrices(a, b)

    if result is None:
        print("Matrix multiplication not possible")
    else:
        print("Resultant Matrix:")
        for row in result:
            print(*row)


def test_cases():
    a = [[1, 2], [3, 4]]
    b = [[5, 6], [7, 8]]
    assert multiply_matrices(a, b) == [[19, 22], [43, 50]]

    a = [[1, 2, 3]]
    b = [[4], [5], [6]]
    assert multiply_matrices(a, b) == [[32]]

    assert multiply_matrices([[1, 2]], [[1, 2]]) is None

    print("All test cases passed!")


if __name__ == "__main__":
    main()
    test_cases()
