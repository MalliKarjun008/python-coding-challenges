def create_2d_array(rows, cols, values):
    matrix = []
    idx = 0
    for _ in range(rows):
        row = []
        for _ in range(cols):
            row.append(values[idx])
            idx += 1
        matrix.append(row)
    return matrix


def main():
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    values = []

    for _ in range(rows * cols):
        values.append(int(input("Enter element: ")))

    matrix = create_2d_array(rows, cols, values)
    for row in matrix:
        print(*row)


def test_cases():
    m = create_2d_array(2, 2, [1, 2, 3, 4])
    assert m == [[1, 2], [3, 4]]

    m = create_2d_array(1, 3, [5, 6, 7])
    assert m == [[5, 6, 7]]

    m = create_2d_array(0, 0, [])
    assert m == []

    print("All test cases passed!")


if __name__ == "__main__":
    main()
    test_cases()
