def sum_2d_array(matrix):
    total = 0
    for row in matrix:
        for val in row:
            total += val
    return total


def main():
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    matrix = []

    for _ in range(rows):
        row = []
        for _ in range(cols):
            row.append(int(input("Enter element: ")))
        matrix.append(row)

    print("Sum:", sum_2d_array(matrix))


def test_cases():
    assert sum_2d_array([[1, 2], [3, 4]]) == 10
    assert sum_2d_array([[5]]) == 5
    assert sum_2d_array([]) == 0
    print("All test cases passed!")


if __name__ == "__main__":
    main()
    test_cases()
