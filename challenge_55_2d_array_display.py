def create_2d_array(rows, cols):
    if not isinstance(rows, int) or not isinstance(cols, int):
        raise ValueError("Rows and columns must be integers")
    if rows < 0 or cols < 0:
        raise ValueError("Rows and columns must be non-negative")

    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(int(input(f"Enter element [{i + 1}][{j + 1}]: ")))
        matrix.append(row)

    return matrix


def main():
    while True:
        try:
            rows = int(input("Enter number of rows: "))
            cols = int(input("Enter number of columns: "))
            matrix = create_2d_array(rows, cols)
            break
        except ValueError:
            print("Invalid input. Please enter valid integers.")

    print("2D Array (Row-wise):")
    for row in matrix:
        print(row)


def test_cases():
    assert create_2d_array(0, 0) == []

    try:
        create_2d_array(-1, 3)
        assert False
    except ValueError:
        pass

    try:
        create_2d_array(2, "3")
        assert False
    except ValueError:
        pass

    print("Test cases passed (manual input required for elements).")


if __name__ == "__main__":
    test_cases()
    main()
